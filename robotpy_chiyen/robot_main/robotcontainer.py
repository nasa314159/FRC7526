import commands2
from subsystems.drivesubsystem import Drivesubsystem  
import wpilib
from wpilib.drive import DifferentialDrive

class RobotContainer:
    def __init__(self):
        self.stick = wpilib.XboxController(0)

        self.drive = Drivesubsystem()
        self.drivecontrol = DifferentialDrive(self.drive.left1,self.drive.right1)
        self.drivecontrol.setMaxOutput(0.4)


    def applyDeadzone(self, value, deadzone=0.1):
        return 0 if abs(value) < deadzone else value
    
    def teleopPeriodic(self):
        # 讀取搖桿輸入，並加入 deadzone 處理
        forward = self.applyDeadzone(self.stick.getLeftY())
        turn = self.applyDeadzone(self.stick.getRightX())

        # 執行 arcadeDrive（前後 + 左右轉）
        self.drivecontrol.arcadeDrive(forward, turn)
        a = 123

