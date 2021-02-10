MSG_AUX_DIGITAL_INPUT_ON    = b'07'
MSG_AUX_DIGITAL_INPUT_OFF   = b'17'

# Message codes definitions, see FileMessageCodes.h file in the C API

MSG_NACC_WAVEFORM           = b'00'
MSG_ACC_WAVEFORM	        = b'01'
MSG_NOTRIAL_NACC_WAVEFORM	= b'02'
MSG_NOTRIAL_ACC_WAVEFORM	= b'03'
MSG_TIMESTAMP				= b'04'
MSG_START_OF_TRIAL			= b'05'
MSG_END_OF_TRIAL			= b'06'
MSG_EXT_EVENT				= b'07'
MSG_TRIGGER_LEVEL			= b'08'
MSG_TRIGGER_TIME			= b'09'
MSG_TRIGGER_SLOPE			= b'10'
MSG_WINDOW_TIME				= b'11'
MSG_WINDOW_LOW				= b'12'
MSG_WINDOW_HIGH				= b'13'
MSG_TIME_CALIBRATION		= b'14'
MSG_VOLTAGE_CALIBRATION		= b'15'
MSG_SAMPLING_FREQUENCY		= b'16'
MSG_REWARD					= b'17'
MSG_LFP_TIME_CALIBRATION	= b'18'
MSG_DIGINPUT_CHANGED	    = b'19'
MSG_STROBED_DATA        	= b'20'
MSG_UART_DATA               = b'21'
MSG_SPIKE_LEN       	    = b'22'   # Code added by FSS
MSG_AVG_SAMPLES         	= b'23'     #Code added by FSS
MSG_DRIVE_DEPTH            	= b'24'
MSG_CHANNEL_INFO           	= b'25'   # Type (if missing, then APM_CHAN is assumed)
MSG_CHANNEL_NAME           	= b'26'   # Channel name, a string that's padded to a multiple of 4 characters, to fit into the message structure
MSG_LINE_NOISE_FILTER      	= b'27'
MSG_HIGH_PASS_FREQ         	= b'28'
MSG_LOW_PASS_FREQ         	= b'29'
MSG_TEMPLATE				= b'32'
MSG_MEAN_FIRING_RATE        = b'40'
MSG_RMS                     = b'46'
MSG_CONT_WAVEFORM			= b'48'
MSG_LFP     				= b'56'
MSG_TRIAL_SLOW_WAVEFORM	    = b'64'
MSG_NOTRIAL_SLOW_WAVEFORM	= b'66'
MSG_AUX_DATA        	    = b'72'
MSG_TCPIP_USER0				= int('10000', 16)
MSG_TCPIP_USER1				= int('10001', 16)
MSG_TCPIP_USER2				= int('10002', 16)
MSG_TCPIP_USER3				= int('10003', 16)
MSG_TCPIP_USER4				= int('10004', 16)
MSG_TCPIP_USER5				= int('10005', 16)
MSG_TCPIP_USER6				= int('10006', 16)
MSG_TCPIP_USER7				= int('10007', 16)

MSG_STIMULUS_ARTIFACT_SUPPRESSOR	= b'86'

MSG_STIM_ON_TIMESTAMP               = b'90'
MSG_STIM_OFF_TIMESTAMP              = b'91'

MSG_STIMULATION_MODE                = b'92'
MSG_STIMULATION_CATHODE             = b'93'
MSG_STIMULATION_ANODE               = b'94'
MSG_STIMULATION_CURRENT             = b'95'
MSG_STIMULATION_PULSE_FREQUENCY     = b'96'
MSG_STIMULATION_PULSE_DURATION      = b'97'
MSG_STIMULATION_PULSE_PHASE         = b'98'
MSG_STIMULATION_PULSE_POLARITY      = b'99'
MSG_STIMULATION_TRAIN_DURATION      = b'100'
MSG_STIMULATION_SAMPLING_FREQUENCY  = b'101'
MSG_STIMULATION_PULSE_TYPE          = b'102'
