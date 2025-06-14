import commands2
from rev import SparkMax
#from rev import SparkMaxConfig
from wpilib.drive import DifferentialDrive
import wpilib
import wpilib.drive

class Drivesubsystem(commands2.Subsystem ,):
    def __init__(self):
        super().__init__()    
        self.left1 = SparkMax(1, SparkMax.MotorType.kBrushed)
        self.left2 = SparkMax(2, SparkMax.MotorType.kBrushed)
        self.right1 = SparkMax(3, SparkMax.MotorType.kBrushed)
        self.right2 = SparkMax(4, SparkMax.MotorType.kBrushed)
        self.left = wpilib.MotorControllerGroup(self.left1,self.left2)
        self.right = wpilib.MotorControllerGroup(self.right1,self.right2)

        self.drive = DifferentialDrive(self.left1,self.right1)
        self.drive.setMaxOutput(0.4)




    def arcadeDrive(self, fwd, rot):
        self.drive.arcadeDrive(fwd, rot)

    def stopMotor(self):
        self.drive.stopMotor()


    def autonomousRoutine(self, timer: wpilib.Timer):
        if timer.get() < 5.0:
            self.arcadeDrive(xSpeed=-0.4, zRotation=0, squareInputs=False)
        elif timer.get() < 5.5:
            self.arcadeDrive(xSpeed=0, zRotation=1.0, squareInputs=False)  # 用 1.0 比較安全
        elif timer.get() < 6.5:
            self.arcadeDrive(xSpeed=-0.3, zRotation=0, squareInputs=False)
        else:
            self.stopMotor()



#        cfg_left1 = SparkMaxConfig()
#        self.left1.configure(cfg_left1, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)
#
#        cfg_left2 = SparkMaxConfig()
#        cfg_left2.follow(self.left1, False)
#        self.left2.configure(cfg_left2, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)
#
#        cfg_right1 = SparkMaxConfig()
#        cfg_right1.inverted(True)
#        self.right1.configure(cfg_right1, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)
#
#        cfg_right2 = SparkMaxConfig()
#        cfg_right2.follow(self.right1, False)
#        self.right2.configure(cfg_right2, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)
#


# subsystems/drivesubsystem.py







