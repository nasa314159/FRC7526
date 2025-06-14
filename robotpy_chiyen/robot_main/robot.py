# TODO: insert robot code here
import commands2
from robotpy_chiyen.robot_main.robotcontainer import RobotContainer  # 匯入 RobotContainer 類別

# 定義機器人主類別，繼承自 commands2.TimedCommandRobot
class MyRobot(commands2.TimedCommandRobot):
    # 機器人初始化方法
    def robotInit(self):
        # 創建 RobotContainer 的實例，管理子系統、指令和控制器
        self.container = RobotContainer() 

    def autonomousInit(self):
        self.container.timer.restart()

    def autonomousPeriodic(self):
        self.container.drive.autonomousRoutine(self.container.timer)


    def robotPeriodic(self):
        # 指令排程器：會自動執行 commands 的 execute()
        commands2.CommandScheduler.getInstance().run()
