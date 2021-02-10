# This script performs data alignment given two Guideline 5 .gld file,
# where one is configured as uE Interface and the other as Lf Interface.
# Parameters:
# merFile - Full path to the uE Interface data file.
# eogFile - Full path to the Lf Interface data file.
# Return values:
# t1 - data structure holding the uE Interface aligned data.
# t2 - data structure holding the Lf Interface aligned data.


from GLDFile import *
import math


def gld_align(merFile: str, eogFile: str):
    do_correction = 1
    t1 = extract_data(merFile, True, "")
    t2 = extract_data(eogFile, True, "")

    n = len(t1.segments)
    segs = list(range(0, n))

    for k in range(0, n):
        nseg = k
        if nseg not in segs:
            continue

        sf_mer = t1.segments[nseg].sampling_rate_mer[0]  # MER sampling rate recorded on the first device.
        sf_eog = t2.segments[nseg].sampling_rate_lf[0]  # EOG data sampling rate recorded on the second device.
        sf_lfp = t1.segments[nseg].sampling_rate_lf[0]  # EOG data sampling rate recorded on the second device.

        # drop very short data trials.
        nsec = math.floor(len(t1.segments[nseg].channels[1].continuous) / 32000)
        if nsec < 1:
            continue

        ts_mer = (t1.segments[nseg].start_timestamp_mer).astype(np.double)
        ts_eog = (t2.segments[nseg].start_timestamp_lf).astype(np.double)

        # Align MER (uE Interface 1) and LF (Lf Interface) data using timestamps.
        tsd = ts_mer - ts_eog
        if do_correction == 1:
            if tsd > 0:
                offset_eog = np.int32(math.ceil(
                    tsd.astype(np.double) / sf_mer.astype(np.double) * sf_eog.astype(np.double) + 0.5))
                offset_mer = 1
                t2.segments[nseg].start_timestamp_lf = t2.segments[nseg].start_timestamp_lf + np.uint32(math.ceil(
                    offset_eog.astype(np.double) / sf_eog.astype(np.double) * sf_mer.astype(np.double) + 0.5))
            else:
                offset_eog = 1
                offset_mer = abs(tsd)
                ts_mer = ts_mer + offset_mer
                t1.segments[nseg].start_timestamp_mer = ts_mer

            if offset_mer <= 0:
                offset_mer = 1

            if offset_eog <= 0:
                offset_eog = 1

        else:
            offset_eog = 1
            offset_mer = 1

        # Align MER channels on the first interface
        mer_length = 0
        for j in t1.segments[nseg].channels.keys():
            if t1.segments[nseg].channels[j] != Channel():
                t1.segments[nseg].channels[j].continuous = t1.segments[nseg].channels[j].continuous[
                                                           int(offset_mer) - 1:]
                mer_length = len(t1.segments[nseg].channels[j].continuous)

        # Align EOG channels on the second (Lf) interface
        for j in t2.segments[nseg].channels.keys():
            if t2.segments[nseg].channels[j].lf:
                t2.segments[nseg].channels[j].lf = t2.segments[nseg].channels[j].lf[int(offset_eog) - 1:]

        # Align LF channels on the first (uE) interface
        ts_lfp = t1.segments[nseg].start_timestamp_lf
        tsd = ts_mer - ts_lfp
        if do_correction == 1:
            if tsd > 0:
                offset_lf = np.int32(
                    math.ceil(np.double(tsd) / np.double(sf_mer) * np.double(sf_lfp)))
            else:
                offset_lf = 1

            if offset_lf <= 0:
                offset_lf = 1

        else:
            offset_lf = 1

        for j in t1.segments[nseg].channels.keys():
            if t1.segments[nseg].channels[j].lf:
                t1.segments[nseg].channels[j].lf = t1.segments[nseg].channels[j].lf[int(offset_lf) - 1:]

        # Re-create digital input signal from timestamps
        if t1.segments[nseg].sync:
            if t1.segments[nseg].sync.rt_timestamps:
                rt_align = [x.astype(np.double) - ts_mer + 5 for x in t1.segments[nseg].sync.rt_timestamps]
                ts_rt = [x / sf_mer for x in rt_align]
                digin = np.zeros(mer_length)
                state = 0
                for i in range(0, len(rt_align) - 1):
                    digin[int(rt_align[i]):int(rt_align[i + 1])] = (state + 1) % 2
                    state = state + 1

                # Re-create digital input signal.
                t1.segments[nseg].sync.digin = digin
                t1.segments[nseg].sync.rt_timestamps = np.linspace(0, len(digin) / sf_mer, num=len(digin))

    return t1, t2
