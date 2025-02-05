# [EXPERIMENT MODES]
experiment_modes = [0, 1, 2, 3]
# 0 = normal mode
# 1 = random poetry only. No AI. No human interaction
# 2 = human input only
# 3 = scripted list


# [HARDWARE]
xarm_connected = True
# eda_live = False

# [DATAWRITER]
# data_writer = False
data_logging = True
# pupil_logging = False
# pupil_labs_addr = "tcp://127.0.0.1:50020"
path = "data"
figsize_xy = (100, 12)
samplerate = 0.01

# [PLAY PARAMS]
silence_listener = False
duration_of_piece = 240  # 240  # in sec
speed = 5  # dynamic tempo of the all processes: 1 = slow, 10 = fast
temperature = 0

# [XARM]
xarm1_port = '192.168.1.222'
xarm_x_extents = [-500, 500]  # cartesian coords in mm
xarm_y_extents = [-500, 500]
xarm_z_extents = [55, 1000]
# xarm_ballet_x_extents = [400, 400]
# xarm_ballet_y_extents = [-250, 250]
# xarm_ballet_z_extents = [150, 400]
xarm_irregular_shape_extents = 50
xarm_fenced = True

# [SOUND IN]
mic_sensitivity = 10000
mic_in_prediction = 0.36
mic_in_logging = False

# [BITALINO]
baudrate = 100
channels = [0, 1, 2, 3]  # , 4, 5]
mac_address = "98:D3:B1:FD:3D:1F"  #"00:21:08:35:16:D4"    # "00:21:08:35:17:C0" #"98:D3:B1:FD:3D:1F"  # '/dev/cu.BITalino-3F-AE' (Linux)

# [STREAMING]
stream_list = ['rnd_poetry',
               'flow2core',
               'core2flow',
               'audio2core',
               'audio2flow',
               'flow2audio',
               'eda2flow']



"""
Notes:
To check available ports, run the following code:
    from serial.tools import list_ports

    available_ports = list_ports.comports()
    print(f'available ports: {[x.device for x in available_ports]}')

May need `sudo chmod 666 /dev/ttyACM0`
"""
