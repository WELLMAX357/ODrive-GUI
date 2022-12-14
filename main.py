import time

import PySimpleGUI as sg
import odrive
from odrive.enums import AxisState

import config


def calibrate():
    odrv0.axis0.requested_state = odrv0.axis1.requested_state = AxisState.MOTOR_CALIBRATION

def loop():
    odrv0.axis0.requested_state = odrv0.axis1.requested_state = AxisState.CLOSED_LOOP_CONTROL

def stop():
    odrv0.axis0.requested_state = odrv0.axis1.requested_state = AxisState.IDLE

def sendVelocity():
    odrv0.axis0.controller.input_vel = int(values[0])
    odrv0.axis1.controller.input_vel = int(values[0])


print('Searching ODrive...')
odrv0 = odrive.find_any()
print('Find ODrive!!!')


# add a touch of color
sg.theme('Black')


# all the stuff inside window
layout = [
    [sg.Text('ODrive Motor Tuning')],

    # [sg.Text('Voltage'), sg.Print(float(odrv0.vbus_voltage))],
    
    # axis0
    [sg.Text('Axis0'),
    sg.Slider(range=(-300,300), default_value=0, resolution=10, orientation='h',
    enable_events=True, disable_number_display=True, size=(50,40), key='sl0'),
    sg.InputText(default_text='0', size=(5, 1), key='txt0'),
    sg.Button('Set', key='btn0')],
    
    # axis1
    [sg.Text('Axis1'),
    sg.Slider(range=(-300,300), default_value=0, resolution=10, orientation='h',
    enable_events=True, disable_number_display=True, size=(50,40), key='sl1'),
    sg.InputText(default_text='0', size=(5, 1), key='txt1'),
    sg.Button('Set', key='btn1')],
    
    # button
    [sg.Button('Calibration'), sg.Button('STOP'), sg.Button('LOOP'), sg.Button('Send Velocity')],
]

# create window object
window = sg.Window('ODrive GUI', layout)

while True:
    # load events
    event, values = window.read()

    # close window
    if event == sg.WIN_CLOSED:
        break

    # update axis0 value
    elif event == 'sl0':
        window['txt0'].Update(int(values['sl0']))
    elif event == 'btn0':
        window['sl0'].Update(int(values['txt0']))

    # update axis1 value
    elif event == 'sl1':
        window['txt1'].Update(int(values['sl1']))
    elif event == 'btn1':
        window['sl1'].Update(int(values['txt1']))

    # start calibration
    elif event == 'Calibration':
        calibrate()
        time.sleep(0.5)

    # stop rotaion
    elif event == 'STOP':
        stop()

    # start rotation    
    elif event == 'LOOP':
        loop()
        time.sleep(0.5)

    # send velocity
    elif event == 'Send Velocity':
        odrv0.axis0.controller.input_vel = int(values['txt0'])
        odrv0.axis1.controller.input_vel = int(values['txt1'])

window.close()