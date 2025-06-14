import commands2
from subsystems.drivesubsystem import Drivesubsystem  
import wpilib
from wpilib.drive import DifferentialDrive
from commands2 import RunCommand
from subsystems.elevatorsubsystem import ElevatorSubsystem
import wpilib.drive

class RobotContainer:
    def __init__(self):
        self.stick = wpilib.XboxController(0)
        self.drive = Drivesubsystem()
        self.elevator = ElevatorSubsystem()
        self.timer: wpilib.Timer = wpilib.Timer()
        self.elevator.pid_p
        self.elevator.prev_a
        self.elevator.prev_b
        n = 0

        # ...existing code...
        # Elevator 控制：按 X 增加 50、按 Y 減少 50
#        if self.stick.getXButton():
 #           n += 50
  #          self.elevator.setHeight(n)
   #     elif self.stick.getYButton():
    #        n -= 50
     #       self.elevator.setHeight(n)

        self.drive.setDefaultCommand(
            RunCommand(
                lambda: self.drive.arcadeDrive(
                    self.applyDeadzone(self.stick.getLeftY()),
                    self.applyDeadzone(self.stick.getRightX())
                ),
                self.drive
            )
        )

    def applyDeadzone(self, value, deadzone=0.1):
        return 0 if abs(value) < deadzone else value
'''
    def robotPeriodic(self):
        # 取得目前按鈕狀態
        a_pressed = self.stick.getAButton()
        b_pressed = self.stick.getBButton()

        # --- A 鍵剛被按下：增加 P 值 ---
        if a_pressed and not self.prev_a:
            self.elevator.pid_p += 0.01
            print(f"P 值增加為 {self.pid_p:.2f}")
            self.elevator.setPID(self.pid_p, 0, 0)

        # --- B 鍵剛被按下：減少 P 值 ---
        if b_pressed and not self.prev_b:
            self.elevator.pid_p = max(0, self.pid_p - 0.01)
            print(f"P 值減少為 {self.pid_p:.2f}")
            self.elevator.setPID(self.pid_p, 0, 0)

        # 記住前一次的狀態（做「邊緣觸發」）
        self.prev_a = a_pressed
        self.prev_b = b_pressed
'''



    


