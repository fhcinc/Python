#/**
#@file    message.h
#@brief   Defines communication message codes and specific macros.
#
#@details
#The message codes defined in this file are used to implement the
#eRPC (embedded Remote Procedure Call) protocol.
#This header defines module codes on the uper 16 bits of a 32 bit word and
#function codes on the lower 16 bits of the same word to accomplish a
#module.function couple that can be decoded and the corresponding functio.
#Module codes are identified by applying the mask: MODULE_MASK,
#while data codes are identified by applying the mask: DATA_MASK.
#
#@author		Cosmin Serban
#@copyright Termobit. All rights reserved.
#
#@version 0.2
#*/
#
##ifndef _MESSAGE_H_
##define _MESSAGE_H_
#
#/** The length of the standard eRPC header.
#	Please see the eRPC protocol documentation for more information.
#*/
RPC_HEADER_LENGTH         =              int( '3', 16)
#
#/** The length of the standard eRPC data header.
#Please see the eRPC protocol documentation for more information.
#*/
DATA_HEADER_LENGTH        =              int( '5', 16)
#
#/** The standard eRPC synchronization word.
#	Please see the eRPC protocol documentation for more information.
#*/
SYNC                      =              int( '10000001', 16)
#
#/** The eRPC function call code.
#Please see the eRPC protocol documentation for more information.
#*/
FUNCTION_CALL_CODE        =              int( 'C0000000', 16)
#
#/** The eRPC data code.
#Please see the eRPC protocol documentation for more information.
#*/
DATA_CODE                 =              int( '30000000', 16)
#
#/** The eRPC function response code.
#Please see the eRPC protocol documentation for more information.
#*/
RESPONSE_CODE             =              int( 'A0000000', 16)
#
#/** The eRPC function fault code.
#Please see the eRPC protocol documentation for more information.
#*/
FAULT_CODE                =              int( '50000000', 16)
#
#/** The eRPC event code.
#Please see the eRPC protocol documentation for more information.
#*/
EVENT_CODE                =              int( '90000000', 16)
#
#/** The eRPC diagnosis.
#Please see the eRPC protocol documentation for more information.
#*/
DIAGNOSIS_CODE            =              int( '70000000', 16)
#
#/** The standard eRPC type mask.
#Please see the eRPC protocol documentation for more information.
#*/
TYPE_MASK                 =              int( 'F0000000', 16)
#
#/** The standard eRPC module mask.
#Please see the eRPC protocol documentation for more information.
#*/
MODULE_MASK               =              int( '0FFF0000', 16)
#
#/** The standard eRPC module and function mask.
#Please see the eRPC protocol documentation for more information.
#*/
MODULE_AND_FUNCTION_MASK  =              int( '0FFFFFFF', 16)
#
#/** The standard eRPC data code mask.
#Please see the eRPC protocol documentation for more information.
#*/
DATA_CODE_MASK            =              int( '0FFFFFFF', 16)
#
#/** The standard eRPC function code mask.
#Please see the eRPC protocol documentation for more information.
#*/
FUNCTION_MASK             =              int( '0000FFFF', 16)
#
#/** This code is not used in firmware, however,
#to ensure consistency with this header's usage, we define it here.*/
NIRS_DATA_CODE            =              int( '3000FFFF', 16)
#
#/** The Guideline 5 ADS module.
#*/
MODULE_ADS                =              int( '00010000', 16)
#
#/** The Guideline 5 Wiznet module.
#	Handles TCP/IP communication with remote clients. Application independent.
#*/
MODULE_W5200              =              int( '00020000', 16)
#
#/** The Guideline 5 EEPROM module.
#	Application dependent in terms of values being preserved.
#	Stores APM-03 specific information, such as serial numbers, IP addresses, etc.
#*/
MODULE_CPM_EEPROM         =              int( '00030000', 16)
#
#/** The Guideline 5 Central Processing Module.
#	Handles general functionality, application independent.
#*/
MODULE_CPM                =              int( '00040000', 16)
#
#/** The Guideline 5 stimulation module.
#	Handles functionality pertaining to configuration and generation of stimulation
#	and impedance measurement waveforms.
#	Application dependent.
#*/
MODULE_STIM               =              int( '00050000', 16)
#
#/** The Guideline 5 Flash module.
#	Handles reading and writing to the on-board APM-03 flash memory.
#	Used during firmware updgrade procedures.
#	Application independent.
#*/
MODULE_FLASH              =              int( '00060000', 16)
#
#/// @cond DO_NOT_DOCUMENT
#/** Not used.
#*/
MODULE_GPIO               =              int( '00070000', 16)
#
#/** Not used. Octal DAC module code.
#*/
MODULE_DAC8               =              int( '00080000', 16)
#
#/** Not used. Filter module code.
#*/
MODULE_FILTER             =              int( '00090000', 16)
#
#/** Not used.
#*/
MODULE_KNOB               =              int( '000A0000', 16)
#
MODULE_LFP                =              int( '000C0000', 16)
#
MODULE_EQ                 =              int( '000D0000', 16)
#/// @endcond
#
#/** The Guideline 5 remote controller driver.
#*/
MODULE_REMOTE             =              int( '000B0000', 16)
#
#/** The Guideline 5 CODEC driver. Handles analog outputs and
#	analog inputs on the Sync Interface.
#*/
MODULE_AUDIO              =              int( '000E0000', 16)
#
#/** Not used.
#*/
MODULE_TEMP               =              int( '00100000', 16)
#
#/** The Guideline 5 HMS (Headstage MER-Stim) module.
#	Implements the uE Interface and Lfs Interface driver.
#*/
MODULE_HMS                =              int( '00200000', 16)
#
#/** General Guideline 5 application module.
#*/
MODULE_GL5K               =              int( '00300000', 16)
#
#/** The Guideline 5 microTargeting Controller module.
#	Used in the mTC firmware code only. .
#*/
MODULE_MTC                =              int( '00400000', 16)
#
#/** The Sync Interface module.
#*/
MODULE_SYNC_INTERFACE     =              int( '00500000', 16)
#
#/** Represents messages pertaining to APM file properties.
#This is not mapped to a firmware module, but is a means
#of defining a consistent message coding scheme.
#*/
MODULE_APM_FILE           =              int( '01000000', 16)
#
#/** Designates NULL data, filling the data buffer when the lead is off or other
#erroneous events occur.
#*/
NULL_DATA                 =              int( '20000002', 16)
#
#/**This is a special code that we send when not streaming data to
#keep the connection alive, otherwise the uplink host will timeout and
#close connection thinking we have a problem. */
KEEP_ALIVE_EVENT_CODE     =              int( '90000000', 16)
#
#/// @cond DO_NOT_DOCUMENT
##if 0
ADS_SET_SAMPLING_RATE     =              int( '0001000F', 16)
ADS_SET_GAIN              =              int( '00010002', 16)
ADS_START_RECORDING       =              int( '00010003', 16)
ADS_SET_ACTIVE_CHANNELS   =              int( '00010004', 16)
ADS_SET_INPUT_MUX         =              int( '00010005', 16)
ADS_GET_SAMPLING_RATE     =              int( '00010006', 16)
ADS_SET_CHANNEL_GAIN      =              int( '00010007', 16)
ADS_ENABLE_NOISE_REMOVAL  =              int( '00010008', 16)
ADS_ENABLE_FILTER         =              int( '00010009', 16)
#
ADS_REGISTER_DUMP         =              int( '0001000A', 16)
ADS_AUTOSET_GAIN          =              int( '0001000B', 16)
ADS_AUTOSET_OFFSET        =              int( '0001000C', 16)
ADS_AUTOCALIBRATE_OFFSET  =              int( '0001000D', 16)
ADS_CONFIG_DAC_LOOP       =              int( '0001000E', 16)
#
ADS_SET_MONITORED_CHANNELS =              int( '0001000F', 16)
#
#/** Initiates impedance measurement.
#	@param duration Measurement duration.
#	@param current Measurement current (predefined values).
#*/
ADS_START_ZCHECK          =              int( '00010010', 16)
#
#/**
#	Autocalibrate Z Check.
#	All EEG inputs must be shorted before calling this function.
#	@param num_cycles Number of measurement cycles to average before storing
#	the calibration constants.
#*/
ADS_AUTOCALIBRATE_ZCHECK  =              int( '00010011', 16)
ADS_AUTOCALIBRATE_GAIN    =              int( '00010012', 16)
ADS_STORE_CALIBRATION     =              int( '00010013', 16)
##endif
#/// @endcond
#
#/**@ brief ADS continuous data code. Not used. */
ADS_DATA_CONTINUOUS       =              int( '30010001', 16)
#/**@ brief ADS raw data code. Not used. */
ADS_DATA_RAW              =              int( '30010002', 16)
#
#/**@ brief MER data code.
#	1. Message code: ADS_DATA_MER
#	2. Message length: (2 + nChannels * nSamplesPerChannel)
#	3. Active channels bitmap
#	4. Timestamp (unsigned int)
#	5. N channels of M samples each.
#	Please see the eRPC protocol documentation for more information on
#	the data code message format.
#*/
ADS_DATA_MER              =              int( '30010003', 16)
#
#/**@ brief MER data code.
#1. Message code: ADS_DATA_MER
#2. Message length: (3 + nChannels * nSamplesPerChannel)
#3. Active channels bitmap
#4. Timestamp (unsigned int)
#5. Stimulation channel map.
#	During stimulation, the pulse map reflects the onset of each stimulus, per channel.
#	This is a bitmap: each channel is allocated 4 bits [ channel 0 the 4 - LSBs to channel 7 - the 4 MSBs].
#	Each group of 4 bits represents the stimulus onset offset from the data message timestamp.
#	An empty slot is denoted by the code 0xF or -1.
#6. N channels of M samples each.
#Please see the eRPC protocol documentation for more information on
#the data code message format.
#*/
ADS_DATA_MER_STIM         =              int( '30010004', 16)
#
#
##if 0
#/******************************************************************************
#* ADS1299 event codes.
#*
#*******************************************************************************/
#/** @def ADS_EVENT_LEAD_OFF_P
#*/
ADS_EVENT_LEAD_OFF_P      =              int( '90011001', 16)
ADS_EVENT_LEAD_OFF_N      =              int( '90011002', 16)
ADS_EVENT_GAIN_CHANGED    =              int( '90011003', 16)
ADS_EVENT_AUTOSET_DONE    =              int( '90011004', 16)
#/** This is the calibration mode offset, calculated with all
#the inputs shorted. The dynamic offset is sent via DAC8_EVENT_OFFSET_CHANGED.
#*/
ADS_EVENT_OFFSET_CHANGED  =              int( '90011005', 16)
ADS_EVENT_ZCHECK_ON       =              int( '90011006', 16)
ADS_EVENT_ZCHECK_OFF      =              int( '90011007', 16)
ADS_EVENT_ZCHECK_VALUES   =              int( '90011008', 16)
#
#//** This code is useful for software playback to separate recordings in the same data file
ADS_EVENT_STOP_REC        =              int( '90011009', 16)
ADS_EVENT_START_REC       =              int( '90011010', 16)
#
#/*This code is used for software playback to identify classification events in the same data file */
ADS_EVENT_CLASSIFICATION  =              int( '9001100A', 16)
##endif
#
#/******************************************************************************
#* EEPROM Function Call Codes.
#*
#*******************************************************************************/
#/**
#Resets the EEPROM configuration to defaults.
#1. Function Code: 		EEPROM_RESET_TO_DEFAULTS
#2. Message Length: 		1
#3. Reset defaults		integer values { any: the value is ignored. }.
#*/
EEPROM_RESET_TO_DEFAULTS  =              int( '00030001', 16)
#
#/**
#	Write the APM serial number to EEPROM.
#	1. Function Code: 		EEPROM_SET_SERIAL_NUMBER
#	2. Message Length: 		1
#	3. Serial number		integer values { positive integer }.
#*/
EEPROM_SET_SERIAL_NUMBER  =              int( '00030002', 16)
#
#/**
#Write IP configuration to EEPROM.
#Command contents:
#1. Function Code: 		EEPROM_SET_IP
#2. Message Length: 		10
#3. Config Number:		integer values { 0 - 3 }.
#						The index of the IP configuration in EEPROM memory (see CPM EEPROM map).
#
#4. IP address			integer values {valid IPv4 address}
#5. MAC address			integer x 2 8 bytes - only 6 are used:
#						first word (4 bytes) and the 2 most significant bytes of the second word.
#6. Subnet address		integer values {valid IPv4 subnet address}
#7. Gateway address		integer values {valid IPv4 address}
#8. DHCP_ON				boolean values { 0,1 }. 1 - DHCP is on (Not supported for now).
#9. DNS address			integer values {valid IPv4 address}
#10. Destination IP address	integer values {valid IPv4 address}
#11. Port number			integer values { 0 - 65535 }
#*/
EEPROM_SET_IP             =              int( '00030003', 16)
#
#/** Not used. */
EEPROM_ERASE_ALL          =              int( '00030004', 16)
#
#/** Not used. */
EEPROM_GET_CONTENTS       =              int( '00030005', 16)
#
#/// @cond DO_NOT_DOCUMENT
#/******************************************************************************
#* EQ SigmaDSP Function Call Codes.
#*
#*******************************************************************************/
EQ_DSP_RESET              =              int( '000D0001', 16)
EQ_DSP_SET_PARAM          =              int( '000D0002', 16)
EQ_DSP_UPDATE             =              int( '000D0003', 16)
EQ_DSP_UNMUTE_DAC         =              int( '000D0004', 16)
EQ_DSP_BYPASS             =              int( '000D0005', 16)
#/// @endcond
#
#/******************************************************************************
#* AD1938 Audio Codec Function Call Codes.
#*
#*******************************************************************************/
#/**Set a CODEC channel volume.
#Command contents:
#1. Function Code: AUDIO_SET_VOLUME
#2. Message Length: 2
#3. Channel number: integer values { 0-7 }
#4. Volume: integer values {0-10000}
#*/
AUDIO_SET_VOLUME          =              int( '000E0001', 16)
#
#/**Increase a CODEC channel's volume (increment by one step).
#Command contents:
#1. Function Code: AUDIO_INCREASE_VOLUME
#2. Message Length: 1
#3. Channel number: integer values { 0-7 }
#*/
AUDIO_INCREASE_VOLUME     =              int( '000E0002', 16)
#
#/**Decrease a CODEC channel's volume (increment by one step).
#Command contents:
#1. Function Code: AUDIO_DECREASE_VOLUME
#2. Message Length: 1
#3. Channel number: integer values { 0-7 }
#*/
AUDIO_DECREASE_VOLUME     =              int( '000E0003', 16)
#
#/**Mutes or un-mutes a CODEC channel.
#Command contents:
#1. Function Code: AUDIO_MUTE_CHANNEL
#2. Message Length: 2
#3. Channel number: integer values { 0-7 }
#4. Mute: integer 0 - un-mute 1 - mute.
#*/
AUDIO_MUTE_CHANNEL        =              int( '000E0004', 16)
#
#/**Mutes or un-mutes all CODEC channels.
#Command contents:
#1. Function Code: AUDIO_MUTE_CHANNEL
#2. Message Length: 1
#3. Mute: integer 0 - un-mute 1 - mute.
#*/
AUDIO_MUTE_CHANNEL_ALL    =              int( '000E0005', 16)
#
#/**Enables an on-board audio amplifier. Deprecated and no longer used.
#Command contents:
#1. Function Code: AUDIO_ENABLE
#2. Message Length: 1
#3. Enable: integer 0 - disable 1 - enable.
#4. Toggle audio ON: 0 - do not toggle, 1 - toggle. This is used
#to toggle the APM1_AUDIO_ON line. Only APM1 is required to toggle
#the AUDIO_ON line. APM2 must keep it at logic level high.
#*/
AUDIO_ENABLE              =              int( '000E0006', 16)
#
#/**Sets the active analog input channel map for the Sync Interface.
#Command contents:
#1. Function Code: SYNC_INT_INPUT_CHANNEL_MAP
#2. Message Length: 1
#3. Channel map: integer Channel numbering starts from the least significant bit
#towards the MSB. A value of 1 in the corresponding bit denotes an active channel
#and a value of zero, an inactive channel.
#For eight channels, the map is:
#-----------------------------------------
#|B7  |B6  |B5  |B4  |B3  |B2  |B1  |B0  |
#|CH8 |CH7 |CH6 |CH5 |CH4 |CH3 |CH2 |CH1 |
#-----------------------------------------
#Only two channels are used for the Sync Interface analog input section, so only
#bits B0 and B1 will be set.
#*/
SYNC_INT_INPUT_CHANNEL_MAP =              int( '000E0007', 16)
#
#/**
#Sets the Sync Interface analog inputs sample rate.
#Command contents:
#1. Function Code: 		AUDIO_SET_SAMPLE_RATE
#2. Message Length: 		1
#3. Values:				integer values { 32000, 16000, 8000, 4000, 2000, 1000 }
#*/
AUDIO_SET_SAMPLE_RATE     =              int( '000E0008', 16)
#
#/**Sets the polarity switches on the Sync Interface for the specified channel.
#Command contents:
#1. Function Code: SYNC_INT_SET_INPUT_POLARITY
#2. Message Length: 2
#3. Channel Number: integer {0,1}. Only two analog inputs on the Sync Interface.
#4. Polarity: integer values { 0 - Unipolar 1 - Bipolar }
#*/
SYNC_INT_SET_INPUT_POLARITY =              int( '00500001', 16)
#
#/**Sets the input gain switches on the Sync Interface for the specified channel.
#Command contents:
#1. Function Code: SYNC_INT_SET_INPUT_GAIN
#2. Message Length: 2
#3. Channel Number: integer {0,1}. Only two analog inputs on the Sync Interface.
#4. Input gain: integer values { 0 - x10 1 - x100}
#*/
SYNC_INT_SET_INPUT_GAIN   =              int( '00500002', 16)
#
#/**Sets the input coupling switches on the Sync Interface for the specified channel.
#Command contents:
#1. Function Code: SYNC_INT_SET_INPUT_COUPLING
#2. Message Length: 2
#3. Channel Number: integer {0,1}. Only two analog inputs on the Sync Interface.
#4. Input coupling: integer values { 0 - AC 1 - DC}
#*/
SYNC_INT_SET_INPUT_COUPLING =              int( '00500003', 16)
#
#/**Sets the input divider switches on the Sync Interface for the specified channel.
#Command contents:
#1. Function Code: SYNC_INT_SET_INPUT_DIV
#2. Message Length: 2
#3. Channel Number: integer {0,1}. Only two analog inputs on the Sync Interface.
#4. Input divider: integer values { 0 - divide by 3  1 - divide by 6}.
#*/
SYNC_INT_SET_INPUT_DIV    =              int( '00500004', 16)
#
#/**Sets the digital output channel values for the Sync Interface.
#Command contents:
#1. Function Code: SYNC_INT_SET_BOB_OUTPUTS
#2. Message Length: 1
#3. Output values: integer Channel numbering starts from the least significant bit
#towards the MSB. A value of 1 in the corresponding bit denotes a logic level high
#and a value of zero a logic level zero.
#For eight channels, the map is:
#-----------------------------------------
#|B7  |B6  |B5  |B4  |B3  |B2  |B1  |B0  |
#|CH8 |CH7 |CH6 |CH5 |CH4 |CH3 |CH2 |CH1 |
#-----------------------------------------
#*/
SYNC_INT_SET_BOB_OUTPUTS  =              int( '00500005', 16)
#
#/**
#Sends an event containing the Sync Interface connectivity status.
#Command contents:
#1. Function Code: 		SYNC_INT_EVENT_BOB_PRESENT
#2. Message Length: 		1
#3. Is Connected:		integer values { 0 - not connected 1 - connected }
#*/
SYNC_INT_EVENT_BOB_PRESENT =              int( '900E0001', 16)
#
#/**
#Sends breakout box input ports values to the uplink.
#Command contents:
#1. Event Code: 		SYNC_INT_EVENT_DIG_INPUT
#2. Message Length: 		5
#3. Values:
#	3.1. Device Identifier.
#	3.2. Timestamp (ADC timestamp).
#	3.3. Port 0 state.
#	3.4. Port 1 state (these values should be ignored if the port is configured as output - default).
#	3.5. Port 5 state (the input available on the box).
#*/
SYNC_INT_EVENT_DIG_INPUT  =              int( '900E0002', 16)
#
#/** Sends breakout box voltage calibration for the specified channel.
#	This message is used by the PC software to transfer this value to
#	external TCP clients, it is not sent by the firmware.
#Event contents:
#1. Event Code: SYNC_INT_EVENT_VOLTAGE_CALIBRATION
#2. Message Length: 3
#3. Channel Number: integer values { 1 or 2 }
#4. Device Identifier: integer values { 1 .. }
#5. Voltage Calibration: Calibration value used to convert ADC samples into micro-volts.
#*/
SYNC_INT_EVENT_VOLTAGE_CALIBRATION =              int( '900E0003', 16)
#
#/**
#Sends breakout box input ports values to the uplink.
#Command contents:
#1. Event Code: 		SYNC_INT_EVENT_REALTIME_DIG_INPUT
#2. Message Length: 		N
#3. Values:
#3.1. Device Id.
#3.2. Timestamps (ADS1298 timestamps). A sequence of timestamps marking a level change
#in the digital input.
#*/
SYNC_INT_EVENT_REALTIME_DIG_INPUT =              int( '900E0004', 16)
#
#/**
#Sends breakout box input ports values to the uplink.
#Command contents:
#1. Event Code: 		SYNC_INT_EVENT_SAMPLING_RATE
#2. Message Length: 		1
#3. Values: integer values { 8000, 4000, 2000, 1000 }
#in the digital input.
#*/
SYNC_INT_EVENT_SAMPLING_RATE =              int( '900E0005', 16)
#
#/**@ brief Sync Interface analog input data code.
#1. Message code: SYNC_INT_INPUT_DATA
#2. Message length: (2 + nChannels * nSamplesPerChannel)
#3. Active channels bitmap
#4. Timestamp (unsigned int)
#5. N channels of M samples each.
#Please see the eRPC protocol documentation for more information on
#the data code message format.
#*/
SYNC_INT_INPUT_DATA       =              int( '300E0001', 16)
#
#/// @cond DO_NOT_DOCUMENT
#/** @private
#*/
CPM_RESET                 =              int( '00040001', 16)
#/** @private
#*/
CPM_SW_RESET              =              int( '00040002', 16)
#/** @private
#*/
CPM_ENABLE_CODEC          =              int( '00040003', 16)
#/// @endcond
#
#/** Configure the CDCE906 PLL using init_PLL_clock_synthesizer defined in system_ctrl.h.
#	1. Function Code: 	CPM_INIT_PLL
#	2. Message Length: 		1
#	3. Set PLL: 			integer values {1}. Value is ignored.
#
#*/
CPM_INIT_PLL              =              int( '00040004', 16)
#
#/** Sends APM-03 board information.
#Event contents:
#1. Event Code: CPM_EVENT_INFO
#2. Message Length: 6
#3. Device information:
#g_cpm_info.device_id
#g_cpm_info.firmware_id
#g_cpm_info.firmware_version
#g_cpm_info.serial_number
#g_cpm_info.eeprom_test_ok
#g_cpm_info.sram_test_ok
#
#*/
CPM_EVENT_INFO            =              int( '90041001', 16)
#
#/** Sends APM-03 temperature from ADM1032.
#Event contents:
#1. Event Code: CPM_EVENT_TEMP_VALUE
#2. Message Length: 1
#3. Temperature value
#*/
CPM_EVENT_TEMP_VALUE      =              int( '90041002', 16)
#
#/******************************************************************************
#* Stim data code.
#*******************************************************************************/
STIM_DATA_CONTINUOUS      =              int( '30050001', 16)
#
#/******************************************************************************
#* STIMULATOR function codes
#*
#*******************************************************************************/
#/** Enable stimulation. For security purposes, this function is not used.
#Command contents:
#	1. Function Code: 	STIM_START
#	2. Message Length: 		1
#	3. Stim_Start: 		boolen {
#						false: set stimulation mode to #MODE_STIM_NONE.
#						true: initialize stimulation parameters and buffers.
#						}
#*/
STIM_START                =              int( '00050001', 16)
#
#/** Set stimulation or impedance measurement type (range): Micro/ macro stimulation/ ZCheck.
#Command contents:
#	1. Function Code: 		STIM_SET_TYPE
#	2. Message Length: 		1
#	3. Stimulation type:	integer
#							values: { 0 - microstimulation,
#									  1 - macrostimulation,
#									  2 - micro - impedance check,
#									  3 - macro - impedance check
#									  }
#*/
STIM_SET_TYPE             =              int( '00050002', 16)
#
#/** Set stimulation frequency.
#Command contents:
#	1. Function Code: 		STIM_SET_FREQUENCY
#	2. Message Length: 		2
#	3. Output channel: 		integer values { 0 - 7 }
#	4. Stim frequency: 		integer
#							values: { 1 - 300 Hz }
#*/
STIM_SET_FREQUENCY        =              int( '00050003', 16)
#
#/** Set pulse amplitude for the specified channel and train.
#Command contents:
#	1. Function Code: 		STIM_SET_AMPLITUDE
#	2. Message Length: 		2
#	2. Output channel: 		integer values { 0 - 7 }
#	3. Stim amplitude: 		float values: { 0 - 1}.
#							The amplitude value is a percent of the output scale.
#	4. Train index			integer values {0 - #STIM_NUM_MAX_TRAINS}
#*/
STIM_SET_AMPLITUDE        =              int( '00050004', 16)
#
#/** Set pulse duration.
#Command contents:
#	1. Function Code: 		STIM_SET_DURATION
#	2. Message Length: 		3
#	2. Output channel: 		integer values { 0 - 7 }
#	3. Pulse duration: 		unsigned int values: { [0 - (3000/1e6) * sampling_rate] - ADC ticks}
#*/
STIM_SET_DURATION         =              int( '00050005', 16)
#
#/** Set pulse phase.
#Command contents:
#	1. Function Code: 		STIM_SET_PHASE
#	2. Message Length: 		2
#	2. Output channel: 		integer values { 0 - 7 }
#	3. Pulse phase: 		unsigned int values: { 0 - monophasic, 1 - biphasic }
#*/
STIM_SET_PHASE            =              int( '00050006', 16)
#
#/** Set pulse polarity.
#Command contents:
#	1. Function Code: 		STIM_SET_POLARITY
#	2. Message Length: 		2
#	2. Output channel: 		integer values { 0 - 7 }
#	3. Pulse phase: 		unsigned int values: { 0 - negative, 1 - positive}
#*/
STIM_SET_POLARITY         =              int( '00050007', 16)
#
#/** Set output channels.
#Command contents:
#1. Function Code: 		STIM_SET_OUTPUT_CHANNELS
#2. Message Length: 		2
#2. Output channel bank: integer values { >= 0 }.
#	Remark: The channel bank is a means of future extension of the number of channels
#	to greater than 32.
#3. Output channel bit-map: 	unsigned int
#	Configure the active channels by setting a corresponding bit in the channel bank.
#	The default is to use bank 0 and channels 0-7, specified in the least significant
#	bits of this word.
#*/
STIM_SET_OUTPUT_CHANNELS  =              int( '00050008', 16)
#
#/** Set return channels.
#Command contents:
#1. Function Code: 		STIM_SET_RETURN_CHANNELS
#2. Message Length: 		2
#2. Output channel bank: integer values { >= 0 }.
#Remark: The channel bank is a means of future extension of the number of channels
#to greater than 32.
#3. Output channel bit-map: 	unsigned int
#Configure the return channels by setting a corresponding bit in the channel bank.
#The default is to use bank 0 and channels 0-7, specified in the least significant
#bits of this word.
#NOTE!!! There must be a collision detection method to prevent return channels being
#also configured as output channels.
#*/
STIM_SET_RETURN_CHANNELS  =              int( '00050009', 16)
#
#/** Set train duration in DAC ticks.
#Command contents:
#1. Function Code: 		STIM_SET_TRAIN_DURATION
#2. Message Length: 		2
#2. Output channel: 		integer values { 0 - 7 }
#3. Train duration: 		unsigned int values: { [ -1 - (max uint -1 )] -> ADC ticks}
#*/
STIM_SET_TRAIN_DURATION   =              int( '0005000A', 16)
#
#/** Set train duration in DAC ticks.
#Command contents:
#1. Function Code: 		STIM_SET_PULSE_DELAY
#2. Message Length: 		2
#2. Output channel: 		integer values { 0 - 7 }
#3. Pulse delay: 		unsigned int values: { [ 0 - (max uint -1 )] -> ADC ticks}
#*/
STIM_SET_PULSE_DELAY      =              int( '0005000B', 16)
#
#/** Starts or stops impedance measurement.
#Command contents:
#1. Function Code: 		STIM_START_ZCHECK
#2. Message Length: 		1
#3. Start ZCheck: 		integer values { 1 - starts zcheck, 0 - halts zcheck. }
#
#ZCheck will behave like fixed duration stimulation and will depend on the
#train durations configured for each channel prior to initiating measurement.
#*/
STIM_START_ZCHECK         =              int( '0005000C', 16)
#
#/** Configures impedance measurement parameters.
#Command contents:
#1. Function Code: 		STIM_CONFIG_ZCHECK
#2. Message Length: 		3
#3. Duration: 		float values { 1 - 10 } in seconds
#4. Frequency:		integer values { 100 - 5000 } in Hertz.
#5. Measuring cycles:integer values {1 - 10}.
#6. Send Waveforms:  true - send measurement waveforms to uplink otherwise false.
#*/
STIM_CONFIG_ZCHECK        =              int( '0005000D', 16)
#
#/** The remote controller input is only being read while in stimulation mode.
#	This function call configures APM_SYNC_0 to instruct the mTController to read or
#	ignore the remote input.
#	Both APMs assigned to HMS devices are required to call this function, otherwise
#	the logic level of the digital output that they both share will remain in
#	logic level high and the mTC will continue to respond to remote input during stimulation.
#Command contents:
#1. Function Code: 		STIM_SET_REMOTE_READBACK
#2. Message Length: 		1
#3. Enable: 			boolean values { 0 - disable readback, 1 - enable readback}.
#*/
STIM_SET_REMOTE_READBACK  =              int( '0005000E', 16)
#
#/** Initiates stimulation self test.
#Command contents:
#1. Function Code: 		STIM__SELF_TEST
#2. Message Length: 		1
#3. Mode: 			integer values { 0 - MODE_MICRO, 1 - MODE_MACRO}.
#					See dac_stim.h for the respective modes definitions.
#*/
STIM_SELF_TEST            =              int( '0005000F', 16)
#
#/** Sets the stimulation output for custom stimulation.
#Command contents:
#1. Function Code: 		STIM_SET_CUSTOM_OUTPUT
#2. Message Length: 		sizeof(output_t)
#3. Output: 			An output_t (see dac_stim.h) structure.
#*/
STIM_SET_CUSTOM_OUTPUT    =              int( '00050010', 16)
#
#/** Configures the stimulator to accept an externally provided trigger
#to initiate stimulation at the expense of the remote Activate button.
#Command contents:
#1. Function Code: 		STIM_SET_EXTERNAL_TRIGGER
#2. Message Length: 		1
#3. Value: 			integer values {0 - disable 1- enable}.
#*/
STIM_SET_EXTERNAL_TRIGGER =              int( '00050011', 16)
#
#/** Sets the DC-offset detection threshold, in ADS levels, at gain x1.
#Command contents:
#1. Function Code: 		STIM_SET_DC_THRESHOLD
#2. Message Length: 		1
#3. Value: 			integer values {0 - 2^23-1}.
#*/
STIM_SET_DC_THRESHOLD     =              int( '00050012', 16)
#
#/** Sets the remote active button led.
#Command contents:
#1. Function Code: 		STIM_SET_ACTIVE_BUTTON
#2. Message Length: 		1
#3. Value: 			integer values {0, 1}.
#*/
STIM_SET_ACTIVE_BUTTON    =              int( '00050013', 16)
#
#/** Sets the Internal MTC connection state
#Command contents:
#1. Function Code: 		STIM_SET_MTC_CONNECTED
#2. Message Length: 		1
#3. Value: 			integer values {0, 1}.
#*/
STIM_SET_MTC_CONNECTED    =              int( '00050014', 16)
#
#/** Sets the stim offset compensation on/off
#Command contents:
#1. Function Code: 		STIM_SET_OFFSET_COMPENSATION
#2. Message Length: 		1
#3. Value: 			integer values {0 - disable, 1 - enable}.
#*/
STIM_SET_OFFSET_COMPENSATION =              int( '00050015', 16)
#
#/** Sets the ground stimulation output mode
#Command contents:
#1. Function Code: 		STIM_SET_GND_STIM_OUT_MODE
#2. Message Length: 		1
#3. Value: 			integer values {0, 1}.
#*/
STIM_SET_GND_STIM_MULTICHANNEL_MODE =              int( '00050016', 16)
#
#/** Sets the ZCheck DC Offset threshold value.
#Command contents:
#1. Function Code: 		STIM_SET_ZCHECK_DC_OFFSET_THRESHOLD
#2. Message Length: 		1
#3. Value: 			integer values {0 - 2^23-1}.
#*/
STIM_SET_ZCHECK_DC_OFFSET_THRESHOLD =              int( '00050017', 16)
#
#/** Stimulation on timestamp.
#Contents:
#	1. Function Code: 		STIM_EVENT_STIM_ON
#	2. Message Length: 		2
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Stimulation on timestamp: unsigned integer.
#*/
STIM_EVENT_STIM_ON        =              int( '90051001', 16)
#
#/** Stimulation off timestamp.
#Contents:
#	1. Function Code: 		STIM_EVENT_STIM_OFF
#	2. Message Length: 		2
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Stim on timestamp: unsigned integer
#*/
STIM_EVENT_STIM_OFF       =              int( '90051002', 16)
#///@cond DO_NOT_DOCUMENT
#/** Unused with GL5K. */
STIM_EVENT_POST_OFF       =              int( '90051003', 16)
#
#/** Unused with GL5K. */
STIM_EVENT_PRE_ON         =              int( '90051004', 16)
#/// @endcond
#
#/** Report the impedance measurement waveform.
#Event contents:
#1. Event Code: 		STIM_EVENT_ZCHECK_WAVE
#2. Message Length: 		1 + N (channel number field + number of waveform samples).
#3. Channel Number : integer values { 0 to 7}. Number of the measured channel.
#4. Impedance measurement waveform. The waveform may be of variable length,
#depending on the measurement frequency.
#*/
STIM_EVENT_ZCHECK_WAVE    =              int( '90051005', 16)
#
#/**
#Reports the impedance values.
#Event contents:
#1. Event Code: 		STIM_EVENT_IMPEDANCE
#2. Message Length: 	5.
#3. Channel Number : integer values { 0 to 7}. Number of the measured channel.
#4. Impedance: float. The value of the complex impedance, in Ohms.
#5. Resistance: float. The resistive component of the impedance, in Ohms.
#6. Capacitance: float. The capacitive component of the impednace, in Ohms.
#7. Phase: float. The phase delay introduced by the capacitive component, in Ohms.
#*/
STIM_EVENT_IMPEDANCE      =              int( '90051006', 16)
#
#/**
#Reports the remote controller forward button press.
#1. Event Code: 		STIM_EVENT_REMOTE_FWD
#2. Message Length: 	1.
#3. Speed : integer values { 0, 1 .. }.
#*/
STIM_EVENT_REMOTE_FWD     =              int( '90051007', 16)
#
#/**
#Reports the remote controller reverse button press.
#1. Event Code: 		STIM_EVENT_REMOTE_REV
#2. Message Length: 	1.
#3. Speed : integer values { 0, 1 .. }.
#*/
STIM_EVENT_REMOTE_REV     =              int( '90051008', 16)
#
#/**
#Reports the remote controller speed selection.
#1. Event Code: 		STIM_EVENT_REMOTE_SPEED_SELECTION
#2. Message Length: 	1.
#3. Speed : integer values { 0, 1 .. }.
#*/
STIM_EVENT_REMOTE_SPEED_SELECTION =              int( '90051009', 16)
#
#/** Report stimulation type (range): Micro/ macro stimulation.
#Command contents:
#	1. Function Code: 		STIM_EVENT_STIM_TYPE
#	2. Message Length: 		2
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Stimulation type:	integer
#							values: { 0 - microstimulation,
#							1 - macrostimulation }
#*/
STIM_EVENT_STIM_TYPE      =              int( '9005100B', 16)
#
#/** Report stimulation frequency.
#Command contents:
#	1. Function Code: 		STIM_EVENT_PULSE_FREQUENCY
#	2. Message Length: 		3
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Output channel: 		integer values { 0 - 7 }
#	5. Stim frequency: 		integer
#							values: { 1 - 300 Hz }
#*/
STIM_EVENT_PULSE_FREQUENCY =              int( '9005100C', 16)
#
#/** Report pulse amplitude.
#	Command contents:
#	1. Function Code: 		STIM_EVENT_PULSE_AMPLITUDE
#	2. Message Length: 		3
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Output channel: 		integer values { 0 - 7 }
#	5. Stim amplitude: 		float values: { 0 - 1}.
#	The amplitude value is a percent of the output scale.
#*/
STIM_EVENT_PULSE_AMPLITUDE =              int( '9005100D', 16)
#
#/** Report pulse duration.
#Command contents:
#	1. Function Code: 		STIM_EVENT_PULSE_DURATION
#	2. Message Length: 		3
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Output channel: 		integer values { 0 - 7 }
#	5. Pulse duration: 		unsigned int values: { [0 - (3000/1e6) * sampling_rate] - ADC ticks}
#*/
STIM_EVENT_PULSE_DURATION =              int( '9005100E', 16)
#
#/** Report pulse phase.
#Command contents:
#	1. Function Code: 		STIM_EVENT_PULSE_PHASE
#	2. Message Length: 		3
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Output channel: 		integer values { 0 - 7 }
#	5. Pulse phase: 		unsigned int values: { 0 - monophasic, 1 - biphasic }
#*/
STIM_EVENT_PULSE_PHASE    =              int( '9005100F', 16)
#
#/** Report pulse polarity.
#Command contents:
#	1. Function Code: 		STIM_EVENT_PULSE_POLARITY
#	2. Message Length: 		3
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Output channel: 		integer values { 0 - 7 }
#	5. Pulse phase: 		unsigned int values: { 0 - negative, 1 - positive}
#*/
STIM_EVENT_PULSE_POLARITY =              int( '90051010', 16)
#
#/** Reports the stimulator operating mode
#	1. Function Code: STIM_EVENT_OPERATING_MODE
#	2. Message Length:	3
#	3. Device Identifier: integer values { 0, 1 .. }
#	4. Operating Mode: unsigned int values { 0 - Constant Current, 1 - Constant Voltage }
#*/
STIM_EVENT_OPERATING_MODE =              int( '90051011', 16)
#
#/** Report output channels.
#Command contents:
#	1. Function Code: 		STIM_EVENT_PULSE_OUTPUT_CHANNELS
#	2. Message Length: 		3
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Output channel bank: integer values { >= 0 }.
#	Remark: The channel bank is a means of future extension of the number of channels
#	to greater than 32.
#	5. Output channel bit-map: 	unsigned int
#	Configure the active channels by setting a corresponding bit in the channel bank.
#	The default is to use bank 0 and channels 0-7, specified in the least significant
#	bits of this word.
#*/
STIM_EVENT_OUTPUT_CHANNELS =              int( '90051020', 16)
#
#/** Report return channels.
#Command contents:
#	1. Function Code: 		STIM_EVENT_PULSE_RETURN_CHANNELS
#	2. Message Length: 		3
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Output channel bank: integer values { >= 0 }.
#	Remark: The channel bank is a means of future extension of the number of channels
#	to greater than 32.
#	5. Output channel bit-map: 	unsigned int
#	Configure the return channels by setting a corresponding bit in the channel bank.
#	The default is to use bank 0 and channels 0-7, specified in the least significant
#	bits of this word.
#	NOTE!!! There must be a collision detection method to prevent return channels being
#	also configured as output channels.
#*/
STIM_EVENT_RETURN_CHANNELS =              int( '90051030', 16)
#
#/** Report train duration in ADS ticks.
#Command contents:
#	1. Function Code: 		STIM_EVENT_TRAIN_DURATION
#	2. Message Length: 		3
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Output channel: 		integer values { 0 - 7 }
#	5. Train duration: 		unsigned int values: { [ 0 - (max uint -1 )] -> ADC ticks}
#*/
STIM_EVENT_TRAIN_DURATION =              int( '90051040', 16)
#
#/** Report train duration in ADS ticks.
#Command contents:
#	1. Function Code: 		STIM_EVENT_PULSE_DELAY
#	2. Message Length: 		3
#	3. Device Identifier : integer values { 0, 1 .. }
#	4. Output channel: 		integer values { 0 - 7 }
#	5. Pulse delay: 		unsigned int values: { [ 0 - (max uint -1 )] -> ADC ticks}
#*/
STIM_EVENT_PULSE_DELAY    =              int( '90051050', 16)
#
#/** Report stimulation output error.
#Command contents:
#1. Function Code: 		STIM_EVENT_OUTPUT_ERROR
#2. Message Length: 		3
#3. Device Identifier:	integer values { 0, 1 .. }
#4. Output channel: 		integer values { 0 - 7 }
#5. Pulse duration: 		unsigned int values: { [ 0 - (max uint -1 )] -> ADC ticks}
#*/
STIM_EVENT_OUTPUT_ERROR   =              int( '90051060', 16)
#
#/** Reports custom waveform Id
#Command contents:
#1. Function Code: 		STIM_EVENT_CUSTOM_WAVEFORM
#2. Message Length: 		1
#3. Identifier : unsigned int
#*/
STIM_EVENT_CUSTOM_WAVEFORM =              int( '90051070', 16)
#
#
#/******************************************************************************
#* UPGRADE function codes
#*
#*******************************************************************************/
#/** Initiates the Flash memory upgrade process.
#Command contents:
#1. Function code: FLASH_UPGRADE
#2. Message length: 1
#3. Firmware Length: integer Represents the length of the firmware file, in bytes.
#*/
FLASH_UPGRADE             =              int( '00060001', 16)
#
#/** Sends a write message. The firmware .ldr file is parsed and split into
#chunks that are sequentially sent to the Flash module via this message.
#Command contents:
#1. Function code: FLASH_WRITE_DATA
#2. Message length: integer maximum: FLASH_DATA_CHUNK_SIZE
#3. Firmware data: integer firmware data to write to flash memory.
#*/
FLASH_WRITE_DATA          =              int( '00060002', 16)
#
#/**
#Sends a command to erase the full contents of the flash.
#Note: the failsafe flash region is not deleted by this command.
#Command contents:
#1. Function code: FLASH_ERASE_FULL
#2. Message length: 1.
#3. Message data: 0. The actual value is ignored.
#*/
FLASH_ERASE_FULL          =              int( '00060003', 16)
#
#/**
#Sends a command to erase the contents of the flash that will be written
#to during the upgrade.
#Note: the failsafe flash region is not deleted by this command.
#Command contents:
#1. Function code: FLASH_ERASE_AFFECTED
#2. Message length: 1.
#3. Message data: 0. The actual value is ignored.
#*/
FLASH_ERASE_AFFECTED      =              int( '00060004', 16)
#
#/// @cond DO_NOT_DOCUMENT
DAC8_SET_OUTPUT           =              int( '00080001', 16)
DAC8_EVENT_OFFSET_CHANGED =              int( '90081001', 16)
#
FILTER_SET_PARAMETERS     =              int( '00090001', 16)
FILTER_ENABLE             =              int( '00090002', 16)
#/// @endcond
#
#/******************************************************************************
#* Knob message codes.
#*
#*******************************************************************************/
#
KNOB_EVENT_LEFT           =              int( '900A1001', 16)
KNOB_EVENT_RIGHT          =              int( '900A1002', 16)
KNOB_EVENT_PUSH           =              int( '900A1003', 16)
#
#/******************************************************************************
#* Flash message codes.
#*
#*******************************************************************************/
#/**
#The event generated after the flash had been erased.
#Event contents:
#1. Event Code: 			FLASH_EVT_DONE_ERASE
#2. Message Length: 		1
#3. Return Code: Error code returned by the erase function. NO_ERR for success.
#*/
FLASH_EVT_DONE_ERASE      =              int( '90061001', 16)
#
#/**
#The event generated if there is an error during the erase process.
#Event contents:
#1. Event Code: 			FLASH_EVT_ERROR_ERASE
#2. Message Length: 		1
#3. Return Code: Error code returned by the erase function.
#*/
FLASH_EVT_ERROR_ERASE     =              int( '90061002', 16)
#
#/**
#The event generated if there is an error during the write process.
#Event contents:
#1. Event Code: 			FLASH_EVT_ERROR_WRITE
#2. Message Length: 		1
#3. Return Code: Error code returned by the erase function.
#*/
FLASH_EVT_ERROR_WRITE     =              int( '90061003', 16)
#
#/**
#The event generated when the current data chunk has been written and the driver
#can handle new data.
#Event contents:
#1. Event Code: 			FLASH_EVT_SEND_NEXT
#2. Message Length: 		1
#3. Contents: 1 this value is ignored.
#*/
FLASH_EVT_SEND_NEXT       =              int( '90061004', 16)
#
#/// @cond DO_NOT_DOCUMENT
#/**
#Not used.
#The event generated after the upgrade process is finished.
#Event contents:
#1. Event Code: 			FLASH_EVT_DONE_UPGRADING
#2. Message Length: 		1
#3. Contents: 1 this value is ignored.
#*/
FLASH_EVT_DONE_UPGRADING  =              int( '90061005', 16)
#
#/******************************************************************************
#* Temperature function codes
#*
#*******************************************************************************/
#
TEMP_EVENT_MON            =              int( '90011008', 16)
#
#/** Report the temperature measured on the APM board.
#Event contents:
#1. EventCode: 			CPM_TEMP_EVENT_LOCAL
#2. Message Length: 		1
#3. Temperature: 		integer values { temperature in degrees Celsius }.
#}*/
#
CPM_TEMP_EVENT_LOCAL      =              int( '9004100A', 16)
#
#/** Report the temperature measured at the DSP.
#Event contents:
#1. EventCode: 			CPM_TEMP_EVENT_REMOTE
#2. Message Length: 		1
#3. Temperature: 		integer values { temperature in degrees Celsius }.
#}*/
CPM_TEMP_EVENT_REMOTE     =              int( '9004100B', 16)
#
#/** Report temperature to remote host.
#Command contents:
#1. Function Code: 		GET_CPM_SENSOR_TEMP
#2. Message Length: 		1
#3. Temperature type: 	integer values { 1 - local temperature (see #, CPM_TEMP_EVENT_LOCAL)
#										  0 - remote temperature (see #, CPM_TEMP_EVENT_REMOTE)}
#}
#*/
GET_CPM_SENSOR_TEMP       =              int( '0010000E', 16)
#/// @endcond
#
#/*HMS function codes */
#
#/** Start or stop recording.
#Command contents:
#1. Function Code: 		HMS_START_RECORDING
#2. Message Length: 		1
#3. Start recording: 	integer values { 0 - stop recording, 1 - start recording }
#}
#*/
HMS_START_RECORDING       =              int( '00200001', 16)
#
#/** Set data acquisition sampling rate.
#Command contents:
#1. Function Code: 		HMS_SET_SAMPLING_RATE
#2. Message Length: 		2
#3. ADS ID: 				integer values { HMS_ADS1298_ID, HMS_ADS1299_ID }
#4. Sampling rate: 		integer values:
#	{ Specific to the ADS, in units of Hz:
#	4.1. For ADS1298 valid values are: 500, 1000, 2000, 4000, 8000, 16000, 32000
#	4.2. For ADS1299 valid values are: 250, 500, 1000, 2000, 4000, 8000, 16000
#	}
#*/
HMS_SET_SAMPLING_RATE     =              int( '00200002', 16)
#
#/** Set channel GAIN for all acquisition channels of a certain type (MER or EEG/LFP).
#	Command contents:
#	1. Function Code: 		HMS_SET_GAIN_ALL
#	2. Message Length: 		2
#	3. ADS ID: 				integer values { HMS_ADS1298_ID, HMS_ADS1299_ID }
#	4. Gain value: 			integer values:
#	{ Specific to the ADS:
#	4.1. For ADS1298 valid values are: 1, 2, 4, 6, 8, 12
#	4.2. For ADS1299 valid values are: 1, 2, 4, 8, 12, 24
#	}
#*/
HMS_SET_GAIN_ALL          =              int( '00200003', 16)
#
#/** Set channel GAIN for all acquisition channels of a certain type (MER or EEG/LFP).
#Command contents:
#1. Function Code: 		HMS_SET_GAIN
#2. Message Length: 		3
#3. ADS ID: 				integer values { HMS_ADS1298_ID, HMS_ADS1299_ID }
#4. Channel number:		integer values { 0 - 7 }
#5. Gain value: 			integer values:
#	{ Specific to the ADS:
#	5.1. For ADS1298 valid values are: 1, 2, 4, 6, 8, 12
#	5.2. For ADS1299 valid values are: 1, 2, 4, 8, 12, 24
#	}
#*/
HMS_SET_GAIN              =              int( '00200004', 16)
#
#/** Set ADS active channels.
#Command contents:
#1. Function Code: 		HMS_SET_ACTIVE_CHANNELS
#2. Message Length: 		2
#3. ADS ID: 				integer values { HMS_ADS1298_ID, HMS_ADS1299_ID }
#4. Channel map: 		unsigned int Value:
#	Active channel map. Channel numbering starts from the least significant bit
#	towards the MSB. A value of 1 in the corresponding bit denotes an active channel
#	and a value of zero, an inactive channel.
#	For eight channels, the map is:
#	-----------------------------------------
#	|B7  |B6  |B5  |B4  |B3  |B2  |B1  |B0  |
#	|CH8 |CH7 |CH6 |CH5 |CH4 |CH3 |CH2 |CH1 |
#	-----------------------------------------
#*/
HMS_SET_ACTIVE_CHANNELS   =              int( '00200005', 16)
#
#/** Set ADS input MUX configuration for the specified channel.
#Command contents:
#1. Function Code: 		HMS_SET_ACTIVE_CHANNELS
#2. Message Length: 		2
#3. ADS ID: 				integer values { HMS_ADS1298_ID, HMS_ADS1299_ID }
#4. Channel number:		integer values { 0 - 7 }
#5. Input MUX state.		int
#	Values:
#	The configuration of the analog input, as specified in the ADS12xx datasheet.
#	The range of accepted integer values is 1 to 7.
#	See ads1298.h for the definition of the input MUX configuration.
#*/
HMS_SET_INPUT_MUX         =              int( '00200006', 16)
#
#/** Set ADS input MUX configuration for all channels.
#Command contents:
#1. Function Code: 		HMS_SET_ACTIVE_CHANNELS
#2. Message Length: 		2
#3. ADS ID: 				integer values { HMS_ADS1298_ID, HMS_ADS1299_ID }
#4. Input MUX state.		int
#	Values:
#	The configuration of the analog input, as specified in the ADS12xx datasheet.
#	The range of accepted integer values is 1 to 7.
#	See ads1298.h for the definition of the input MUX configuration.
#*/
HMS_SET_INPUT_MUX_ALL     =              int( '00200007', 16)
#
#/**
#Sets the HMS switch configuration for all channels,
#according to the specified mode.
#Command contents:
#1. Function Code: 		HMS_SET_ALL_CHANNEL_MODE
#2. Message Length: 		8
#4. Channel mode.		uint[]
#Values: The array of channel modes. Index 0 for channel 0, ..., index 7 for channel 7.
#@see hms.h for the list of modes.
#*/
HMS_SET_ALL_CHANNEL_MODE  =              int( '00200008', 16)
#
#/**
#	Sets the HMS switch configuration for the specified channel,
#	according to the specified mode.
#Command contents:
#1. Function Code: 		HMS_SET_CHANNEL_MODE
#2. Message Length: 		2
#3. Channel: 			integer values { 0-7 }
#4. Channel mode.		int
#	Values:
#	@see hms.h for the list of modes.
#*/
HMS_SET_CHANNEL_MODE      =              int( '00200009', 16)
#
#/**
#Sets the MER channel gain calibration.
#Command contents:
#1. Function Code: 		HMS_SET_MER_GAIN_CALIBRATION
#2. Message Length: 		3
#3. Channel: 			integer values { 0-7 }
#4. Calibration:			float values { typically, around 1 }
#5. Write to EEPROM:		integer
#		{ 0 - only update the internal state, but don't write to EEPROM
#		  1 - update the internal state and send this value to the HMS EEPROM }
#*/
HMS_SET_MER_GAIN_CALIBRATION =              int( '0020000A', 16)
#
#/**
#Sets the MER channel offset calibration.
#Command contents:
#1. Function Code: 		HMS_SET_MER_OFFSET_CALIBRATION
#2. Message Length: 		3
#3. Channel: 			integer values { 0-7 }
#4. Calibration:			integer	values { ADS levels, 24 bit wide }
#5. Type:				integer values { 0 - AC offset, 1 - DC offset}
#6. Write to EEPROM:		integer
#{ 0 - only update the internal state, but don't write to EEPROM
#1 - update the internal state and send this value to the HMS EEPROM }
#*/
HMS_SET_MER_OFFSET_CALIBRATION =              int( '0020000B', 16)
#
#/**
#Sets the LFP channel gain calibration.
#Command contents:
#1. Function Code: 		HMS_SET_LFP_GAIN_CALIBRATION
#2. Message Length: 		3
#3. Channel: 			integer values { 0-7 }
#4. Calibration:			float values { typically, around 1 }
#5. Write to EEPROM:		integer
#{ 0 - only update the internal state, but don't write to EEPROM
#1 - update the internal state and send this value to the HMS EEPROM }
#*/
HMS_SET_LFP_GAIN_CALIBRATION =              int( '0020000C', 16)
#
#/**
#Sets the LFP channel offset calibration.
#Command contents:
#1. Function Code: 		HMS_SET_LFP_OFFSET_CALIBRATION
#2. Message Length: 		3
#3. Channel: 			integer values { 0-7 }
#4. Calibration:			integer values { ADS levels, 24 bit wide. }
#5. Write to EEPROM:		integer
#{ 0 - only update the internal state, but don't write to EEPROM
#1 - update the internal state and send this value to the HMS EEPROM }
#*/
HMS_SET_LFP_OFFSET_CALIBRATION =              int( '0020000D', 16)
#
#/**
#Sets the DAC channel gain calibration.
#Command contents:
#1. Function Code: 		HMS_SET_DAC_GAIN_CALIBRATION
#2. Message Length: 		3
#3. Channel: 			integer values { 0-7 }
#4. Calibration:			float values { typically, around 1 }
#5. Write to EEPROM:		integer
#{ 0 - only update the internal state, but don't write to EEPROM
#1 - update the internal state and send this value to the HMS EEPROM }
#*/
HMS_SET_DAC_GAIN_CALIBRATION =              int( '0020000E', 16)
#
#/**
#Sets the DAC channel offset calibration.
#Command contents:
#1. Function Code: 		HMS_SET_DAC_OFFSET_CALIBRATION
#2. Message Length: 		3
#3. Channel: 			integer values { 0-7 }
#4. Calibration:			float values { Scaled amplitude value, range between -1 and 1. }
#5. Stimulation mode		integer value { MODE_MICRO_STIM_CC, MODE_MACRO_STIM_CC, MODE_MICRO_STIM_CV, MODE_MACRO_STIM_CV }
#6. Write to EEPROM:		integer
#{ 0 - only update the internal state, but don't write to EEPROM
#1 - update the internal state and send this value to the HMS EEPROM }
#*/
HMS_SET_DAC_OFFSET_CALIBRATION =              int( '0020000F', 16)
#
#/**
#Sets the ZCheck channel capacitance calibration.
#Command contents:
#1. Function Code: 		HMS_SET_ZCHECK_CAP_CALIBRATION
#2. Message Length: 		3
#3. Channel: 			integer values { 0-7 }
#4. Mode:				integer values { MODE_MICRO_STIM_CC MODE_MACRO_STIM_CC }
#The mode identifies micro or macro contact measurement.
#5. Calibration:			float values { }
#*/
HMS_SET_ZCHECK_CAP_CALIBRATION =              int( '00200010', 16)
#
#/**
#Sets the ZCheck channel capacitance calibration.
#Command contents:
#1. Function Code: 		HMS_SET_ZCHECK_PHASE_CALIBRATION
#2. Message Length: 		3
#3. Channel: 			integer values { 0-7 }
#4. Mode:				integer values { MODE_MICRO_STIM_CC MODE_MACRO_STIM_CC }
#	The mode identifies micro or macro contact measurement.
#5. Calibration:			float values { }
#*/
HMS_SET_ZCHECK_PHASE_CALIBRATION =              int( '00200011', 16)
#
#/**
#	Sets HMS params.
#1. Function Code: 		HMS_SET_PARAMS
#2. Message Length: 		3
#3. Values:				integer
#{ IS_CALIBRATED, SERIAL_NUMBER, BOARD_REVISION }
#as defined in calibration.h
#*/
HMS_SET_PARAMS            =              int( '00200012', 16)
#
#/**
#Configure and enable the LNF (line noise filter).
#Command contents:
#1. Function Code:		HMS_SET_LNF
#2. Message Length:
#3. Channel:				integer values { 0 - 7 }
#3. Enabled:				integer values { 0 - disabled 1 - enabled }
#4. Weight:				float   values { [0, 1] continuous interval }.
#*/
HMS_SET_LNF               =              int( '00200013', 16)
#
#/**
#Configure and enable the SAS (stimulus artifact suppressor).
#Command contents:
#1. Function Code:		HMS_SET_SAS
#2. Message Length:
#3. Channel:				integer values { 0 - 7 }
#3. Enabled:				integer values { 0 - disabled 1 - enabled }
#4. Weight:				float   values { [0, 1] continuous interval }.
#*/
HMS_SET_SAS               =              int( '00200014', 16)
#
#/**
#Configure the HMS board type.
#1. Function Code: 		HMS_SET_BOARD_TYPE
#2. Message Length: 		1
#3. Values:				integer
#{ HMS_BOARD_TYPE_MER_STIM HMS_BOARD_TYPE_STIM_EEG HMS_BOARD_TYPE_EEG }
#as defined in hms.h
#*/
HMS_SET_BOARD_TYPE        =              int( '00200015', 16)
#
#/**
#Reset the EEPROM calibration parameters to defaults.
#1. Function Code: 		HMS_SET_EEPROM_DEFAULTS
#2. Message Length: 		1
#3. Values:				integer { 0, 1 }. The values are ignored.
#*/
HMS_SET_EEPROM_DEFAULTS   =              int( '00200016', 16)
#
#/**
#Set the ADS1299 SRB1 switches.
#1. Function Code: 		HMS_SET_SRB_SWITCHES
#2. Message Length: 		1
#3. Values:				integer { 0, 1 }. 0 - switches open 1 - switches closed
HMS_SET_SRB_SWITCHES      =              int( '00200017', 16)
#
#/**
#Data streaming (MER and LFP) is paused, but timestamps are incremented.
#1. Function Code: 		HMS_SET_PAUSE_RECORDING
#2. Message Length: 		1
#3. Values:				integer { 0, 1 }. 0 - pause recording 1 - resume recording.
#*/
HMS_SET_PAUSE_RECORDING   =              int( '00200018', 16)
#
##define HMS_FAULT
#
#/**
#Sends all MER channels gain calibration to the uplink.
#Command contents:
#1. Function Code: 		HMS_EVENT_MER_GAIN_CALIBRATION
#2. Message Length: 		8
#3. Values:				Gain calibration values for the 8 channels.
#*/
HMS_EVENT_MER_GAIN_CALIBRATION =              int( '9020000A', 16)
#
#/**
#Sends all MER channels offset calibration to the uplink.
#Command contents:
#1. Function Code: 		HMS_EVENT_MER_OFFSET_CALIBRATION
#2. Message Length: 		8
#3. Offset type:			AC/DC
#4. Values:				Offset calibration values for the 8 channels.
#*/
HMS_EVENT_MER_OFFSET_CALIBRATION =              int( '9020000B', 16)
#
#/**
#Sends all LFP channels gain calibration to the uplink.
#Command contents:
#1. Function Code: 		HMS_EVENT_LFP_GAIN_CALIBRATION
#2. Message Length: 		8
#3. Values:				Gain calibration values for the 8 channels.
#*/
HMS_EVENT_LFP_GAIN_CALIBRATION =              int( '9020000C', 16)
#
#/**
#Sends all LFP channels offset calibration to the uplink.
#Command contents:
#1. Function Code: 		HMS_EVENT_LFP_OFFSET_CALIBRATION
#2. Message Length: 		8
#3. Values:				Offset calibration values for the 8 channels.
#*/
HMS_EVENT_LFP_OFFSET_CALIBRATION =              int( '9020000D', 16)
#
#/**
#Sends all DAC channels gain calibration to the uplink.
#Command contents:
#1. Function Code: 		HMS_EVENT_DAC_GAIN_CALIBRATION
#2. Message Length: 		8
#3. Values:				Gain calibration values for the 8 channels.
#*/
HMS_EVENT_DAC_GAIN_CALIBRATION =              int( '9020000E', 16)
#
#/**
#Sends all DAC channels offset calibration to the uplink.
#Command contents:
#1. Function Code: 		HMS_EVENT_DAC_OFFSET_CALIBRATION
#2. Message Length: 		8
#3. Values:				Gain calibration values for the 8 channels.
#*/
HMS_EVENT_DAC_OFFSET_CALIBRATION =              int( '9020000F', 16)
#
#/**
#Sends all ZCheck channels capacitance calibration to the uplink.
#Command contents:
#1. Function Code: 		HMS_EVENT_ZCHECK_CAP_CALIBRATION
#2. Message Length: 		8
#3. Values:				Capacitance calibration values for the 8 channels.
#*/
HMS_EVENT_ZCHECK_CAP_CALIBRATION =              int( '90200010', 16)
#
#/**
#Sends all ZCheck channels phase calibration to the uplink.
#Command contents:
#1. Function Code: 		HMS_EVENT_ZCHECK_CAP_CALIBRATION
#2. Message Length: 		8
#3. Values:				Capacitance calibration values for the 8 channels.
#*/
HMS_EVENT_ZCHECK_PHASE_CALIBRATION =              int( '90200011', 16)
#
#/**
#	Sends HMS params to the uplink.
#	1. Function Code: 		HMS_EVENT_PARAMS
#	2. Message Length: 		3
#	3. Values:				integer
#		{ IS_CALIBRATED, SERIAL_NUMBER, BOARD_REVISION }
#		as defined in calibration.h
#	*/
HMS_EVENT_PARAMS          =              int( '90200012', 16)
#
#/**
#Sends HMS board type to the uplink.
#1. Function Code: 		HMS_EVENT_BOARD_TYPE
#2. Message Length: 		2
#3. Board Type:			integer
#{ HMS_BOARD_TYPE_MER_STIM HMS_BOARD_TYPE_STIM_EEG HMS_BOARD_TYPE_EEG }
#as defined in hms.h
#4. Device Id			integer values { 0, 1, ...}.
#   The device Id is an APM indentifier tied to its physical address.
#*/
HMS_EVENT_BOARD_TYPE      =              int( '90200013', 16)
#
#/**
#	Sends HMS SWITCH write error to the uplink.
#	1. Function Code: 		HMS_EVENT_SWITCH_WRITE_ERROR
#	2. Message Length: 		1
#	3. Values:				integer
#	{ 0 - no values}
#*/
HMS_EVENT_SWITCH_WRITE_ERROR =              int( '90200014', 16)
#
#/**
#Returns the state of the HMS - connected or not connected.
#1. Function Code: 		HMS_EVENT_IS_INITIALIZED
#2. Message Length: 		1
#3. Values:				integer
#{ 0 - HMS not found 1 - HMS initialized. }
#*/
HMS_EVENT_IS_INITIALIZED  =              int( '90200015', 16)
#
#/**
#Sends the MER voltage calibration constant over TCP/ IP (PC to PC).
#This event is not generated by the DSP.
#1. Event Code : HMS_EVENT_MER_VOLTAGE_CALIBRATION
#2. Message Length : 3
#3. Channel Number : integer values{ 1 .. }
#4. Device Identifier : integer values { 0, 1 }
#5. Voltage Calibration : Calibration value used to convert ADC samples into micro - volts.
#*/
HMS_EVENT_MER_VOLTAGE_CALIBRATION =              int( '90200016', 16)
#
#/**
#Sends the LFP voltage calibration constant over TCP/ IP (PC to PC).
#This event is not generated by the DSP.
#1. Event Code : HMS_EVENT_LFP_VOLTAGE_CALIBRATION
#2. Message Length : 3
#3. Channel Number : integer values{ 1 .. }
#4. Device Identifier : integer values { 0, 1 }
#5. Voltage Calibration : Calibration value used to convert ADC samples into micro - volts.
#*/
HMS_EVENT_LFP_VOLTAGE_CALIBRATION =              int( '90200017', 16)
#
#/**
#	Sends HMS ADS gain write error to the uplink.
#	1. Function Code: 		HMS_EVENT_ADS_WRITE_GAIN_ERROR
#	2. Message Length: 		1
#	3. Values:				integer
#	{ 0 - no values}
#*/
HMS_EVENT_ADS_WRITE_GAIN_ERROR =              int( '90200018', 16)
#
#/**
#	Sends HMS ADS gain all write error to the uplink.
#	1. Function Code: 		HMS_EVENT_ADS_WRITE_GAIN_ALL_ERROR
#	2. Message Length: 		1
#	3. Values:				integer
#	{ 0 - no values}
#*/
HMS_EVENT_ADS_WRITE_GAIN_ALL_ERROR =              int( '90200019', 16)
#
#/**
#	Sends HMS ADS sample rate write error to the uplink.
#	1. Function Code: 		HMS_EVENT_ADS_WRITE_SAMPLE_RATE_ERROR
#	2. Message Length: 		1
#	3. Values:				integer
#	{ 0 - no values}
#*/
HMS_EVENT_ADS_WRITE_SAMPLE_RATE_ERROR =              int( '9020001A', 16)
#
#/**
#Microelectrode data sample rate event.
#1. Function Code: 		HMS_EVENT_MER_SAMPLING_RATE
#2. Message Length: 		2
#3. Device Identifier:	integer values { 0, 1 .. }
#4. Sample Rate:			integer
#	{ 32000 - default other options: 16000, 8000, 4000, 2000, 1000, 500 }
#	The sample rate is specified in Hertz.
#*/
HMS_EVENT_MER_SAMPLING_RATE =              int( '9020001B', 16)
#
#/**
#Low frequency signals sample rate event.
#1. Function Code: 		HMS_EVENT_LFS_SAMPLING_RATE
#2. Message Length: 		2
#3. Device Identifier:	integer values { 0, 1 .. }
#4. Sample Rate:			integer
#	{ 1000 - default other options: 16000, 8000, 4000, 2000, 1000, 500, 250 }
#	The sample rate is specified in Hertz.
#*/
HMS_EVENT_LFS_SAMPLING_RATE =              int( '9020001C', 16)
#
#/**
#Low frequency signals sample rate event.
#1. Function Code: 		HMS_EVENT_BOARD_RESET
#2. Message Length: 		2
#3. Device Identifier:	integer values { 0, 1 .. }
#4. Reset:				integer values { 1 }
#*/
HMS_EVENT_BOARD_RESET     =              int( '9020001D', 16)
#
#/******************************************************************************
#* LFP Data codes
#*
#*******************************************************************************/
#/**@ brief Local Field Potentials (LFP) data code.
#1. Message code: LFP_DATA_RAW
#2. Message length: (2 + nChannels * nSamplesPerChannel)
#3. Active channels bitmap
#4. Timestamp (unsigned int)
#5. N channels of M samples each.
#Please see the eRPC protocol documentation for more information on
#the data code message format.
#*/
LFP_DATA_RAW              =              int( '300C0001', 16)
#
#/** Set the firmware application mode.
#Command contents:
#1. Function Code: GL5K_SET_MODE
#2. Message Length: 1
#3. Application mode: integer values { 	APP_RECORDING = 2,
#APP_STIM_REC = 3,
#APP_STIM = 4,
#APP_ZCHECK = 5,
#APP_CALIBRATE = 6
#@see app_state_t in gl5k_app.h.
#*/
GL5K_SET_MODE             =              int( '00300001', 16)
#
#/// @cond DO_NOT_DOCUMENT
#/******************************************************************************
#* MTC function codes
#*
#*******************************************************************************/
MTC_SEND_CMD              =              int( '00400001', 16)
MTC_EVENT_TCP_CMD_SEND    =              int( '90401001', 16)
#/** This event is sent when the mTC postion changes.
#	This code is used to store the information in the data file, it is not exchanged
#	between DSP and software.
#1. Event code: MTC_EVENT_DRIVE_POSTION
#2. Message length: 4
#3. Drive Number: 1 - left, 2 - right.
#4. Drive position: integer {0 - 50000} microns.
#5. Next depth position: long {1 - long.MaxValue}. Pointer to the next depth stored
#													in the data file.
#*/
MTC_EVENT_DRIVE_POSITION  =              int( '90400002', 16)
#/// @endcond
#
#/** This even is sent when an invalid parameter is received when running a function call.
#Event contents:
#1. Event code: ERROR_INVALID_PARAMETER
#2. Message length: 1
#3. Function code: The function code that was executed when the error occurred.
#
#*/
ERROR_INVALID_PARAMETER   =              int( '50000012', 16)
#
#/** This even is sent when an invalid calibration parameter value is retrieved from the
#interface EEPROM.
#Event contents:
#1. Event code: ERROR_INVALID_CALIBRATION
#2. Message length: 3
#3. Calibration code (gain, offset, phase, etc.)
#4. Calibration type (optional e.g. AC/ DC offset calibration)
#4. Channel number
#*/
ERROR_INVALID_CALIBRATION =              int( '5020FFFF', 16)
#
#
#/** Identifies a Guideline 5 data file header.
#	Contents:
#1. Code: EVENT_FILE_HEADER
#2. Message Length: [TODO]
#3. ...
#*/
EVENT_FILE_HEADER         =              int( '91000001', 16)
#
#/** Identifies a Guideline 5 Data file index code.
#Contents:
#1. Code: FILE_INDEX
#2. Data block index: values { Int64 }
#3. Timestamp: date time of the index values { Int64 }
#*/
FILE_INDEX_BLOCK          =              int( '31000001', 16)
#
#/** Identifies motion sensor data within the data file.
#	This code is not used by firmware, but it's defined
#	here to maintain the file codes in the same location.
#Contents:
#1. SYNC
#2. Message code: MOTION_DATA_MESSAGE
#3. Message Length: 3 * N +1, where N is the number of samples per axis.
#4. Timestamp: integer, values { 0 - max int}
#5. X: float values { N motion sensor X axis samples }
#6. Y: float values { N motion sensor Y axis samples }
#7. Z: float values { N motion sensor Z axis samples }
#*/
MOTION_DATA_MESSAGE       =              int( '32000001', 16)
#
#
#/** Specifies the motion sensor sampling rate.
#	This code is not used by firmware, but it's defined
#	here to maintain the file codes in the same location.
#Contents:
#1. SYNC
#2. Message code: MOTION_SENSOR_SAMPLING_RATE
#3. Message Length: 1
#4. Sampling rate: unsigned integer {1 - N}.
#*/
MOTION_SENSOR_EVENT_SAMPLING_RATE =              int( '92000002', 16)
#
#/** Marks the start of the sensory motor testing.
#Contents:
#1. SYNC
#2. Message code: MOTION_SENSOR_EVENT_START_TESTING
#3. Message Length: 0
#*/
MOTION_SENSOR_EVENT_START_TESTING =              int( '92000003', 16)
#
#
#/** Marks the end of the sensory motor testing.
#Contents:
#1. SYNC
#2. Message code: MOTION_SENSOR_EVENT_START_TESTING
#3. Message Length: 0
#*/
MOTION_SENSOR_EVENT_STOP_TESTING =              int( '92000004', 16)
#
##endif // _MESSAGE_H_
