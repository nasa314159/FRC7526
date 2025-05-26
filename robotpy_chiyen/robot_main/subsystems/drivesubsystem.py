import rev
import commands2
import wpilib
from wpilib.drive import DifferentialDrive
from rev import SparkMax
from rev import SparkMaxConfig
import wpilib.drive

class Drivesubsystem(commands2.Subsystem):
    def __init__(self):    
        self.left1 = SparkMax(1, SparkMax.MotorType.kBrushed)
        self.left2 = SparkMax(2, SparkMax.MotorType.kBrushed)
        self.right1 = SparkMax(3, SparkMax.MotorType.kBrushed)
        self.right2 = SparkMax(4, SparkMax.MotorType.kBrushed)


        cfg_left1 = SparkMaxConfig()
        self.left1.configure(cfg_left1, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)

        cfg_left2 = SparkMaxConfig()
        cfg_left2.follow(self.left1, False)
        self.left2.configure(cfg_left2, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)

        cfg_right1 = SparkMaxConfig()
        cfg_right1.inverted(True)
        self.right1.configure(cfg_right1, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)

        cfg_right2 = SparkMaxConfig()
        cfg_right2.follow(self.right1, False)
        self.right2.configure(cfg_right2, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)

        # 建立差速驅動物件



