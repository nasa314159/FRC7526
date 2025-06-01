import commands2
from subsystems.drivesubsystem import Drivesubsystem  
import wpilib
from wpilib.drive import DifferentialDrive
from commands2 import RunCommand

class RobotContainer:
    def __init__(self):
        self.stick = wpilib.XboxController(0)
        self.drive = Drivesubsystem()

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
    


