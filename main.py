import PySimpleGUI as sg
import odrive
from odrive.enums import *

print('Searching for ODrive...')
odrv0 = odrive.find_any()

sg.theme('Black')

layout = [
    [sg.Text('ODrive Motor Tuning')],
    [sg.Text('Axis0'), sg.Text('input_vel'), sg.InputText('0')],
    [sg.Text('Axis1'), sg.Text('input_vel'), sg.InputText('0')],
    [sg.Button('Calibration'), sg.Button('IDLE'), sg.Button('LOOP'), sg.Button('Send Setting')]
]

window = sg.Window('ODrive GUI', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Calibration':
        odrv0.axis0.requested_state = odrv0.axis1.requested_state = AXIS_STATE_MOTOR_CALIBRATION
    elif event == 'IDLE':
        odrv0.axis0.requested_state = odrv0.axis1.requested_state = AXIS_STATE_IDLE
    elif event == 'LOOP':
        odrv0.axis0.requested_state = odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
    elif event == 'Send Setting':
        odrv0.axis0.controller.input_vel = int(values[0])
        odrv0.axis1.controller.input_vel = int(values[1])

window.close()
