# Parses a GL5 file and extracts raw data and event information.
import pickle
import sys
import numpy as np
import os
import time
from legacy_codes import *
from message_codes import *
import datetime
import pandas as pd
from Models import *


def typecast(value, dtype):
    value = np.array(value)
    b = value.tobytes()
    return np.frombuffer(b, dtype=dtype)

def typecast_arr(arr, dtype):
    value = np.array(arr)
    result = [];
    b = value.tobytes();
    result = np.frombuffer(b, dtype=dtype)

    return result


def count_set_bits(n):
    n = typecast(n, np.uint16)[0]
    count = 0
    while n:
        count += (n & 1)
        n >>= 1
    return count

def extract_data(input_file_name: str, create_output_file: bool, output_folder: str):
    # Parameters
    skip_mer = 0  # does not extract MER data.
    skip_lf = 0  # does not extract LF data.


    gvars = []

    # TODO: split_records
    split_records = 1  # If set to 1, the records will be split when ADS_EVENT_START_REC event is found
    mer_split_found = 0
    lfp_split_found = 0

    nStimindex=1
    nPulseindex=1

    nSegment = -1
    t = T()

    v_cal_mer = np.ones((2,8)) # MER voltage calibration - two interfaces.
    v_cal_lfs = np.ones((2,8)) #  LFP voltage calibration - two interfaces.
    v_cal_aux = np.ones((1,2)) # voltage calibration - sync interface

    gain = 12 * 5.92 * 2.82
    voltage_calibration = (4/(2^23-1))/ gain

    last_ts = 0
    last_length = 0
    last_raw_ts = 0
    last_aux_ts = 0
    last_lfp_ts = 0
    last_lfp_len = 0
    last_aux_len = 0

    fp = open(input_file_name, 'rb')
    stat = os.stat(input_file_name)
    file_size = stat.st_size # returns size in bytes
    data_size = file_size/4
    num_channels = 8

    ts = []
    ts_lf = []
    ch_index = np.ones((1, num_channels))
    ch_index_lf = np.ones((1, num_channels))
    ch_index_motion = np.ones((1,4)) # 3-axis accelerometer
    ch_index_aux = np.ones((1,num_channels))

    num_msgs = 1

    mer_channel_list = []
    mer_channel_map = 0

    lf_channel_list = []
    lf_channel_map = 0

    file_data: [] = np.frombuffer(fp.read(), dtype='uint32')
    fp.close()
    timeStart = time.time()

    index: int = 0
    while index < len(file_data):
        word = file_data[index]
        index += 1

        if word == SYNC:
            msg_code = int(file_data[index])
            index += 1
            msg_len = file_data[index]
            index += 1

            if msg_code == ADS_DATA_MER:
                num_msgs = num_msgs + 1

                if skip_mer == 1:
                    index += msg_len
                    continue

                msg_bitmap = file_data[index]
                index += 1
                msg_timestamp = file_data[index]
                index += 1

                num_channels = count_set_bits(msg_bitmap)
                num_samples = int((msg_len-2)/ num_channels)
                msg_seq = ( msg_bitmap & int( 'F0000000', 16)) >> 28
                msg_seq += 1

                if last_ts > 0:
                    # if msg_timestamp - last_ts > last_length:
                    #    fprintf( '\nMER. data loss, expected: %d, found: %d', last_ts + last_length, msg_timestamp )
                    #
                    # if msg_timestamp < last_ts:
                    #     fprintf( '\nMER. restart record at : %d, from %d', msg_timestamp, last_ts )

                    last_ts = msg_timestamp
                    last_length = num_samples
                else:
                    last_ts = msg_timestamp
                    last_length = num_samples

                if t.segments[nSegment].start_timestamp_mer == 0:
                    t.segments[nSegment].start_timestamp_mer = msg_timestamp


                if mer_channel_map != msg_bitmap:
                    mer_channel_list = []
                    for k in range(0,8):
                        if 0 != ( msg_bitmap & (1<<k)):
                            mer_channel_list.append(k+1)

                    for i in range(0,num_channels):
                        channel_index = mer_channel_list[i]

                        if channel_index not in t.segments[nSegment].channels:
                            t.segments[nSegment].channels[channel_index] = Channel()

                    mer_channel_map = msg_bitmap

                if split_records == 1:
                    if mer_split_found == 1:
                        for i in range(0,num_channels):
                            channel_index = mer_channel_list[i]
                            ch_index[0][channel_index-1] = 1

                try:
                    if index + (msg_len-2) <= data_size:
                        for i in range(0,num_channels ):
                            channel_index = mer_channel_list[i]
                            m_data = np.array( file_data[index: (index + int(num_samples))] ).astype('int32')
                            m_data = np.multiply(m_data, t.segments[nSegment].v_cal_mer[channel_index] );
                            index += num_samples

                            if channel_index not in t.segments[nSegment].channels:
                                t.segments[nSegment].channels[channel_index] = Channel()

                            t.segments[nSegment].channels[channel_index].continuous[int(ch_index[0][channel_index -1 ]) : int((ch_index[0][channel_index - 1]) + len(m_data))] =  m_data
                            ch_index[0][channel_index - 1] = ch_index[0][channel_index - 1] + len( m_data )

                    if mer_split_found == 1:
                        mer_split_found = 0

                except Exception as err:
                    print( F'\nError at index {index}\n' )
                    raise err

            elif msg_code == LFP_DATA_RAW:
                if skip_lf == 1:
                    index += msg_len
                    continue

                msg_bitmap = file_data[index]
                index += 1
                msg_timestamp = file_data[index]
                index += 1

                num_channels = count_set_bits(msg_bitmap)
                num_samples = int((msg_len-2)/ num_channels)
                #fprintf( '\nmsg_bitmap = %x', msg_bitmap )
                msg_seq = ( msg_bitmap & int( 'F0000000', 16)) >> 28
                msg_seq = msg_seq + 1

                if lf_channel_map != msg_bitmap:
                    lf_channel_list = []
                    for k in range(0, 8):
                        if 0 != ( msg_bitmap & 1 << k):
                            lf_channel_list.append(k+1)

                    for i in range(0,num_channels):
                        channel_index = lf_channel_list[i]

                        if channel_index not in t.segments[nSegment].channels:
                            t.segments[nSegment].channels[channel_index] = Channel()

                    lf_channel_map = msg_bitmap

                if split_records == 1:
                    if lfp_split_found == 1:
                        for i in range(0,num_channels):
                            channel_index = lf_channel_list[i]
                            ch_index_lf[0][channel_index - 1] = 1

                if last_lfp_ts > 0:
                    # if msg_timestamp - last_lfp_ts > float(( float(t.segments[nSegment].sampling_rate_mer)/float(t.segments[nSegment].sampling_rate_lf))*last_lfp_len):
                    #     fprintf( '\nLFP data loss, expected: %d, found: %d, dif = %d', ...
                    #     last_lfp_ts + 32 * last_lfp_len, msg_timestamp, (last_ts + 32 * last_lfp_len) - msg_timestamp )
                    # else:
                    #     fprintf( '\nLFP timestamp OK: last = %d, new: %d', last_ts, msg_timestamp)

                    last_lfp_ts = msg_timestamp
                    last_lfp_len = num_samples

                else:
                    #fprintf( '\nfirst_lfp_ts = %d', msg_timestamp )
                    last_lfp_ts = msg_timestamp
                    last_lfp_len = num_samples
                    ts_lf.append(msg_timestamp)

                if t.segments[nSegment].start_timestamp_lf == 0:
                    t.segments[nSegment].start_timestamp_lf = msg_timestamp

                try:
                    if index + (msg_len-2) <= data_size:
                        for i in range(0,num_channels):
                            channel_index = lf_channel_list[i]

                            m_data = np.array( file_data[index: (index + int(num_samples))] ).astype('int32')
                            m_data = np.multiply(m_data, t.segments[nSegment].v_cal_mer[channel_index] );

                            index += num_samples

                            if channel_index not in t.segments[nSegment].channels:
                                t.segments[nSegment].channels[channel_index] = Channel()

                            t.segments[nSegment].channels[channel_index].lf[int(ch_index_lf[0][channel_index - 1]) : int(ch_index_lf[0][channel_index - 1] + len(m_data) - 1) ] =  m_data
                            ch_index_lf[0][channel_index - 1] = ch_index_lf[0][channel_index - 1] + len( m_data )

                    if lfp_split_found == 1:
                        lfp_split_found = 0

                except Exception as err:
                    print( F'\nError at index {index}\n')
                    raise err

            elif msg_code == MOTION_DATA_MESSAGE:
                msg_bitmap = file_data[index]
                index += 1
                msg_timestamp = file_data[index]
                index += 1

                num_channels = count_set_bits(msg_bitmap)
                num_samples = int((msg_len-2)/(num_channels+1))
                #fprintf( '\nmsg_bitmap = %x', msg_bitmap )
                msg_seq = ( msg_bitmap & int( 'F0000000', 16)) >> 28
                msg_seq = msg_seq + 1

                if t.segments[nSegment](nSegment).motion.start_timestamp == 0:
                    t.segments[nSegment](nSegment).motion.start_timestamp = last_ts

                try:
                    if index + (msg_len-2) <= data_size:
                        if num_channels == 4:
                            for i in range(0,num_channels - 1):
                                if i==1:
                                    for k in range(0,int(num_samples) - 1):
                                        d1 = file_data[index].astype(np.int64)
                                        index = index+1
                                        d2= file_data[index]
                                        index = index+1
                                        # The data is stored in little endian format.
                                        # Must confirm that this holds on other machines if the file
                                        # format is preserved.
                                        start_date = ((d2.astype(np.int64) << 32) | d1.astype(np.int64)).astype(np.int64)
                                        t.segments[nSegment].motion.data.timestamps[ch_index_motion[i]] = start_date
                                        ch_index_motion[i] = (ch_index_motion[i] + 1)

                                elif i==2:
                                    m_data = [typecast(x,np.single) for x in file_data[index: (index + num_samples)]]
                                    t.segments[nSegment].motion.data.X[ch_index_motion[i]: (ch_index_motion[i] + len(m_data))] = m_data
                                    ch_index_motion[i]= (ch_index_motion[i] + len(m_data))
                                    index += num_samples
                                elif i==3:
                                    m_data = [typecast(x,np.single) for x in file_data[index: (index + num_samples)]]
                                    t.segments[nSegment].motion.data.Y[ch_index_motion[i]: (ch_index_motion[i] + len(m_data))] = m_data
                                    ch_index_motion[i]= (ch_index_motion[i] + len(m_data))
                                    index += num_samples
                                elif i==4:
                                    m_data = [typecast(x,np.single) for x in file_data[index: (index + num_samples)]]
                                    t.segments[nSegment].motion.data.Z[ch_index_motion[i]: (ch_index_motion[i] + len(m_data))] = m_data
                                    ch_index_motion[i]= (ch_index_motion[i] + len(m_data))
                                    index += num_samples

                except Exception as err:
                    print( F'\nError at index {index}\n')
                    raise err

            elif msg_code == SYNC_INT_INPUT_DATA:

                msg_bitmap = file_data[index]
                index += 1
                msg_timestamp = file_data[index]
                index += 1

                msg_seq = ( msg_bitmap & int( 'F0000000', 16)) >> 28
                msg_seq = msg_seq + 1

                num_channels = count_set_bits(msg_bitmap)
                num_samples = int((msg_len-2)/ num_channels)
                #fprintf( '\nmsg_bitmap = %x', msg_bitmap )

                if last_aux_ts > 0:
                    # if msg_timestamp - last_aux_ts > (last_aux_len*4):
                    #     fprintf( '\nAUX data loss, expected: %d, found: %d', last_aux_ts + last_aux_len*4, msg_timestamp )
                    #
                    # ts = [ ts msg_timestamp ]
                    last_aux_ts = msg_timestamp
                    #fprintf( '\nlast_ts = %d', msg_timestamp )
                else:
                    print( F'\nfirst aux ts = {msg_timestamp}')
                    last_aux_ts = msg_timestamp

                last_aux_len = msg_len
                #fprintf( '\nnum_channels = %d', num_channels )
                try:

                    for i in range(0,num_channels):
                        if index + num_samples <= data_size:
                            m_data = typecast_arr(file_data[index: (index + num_samples)], np.single)
                            index += num_samples
                            #m_data = voltage_calibration .* m_data

                            # %if( isfield( t(i).channels, 'continuous' ) )
                            #     %t(i).channels.continuous = cat(1,t(i).channels.continuous, m_data)
                            if i not in t.segments[nSegment].aux.channels:
                                t.segments[nSegment].aux.channels[i] = Channel()
                            t.segments[nSegment].aux.channels[i].continuous[int(ch_index_aux[0][i]) : int(ch_index_aux[0][i] + len(m_data))] =  m_data
                            ch_index_aux[0][i] = ch_index_aux[0][i] + len( m_data )
                            # %else
                            # %    t(i).channels.continuous = m_data

                    t.segments[nSegment].aux.timestamps_aux.append(msg_timestamp)

                except Exception as err:
                    print( F'\nError at index {index}\n' )
                    raise err

            elif msg_code == MOTION_SENSOR_EVENT_SAMPLING_RATE:
                sampling_rate = file_data[index]
                index += 1
                t.segments[nSegment][nSegment].motion.sampling_rate = sampling_rate

            elif msg_code == SYNC_INT_EVENT_DIG_INPUT:
                deviceId = file_data[index]
                index += 1
                timestamp = file_data[index]
                index += 1
                port0 = file_data[index]
                index += 1
                port1 = file_data[index]
                index += 1
                port5 = file_data[index]
                port5 = port5 & 1
                index += 1

                t.segments[nSegment].sync.timestamps.append(timestamp)
                t.segments[nSegment].sync.port1.append(port0)
                t.segments[nSegment].sync.port2.append(port1)
                t.segments[nSegment].sync.digin.append(port5)

            elif msg_code == SYNC_INT_EVENT_REALTIME_DIG_INPUT:
                deviceId = file_data[index]
                index += 1
                ntimestamps = msg_len -1
                for i in range(0,ntimestamps):
                    timestamp = file_data[index]
                    index += 1
                    t.segments[nSegment].sync.rt_timestamps.append(timestamp)

            elif msg_code == SYNC_INT_EVENT_SAMPLING_RATE:
                sampling_rate = file_data[index]
                index += 1

                t.segments[nSegment].aux.sampling_rate = sampling_rate

            elif msg_code == STIM_EVENT_STIM_ON:
                deviceId =file_data[index]
                index += 1
                stim_on_ts = file_data[index]
                index += 1

                if nStimindex not in t.segments[nSegment].stim_params:
                    t.segments[nSegment].stim_params[nStimindex] = StimParams()

                t.segments[nSegment].stim_params[nStimindex].stim_on = stim_on_ts

                print( F'\nStim On TS = {stim_on_ts}' )
                print( F'\nStim index TS = {nStimindex}' )

            elif msg_code == STIM_EVENT_STIM_OFF:
                deviceId =file_data[index]
                index += 1
                stim_off_ts = file_data[index]
                index += 1

                if nStimindex not in t.segments[nSegment].stim_params:
                    t.segments[nSegment].stim_params[nStimindex] = StimParams()

                t.segments[nSegment].stim_params[nStimindex].stim_off = stim_off_ts
                nStimindex=nStimindex+1
                nPulseindex=1
                print( F'\nStim Off TS = {stim_off_ts}')

            elif msg_code == STIM_EVENT_STIM_TYPE:
               device_id = file_data[index]
               index += 1
               stim_type = file_data[index]  # 0 - microstimulation, 1 - macrostimulation
               index += 1

               if nStimindex not in t.segments[nSegment].stim_params:
                   t.segments[nSegment].stim_params[nStimindex] = StimParams()

               t.segments[nSegment].stim_params[nStimindex].stim_type = stim_type
               print( 1, F'\nDevice {device_id}: stimulation type: 0x{stim_type}')

            elif msg_code == STIM_EVENT_OPERATING_MODE:
               device_id = file_data[index]
               index += 1
               stim_mode = file_data[index] # 0 - Constant Current, 1 - Constant Voltage
               index += 1

               if nStimindex not in t.segments[nSegment].stim_params:
                   t.segments[nSegment].stim_params[nStimindex] = StimParams()

               t.segments[nSegment].stim_params[nStimindex].stim_mode = stim_mode
               print( 1, F'\nDevice {device_id}: stimulation type: 0x{stim_mode}')

            elif msg_code == STIM_EVENT_CUSTOM_WAVEFORM:
                waveform_id = []
                for i in range(1,4):
                    waveform_id.append((int(file_data[index]) & int('FF000000')) >> 24)
                    waveform_id.append((int(file_data[index]) & int('00FF0000')) >> 16)
                    waveform_id.append((int(file_data[index]) & int('0000FF00')) >> 8)
                    waveform_id.append(int(file_data[index]) & int('000000FF'))
                    index += 1

                if nStimindex not in t.segments[nSegment].stim_params:
                    t.segments[nSegment].stim_params[nStimindex] = StimParams()

                t.segments[nSegment].stim_params[nStimindex].identifier = waveform_id
                print(F'\nWaveId = {waveform_id}')

            elif msg_code == STIM_EVENT_PULSE_FREQUENCY:
               mdata = file_data[index: (index + msg_len)]
               index += msg_len
               device_id = mdata[0]
               output_channel = mdata[1]+1
               frequency = mdata[2]


               #t.segments[nSegment](nSegment).stim_params(nStimindex).pulse_freq = frequency

               if nStimindex not in t.segments[nSegment].stim_params:
                   t.segments[nSegment].stim_params[nStimindex] = StimParams()

               if nPulseindex in t.segments[nSegment].stim_params[nStimindex].pulse:
                   if t.segments[nSegment].stim_params[nStimindex].pulse[nPulseindex].freq != 0:
                       nPulseindex += 1

               if nPulseindex not in t.segments[nSegment].stim_params[nStimindex].pulse:
                   t.segments[nSegment].stim_params[nStimindex].pulse[nPulseindex] = Pulse()

               t.segments[nSegment].stim_params[nStimindex].pulse[nPulseindex].freq = frequency
               t.segments[nSegment].stim_params[nStimindex].pulse[nPulseindex].channel=output_channel

               print( 1, F'\nDevice {device_id}: channel {output_channel}, stimulation frequency: {frequency}')

            elif msg_code== STIM_EVENT_PULSE_AMPLITUDE:
               mdata = file_data[index: (index + msg_len)]
               index += msg_len
               device_id = mdata[0]
               output_channel = mdata[1]+1
               amplitude = typecast(mdata[2], np.single)[0]
               #t.segments[nSegment](nSegment).stim_params(nStimindex).pulse_amplitude = amplitude

               if nStimindex not in t.segments[nSegment].stim_params:
                   t.segments[nSegment].stim_params[nStimindex] = StimParams()

               if nPulseindex not in t.segments[nSegment].stim_params[nStimindex].pulse:
                   t.segments[nSegment].stim_params[nStimindex].pulse = Pulse()

               t.segments[nSegment].stim_params[nStimindex].pulse[nPulseindex].amplitude = amplitude
               print( 1, F'\nDevice {device_id}: channel {output_channel}, stimulation pulse amplitude: {amplitude}')

            elif msg_code == STIM_EVENT_PULSE_DURATION:
               mdata = file_data[index: (index + msg_len)]
               index += msg_len
               device_id = mdata[0]
               output_channel = mdata[1]+1
               duration = mdata[2]

               #t.segments[nSegment](nSegment).stim_params(nStimindex).pulse_duration = duration

               if nStimindex not in t.segments[nSegment].stim_params:
                   t.segments[nSegment].stim_params[nStimindex] = StimParams()

               if nPulseindex not in t.segments[nSegment].stim_params[nStimindex].pulse:
                   t.segments[nSegment].stim_params[nStimindex].pulse = Pulse()

               t.segments[nSegment].stim_params[nStimindex].pulse[nPulseindex].duration = duration
               print( 1, F'\nDevice {device_id}: channel {output_channel}, stimulation pulse duration (ticks): {duration}')

            elif msg_code == STIM_EVENT_PULSE_PHASE:
               mdata = file_data[index: (index + msg_len)]
               index += msg_len
               device_id = mdata[0]
               output_channel = mdata[1]+1
               phase = mdata[2]  # 0 - monophasic, 1-biphasic

               #t.segments[nSegment](nSegment).stim_params(nStimindex).pulse_phase = phase
               if nStimindex not in t.segments[nSegment].stim_params:
                   t.segments[nSegment].stim_params[nStimindex] = StimParams()

               if nPulseindex not in t.segments[nSegment].stim_params[nStimindex].pulse:
                   t.segments[nSegment].stim_params[nStimindex].pulse = Pulse()

               t.segments[nSegment].stim_params[nStimindex].pulse[nPulseindex].phase = phase
               print( 1, F'\nDevice {device_id}: channel {output_channel}, stimulation pulse phase (ticks): {phase}')

            elif msg_code == STIM_EVENT_PULSE_POLARITY:
               mdata = file_data[index: (index + msg_len)]
               index += msg_len
               device_id = mdata[0]
               output_channel = mdata[1]+1
               polarity = mdata[2] # 0 - negative, 1 - positive

               #t.segments[nSegment](nSegment).stim_params(nStimindex).pulse_polarity = polarity
               if nStimindex not in t.segments[nSegment].stim_params:
                   t.segments[nSegment].stim_params[nStimindex] = StimParams()

               if nPulseindex not in t.segments[nSegment].stim_params[nStimindex].pulse:
                   t.segments[nSegment].stim_params[nStimindex].pulse = Pulse()

               t.segments[nSegment].stim_params[nStimindex].pulse[nPulseindex].polarity = polarity
               print( 1, F'\nDevice {device_id}: channel {output_channel}, stimulation pulse polarity: {polarity}')

            elif msg_code == STIM_EVENT_OUTPUT_CHANNELS:
               mdata = file_data[index: (index + msg_len)]
               index += msg_len
               device_id = mdata[0]
               output_channel = mdata[1]
               channel_map = mdata[2]
               if nStimindex not in t.segments[nSegment].stim_params:
                   t.segments[nSegment].stim_params[nStimindex] = StimParams()

               t.segments[nSegment].stim_params[nStimindex].output_channel_map = channel_map
               print( 1, F'\nDevice {device_id}: channel {output_channel}, stimulation output channels (hex map): 0x{channel_map}')

            elif msg_code == STIM_EVENT_RETURN_CHANNELS:
               mdata = file_data[index: (index + msg_len)]
               index += msg_len
               device_id = mdata[0]
               output_channel = mdata[1]
               channel_map = mdata[2]

               if nStimindex not in t.segments[nSegment].stim_params:
                   t.segments[nSegment].stim_params[nStimindex] = StimParams()

               t.segments[nSegment].stim_params[nStimindex].return_channel_map = channel_map
               print( 1, F'\nDevice {device_id}: channel {output_channel}, stimulation return channels (hex map): 0x{channel_map}')


            elif msg_code == ADS_EVENT_CLASSIFICATION:
                mdata = file_data[index: (index + msg_len)]
                index += msg_len

                position = mdata[0:1] # 64-bit position in file.
                channel = mdata[2]    # channel number
                guid = mdata[3:]   # event guid.

                #fdisp(1, '\nEvent at channel %d, ts = %d', channel, last_ts)


            elif msg_code == HMS_EVENT_BOARD_TYPE:
                m_board_type = file_data[index]
                index += 1
                m_device_id = file_data[index]
                index += 1
                t.device.board_type = m_board_type
                print( 1,F'\nReceived board type = {m_board_type}, device id = {m_device_id}')

    #        ---------------------------------------------------------
            elif msg_code == HMS_EVENT_MER_VOLTAGE_CALIBRATION:
                m_channel = file_data[index]
                index += 1
                m_device_id = file_data[index]
                index += 1
                m_vcal = typecast(file_data[index], np.single)[0]
                index += 1

                offset_dc = typecast(file_data[index], np.int32)[0]
                index += 1
                offset_ac = typecast(file_data[index], np.int32)[0]
                index += 1

                #fprintf(1, '\nMER voltage calibration on device %d, channel %d = %f', ...
                #    m_device_id, m_channel, m_vcal)
                if m_device_id >= 0 and m_device_id < len(v_cal_mer):
                    if m_channel >= 0 and  m_channel < len(v_cal_mer[0]):
                        t.segments[nSegment].v_cal_mer[m_channel+1] = m_vcal
                        t.segments[nSegment].offset_dc_mer[m_channel+1] = offset_dc
                        t.segments[nSegment].offset_ac_mer[m_channel+1] = offset_ac
                    else:
                        print(1,F'\nMER channel out of range {m_channel}')
                else:
                    print(1,F'\nMER device id out of range {m_device_id}')

            # ---------------------------------------------------------
            elif msg_code == HMS_EVENT_LFP_VOLTAGE_CALIBRATION:
                m_channel = file_data[index]
                index += 1
                m_device_id = file_data[index]
                index += 1
                m_vcal = typecast(file_data[index], np.single)[0]
                index += 1
                offset_dc = typecast(file_data[index], np.int32)[0]
                index += 1
                #fprintf(1, '\nLFP voltage calibration on device %d, channel %d = %f', ...
                #    m_device_id, m_channel, m_vcal)
                if m_device_id >= 0 and m_device_id < len(v_cal_lfs):
                    if m_channel >= 0 and  (m_channel) <= len(v_cal_lfs[1]):
                        t.segments[nSegment].v_cal_lf[m_channel+1] = m_vcal
                        t.segments[nSegment].offset_dc_lfs[m_channel+1] = offset_dc
                    else:
                        print(1,F'\nLF channel out of range {m_channel}')
                else:
                    print(1,F'\nLF device id out of range {m_device_id}')

            elif msg_code == EVENT_FILE_HEADER:
                file_type = file_data[index]
                index += 1

                version = file_data[index]
                index += 1
                deviceId= file_data[index]
                index = index+1

                #start_date = int64(0)
                d1 = file_data[index]
                index = index+1
                d2= file_data[index]
                index = index+1
                # The data is stored in little endian format.
                # Must confirm that this holds on other machines if the file
                # format is preserved.
                start_date = (d2.astype(np.int64) << 32) | d1.astype(np.int64).astype(np.int64)

                index1 = file_data[index]
                index = index+1
                index2= file_data[index]
                index = index+1
                #index = int( (int(index2) << 32)| int(index1))

                # d = datenum(start_date)
                #fdisp('\nfileType = 0x%x, version = %d, device = %d', file_type, version, deviceId)

                t.file_info.version = version
                t.file_info.deviceId = deviceId
                t.file_info.start_time =  pd.to_datetime(start_date, unit='ns')
                # t.fileInfo.dateStr = string(t.fileInfo.start_time.ToString)
                #t.fileInfo.Index = index

            elif msg_code == HMS_EVENT_MER_SAMPLING_RATE:
                device_id = file_data[index]
                index += 1
                sampling_rate = file_data[index].astype(np.single)
                index += 1
                print(F'\nMER sampling rate = {sampling_rate}')
                if 0 <= device_id < 2:
                    t.segments[nSegment].sampling_rate_mer.append(sampling_rate)

            elif msg_code == HMS_EVENT_LFS_SAMPLING_RATE:
                device_id = file_data[index]
                index += 1
                sampling_rate = file_data[index].astype(np.single)
                index += 1
                print(F'\nLF sampling rate = {sampling_rate}')
                if 0 <= device_id < 2:
                    t.segments[nSegment].sampling_rate_lf.append(sampling_rate)
            elif msg_code == ADS_EVENT_START_REC:
                print(1, '\nStart recording')
                data = file_data[index]
                index += 1
                mer_split_found = 1
                lfp_split_found = 1
                nSegment = nSegment + 1
                t.segments.append(Segment())
                nStimindex=1
                nPulseindex=1
                ch_index_motion = np.ones((1,4)) # reset motion sensor indexes.
                ch_index_aux = np.ones((1,8))
            elif msg_code == ADS_EVENT_STOP_REC:
                print(1, '\nStop recording')
                if index + 1 < len(file_data):
                    data = file_data[index]
                    index += 1

            elif msg_code == CPM_TEMP_EVENT_LOCAL:
                #Extract temperature data, in degrees Celsius, not stored.
                data = file_data[index]
                index += 1
            elif msg_code == MTC_EVENT_DRIVE_POSITION:
                side = file_data[index]
                index += 1
                position = file_data[index]
                index += 1

                next_depth1 = file_data[index]
                index += 1
                next_depth2 = file_data[index]
                index += 1

                hemi = 'none'
                if side == 1:
                    hemi = 'left'
                elif side == 2:
                    hemi = 'right'

                if side not in t.segments[nSegment].drive:
                    t.segments[nSegment].drive[side] = Drive()

                t.segments[nSegment].drive[side].drive_depths.append(position)
                t.segments[nSegment].drive[side].timestamps.append(last_ts)

                print(1, F'\n side = {hemi}, position = {position} um')
            else:
                print(F'\nUnknown code 0x{msg_code}')
                index += msg_len
        elif index <= len(file_data):
            print( 1, '\nOut of SYNC, ', word )

    print('\n')
    timeStop = time.time()
    print("Elapsed time: ", timeStop - timeStart)

    #Optional - write structure to file:
    if create_output_file:
        output_file_name = output_folder + os.path.splitext(os.path.basename(input_file_name))[0] + '.glpy'
        with open(output_file_name, 'wb') as output_file:
            pickle.dump(t, output_file)

    return t


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please specify file name!')
    else:
        create_output_file = True  # creates a file containing the output object
        output_folder = ""  # file path for the output file; if create_output_file is False than this parameter isn't used
        extract_data(sys.argv[1], create_output_file, output_folder)
