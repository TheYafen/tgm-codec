from pprint import pprint
from collections import OrderedDict
from time import strftime
from time import time
from time import sleep
import copy
import socket
    
####Structure:
header = {
    'tg_id':        None,
    'tg_version':   None,
    'tg_uniq_id':   None,
    'tg_sender':    None,
    'tg_receiver':  None,
    'tg_size':      None,
    'tg_counter':   None,
    'tg_time':      None,
    'tg_reserved':  None,
    }

measurement_result = {
    'Measurement Status':   None,
    'type':                 None,
    'order':                None,
    'customer_id':          None,
    'client_id':            None,
    'truck_id':             None,
    'reserved':             None,
    }


######Body code
####Measurement Results

m_status = {
    0b0000_0000_0000_0001: 'Measurement Abort',
    0b0000_0000_0000_0010: 'Measurement Error',
    0b0000_1000_0000_0000: 'Test01',
    0b0000_0000_1000_0000: 'Test02',
}

m_type = {
    0b0000_0001: 'Empty Measurement',
    0b0000_0010: 'Full Measurement',
    0b0000_0100: 'Reference Measurement',
    0b0000_1000: 'Calibration Measurement',
}

m_order = {
    0b0000_0001: 'Incoming Measurement',
    0b0000_0010: 'Outgoing Measurement',
}

m_direction = {
    0b0000_0001: 'Left to Right',
    0b0000_0010: 'Right to LEft',
}
    
res = b''


with open('bin_reply.bin', 'rb') as f:
    byte = f.read(1)
    while byte != b'':
        res += byte
        byte = f.read(1)
#################
