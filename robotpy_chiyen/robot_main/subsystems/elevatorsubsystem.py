
import commands2
import wpilib
from rev import SparkMax
from rev import SparkMaxConfig
from wpilib import Encoder

class ElevatorSubsystem(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.motor = SparkMax(14, SparkMax.MotorType.kBrushless)
        self.motorsub = SparkMax(15, SparkMax.MotorType.kBrushless)

        self.encoder = self.motor.getEncoder()
        self.closedLoopController = self.motor.getClosedLoopController()



        pid = wpilib.PIDController(0.1, 0, 0)
        self.pid_p = 0.1
        self.prev_a = False
        self.prev_b = False
        self.setpoint = 0

        self.min_height = 0
        self.max_height = 110

    def setHeight(self, height):
        # 軟限位檢查
        height = max(self.min_height, min(self.max_height, height))
        self.setpoint = height

    def periodic(self):
        # 軟限位保護
        pos = self.encoder.getDistance()
        if pos <= self.min_height and self.setpoint < pos:
            self.motor.set(0)
        elif pos >= self.max_height and self.setpoint > pos:
            self.motor.set(0)
        else:
            output = self.pid.calculate(pos, self.setpoint)
            self.motor.set(output)

