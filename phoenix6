import wpilib
import wpilib.drive
import phoenix6
import phoenix6.hardware as hw
from phoenix6 import configs

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.left1=hw.TalonFX(1)
        self.left2=hw.TalonFX(2)
        self.left3=hw.TalonFX(3)
        self.left4=hw.TalonFX(4)
        self.left=wpilib.MotorControllerGroup(self.left1,self.left2,self.left3,self.left4)

        self.right1=hw.TalonFX(5)
        self.right2=hw.TalonFX(6)
        self.right3=hw.TalonFX(7)
        self.right4=hw.TalonFX(8)
        self.right=wpilib.MotorControllerGroup(self.right1,self.right2,self.right3,self.right4)

        self.robotDrive=wpilib.drive.DifferentialDrive(self.left,self.right)
        self.controller = wpilib.XboxController(0)
        self.time=wpilib.Timer #計時器

        return super().robotInit()
    def autonomousInit(self):#run once each time the robot enters autonomous mode
        self.time.restart()
    def autonomousPeriodic(self):#called periodically during autonomous
        if self.time.get()<2.0:
            self.robotDrive.arcadeDrive(xSpeed=0.5,zRotation=0,squareInputs=False)
        else:
            self.robotDrive.stopMotor()
    def teleopInit(self):#called once each time the robot enters teleoperated mode
        
    def teleopPeriodic(self):#called periodically during teleoperated mode
        self.robotDrive.arcadeDrive(
            self.controller.getLeftY(),self.controller.getRightX()
        )
    
if __name__=="main":
    import wpilib
    wpilib.run(Robot)
