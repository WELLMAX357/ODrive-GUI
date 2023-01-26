import time

import PySimpleGUI as sg
import odrive
from odrive.enums import AxisState

import config


def calibrate():
    odrv0.axis0.requested_state = AxisState.MOTOR_CALIBRATION

def loop():
    odrv0.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL

def stop():
    odrv0.axis0.requested_state = AxisState.IDLE

def sendVelocity():
    odrv0.axis0.controller.input_vel = int(values[0])


print('Searching ODrive...')
odrv0 = odrive.find_any()
print('Find ODrive!!!')

print(f'SN {hex(odrv0.serial_number).removeprefix("0x").upper()}')
print(f'HW {odrv0.hw_version_major}.{odrv0.hw_version_minor}.{odrv0.hw_version_variant}')
print(f'FW {odrv0.fw_version_major}.{odrv0.fw_version_minor}.{odrv0.fw_version_revision}')

# add a touch of color
sg.theme('Black')

# all the stuff inside window
layout = [
    [sg.Text('ODrive Motor Tuning')],

    # voltage
    [sg.Text('Voltage'), sg.Text('Loading...', key='voltage')],
    
    # axis0
    [sg.Text('Axis0'),
    sg.Slider(range=(-300,300), default_value=0, resolution=10, orientation='h',
    enable_events=True, disable_number_display=True, size=(50,40), key='sl0'),
    sg.InputText(default_text='0', size=(5, 1), key='txt0'),
    sg.Button('Set', key='btn0')],
    
    # button
    [sg.Button('Calibration'), sg.Button('STOP'), sg.Button('LOOP'), sg.Button('Send Velocity')],
]


# create window object
window = sg.Window('ODrive GUI', layout)

while True:
    # load events
    event, values = window.read(timeout=10000)

    # close window
    if event == sg.WIN_CLOSED:
        break

    # update voltage
    elif event == sg.TIMEOUT_EVENT:
        window['voltage'].Update(round(float(odrv0.vbus_voltage), 2))

    # update axis1 value
    elif event == 'sl0':
        window['txt0'].Update(int(values['sl0']))
    elif event == 'btn0':
        window['sl0'].Update(int(values['txt0']))

    # start calibration
    elif event == 'Calibration':
        calibrate()

    # stop rotaion
    elif event == 'STOP':
        stop()

    # start rotation    
    elif event == 'LOOP':
        loop()

    # send velocity
    elif event == 'Send Velocity':
        odrv0.axis0.controller.input_vel = int(values['txt0'])

window.close()