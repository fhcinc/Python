import numpy as np


class Drive:
    def __init__(self):
        self.timestamps: [] = []
        self.drive_depths: [] = []


class Channel:
    """
      A class used to represent the signal data
      ...

      Attributes
      ----------
       continuous : [np.single]
            extracted MER data for the segment, in microvolts.
       lf : List[np.single]
            extracted LFP data for the segment, in microvolts.

      """
    def __init__(self):
        self.continuous: [] = []
        self.lf: [] = []


class Pulse:
    def __init__(self):
        self.freq: np.uint32 = np.uint32(0)
        self.channel: np.uint32 = np.uint32(0)
        self.amplitude: np.uint32 = np.uint32(0)
        self.duration: np.uint32 = np.uint32(0)
        self.phase: np.uint32 = np.uint32(0)
        self.polarity: np.uint32 = np.uint32(0)


class StimParams:
    """
     A class used to represent the stimulation parameters
     ...

     Attributes
     ----------
      stim_type : np.uint32
           1 - macro, 0 - micro
      stim_mode : np.uint32
           1 - constant voltage, 0 - constant current
      output_channel_map: np.uint32
           output channel bitmap
      return_channel_map: np.uint32
           return channel bitmap
      pulse: Dict[int,Pulse]
           key:;value:pulse parameters object
     """
    def __init__(self):
        self.stim_type: np.uint32 = np.uint32(0)
        self.stim_mode: np.uint32 = np.uint32(0)
        self.output_channel_map: np.uint32 = np.uint32(0)
        self.return_channel_map: np.uint32 = np.uint32(0)
        self.pulse: {} = {}


class Sync:
    """
     Attributes
     ----------
      rt_timestamps : List[np.uint32]
        timestamps of the real time digital input on the Sync unit.
      timestamps: List[np.uint32]
      port1: List[np.uint32]
      port2: List[np.uint32]
      digin: List[np.uint32]
     """
    def __init__(self):
        self.rt_timestamps: [] = []
        self.timestamps: [] = []
        self.port1: [] = []
        self.port2: [] = []
        self.digin: [] = []


class MotionData:
    """
     Attributes
     ----------
      timestamps : List[np.int64]
            an array of 64-bit integers that  match the binary representation of a System.DateTime .NET Framework object
      x: list[np.single]
            Accelerometer X axis values
      y: list[np.single]
            Accelerometer Y axis values
      z: list[np.single]
            Accelerometer Z axis values
    """
    def __init__(self):
        self.timestamps: [] = []
        self.x: [] = []
        self.y: [] = []
        self.z: [] = []


class Motion:
    def __init__(self):
        self.sampling_rate: int = 0
        self.start_timestamp: int = 0
        self.data: MotionData = MotionData()


class Aux:
    """
     Attributes
     ----------
      channels: Dict[int, Channel]
            key: channel; value: Channel object
    """
    def __init__(self):
        self.timestamps_aux: [] = []
        self.channels: {} = {}
        self.sampling_rate: np.uint32 = np.uint32(0)


class Segment:
    """
       A class used to represent the event data
       ...

       Attributes
       ----------
        drive : Dict[int,Drive]
            key: hemisphere(1 = left, 2 = right);  value: Drive object
        offset_ac_mer : Dict[int, np.uint32]
            key: channel ,value:  AC offset calibration constant
        offset_dc_mer : Dict[int, np.uint32]
            key: channel ,value:  DC offset calibration constant
        start_timestamp_mer: np.uint32
            MER start timestamp
        start_timestamp_lf: np.uint32
            LF start timestamp
        sampling_rate_mer: list[np.single]
            MER sampling rate
        sampling_rate_lf: list[np.single]
            LF sampling rate
        v_cal_mer: Dict[int, np.single]
            key: channel; value: Scale raw MER data to microvolts
        v_cal_lf: Dict[int, np.single]
            key: channel; value: Scale raw LF data to microvolts
        channels: Dict[int, Channel]
            key: channel; value: Channel object
        stim_on: np.uint32
            stimulation on timestamp
        stim_off: np.uint32
            stimulation off timestamp
        sync: Sync
        motion: motion
        offset_dc_lfs: Dict[int, np.uint32]
            key: channel ,value:  DC offset calibration constant
        aux: Aux
        stim_params: List[StimParams]

   """
    def __init__(self):
        self.drive: {} = {}
        self.offset_ac_mer: {} = {}
        self.offset_dc_mer: {} = {}
        self.start_timestamp_mer: np.uint32 = np.uint32(0)
        self.start_timestamp_lf: np.uint32 = np.uint32(0)
        self.sampling_rate_mer: [] = []
        self.sampling_rate_lf: [] = []
        self.v_cal_mer: {} = {}
        self.v_cal_lf: {} = {}
        self.channels: {} = {}
        self.stim_on: np.uint32 = np.uint32(0)
        self.stim_off: np.uint32 = np.uint32(0)
        self.sync: Sync = Sync()
        self.motion: Motion = Motion()
        self.offset_dc_lfs : {} = {}
        self.aux: Aux = Aux()
        self.stim_params: {} = {}


class FileInfo:
    """
     Attributes
     ----------
      version : np.uint32
            file version
      deviceId: np.uint32
            device identifier (0 - GL5 port 1 or 1 - GL5 port 2)
     """
    def __init__(self):
        self.version: np.uint32 = np.uint32(0)
        self.device_id: np.uint32 = np.uint32(0)


class Device:
    def __init__(self):
        self.board_type: int = 0


class T:
    """
        A class used to represent the extracted data
        ...

        Attributes
        ----------
        segments : list[Segment]
            list of the events data
        file_info : FileInfo
            information about the file
        device : Device
            information about the GL5 device

    """
    def __init__(self):
        self.segments: [] = []
        self.file_info: FileInfo = FileInfo()
        self.device: Device = Device()