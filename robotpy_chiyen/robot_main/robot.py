# TODO: insert robot code here
import commands2
from robotpy_chiyen.robot_main.robotcontainer import RobotContainer  # 匯入 RobotContainer 類別

# 定義機器人主類別，繼承自 commands2.TimedCommandRobot
class MyRobot(commands2.TimedCommandRobot):
    # 機器人初始化方法
    def robotInit(self):
        # 創建 RobotContainer 的實例，管理子系統、指令和控制器
        self.container = RobotContainer() 
