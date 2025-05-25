import commands2
from subsystems.drivesubsystem import Drivesubsystem  
import wpilib

class RobotContainer:
    def __init__(self):
        self.stick = wpilib.XboxController(0)

        self.drive = Drivesubsystem()


    def applyDeadzone(self, value, deadzone=0.1):
        return 0 if abs(value) < deadzone else value
    
    def teleopPeriodic(self):
        # 讀取搖桿輸入，並加入 deadzone 處理
        forward = self.applyDeadzone(self.stick.getLeftY())
        turn = self.applyDeadzone(self.stick.getRightX())

