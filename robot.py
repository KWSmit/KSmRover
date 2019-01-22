from ev3dev2.motor import MoveJoystick, OUTPUT_A, OUTPUT_B
from ev3dev2 import get_current_platform


class JoyStickRobot():
    ''' Robot with joystick steering.'''
    def __init__(self):
        self.robot = MoveJoystick(OUTPUT_A, OUTPUT_B)
        self.platform_type = get_current_platform()
