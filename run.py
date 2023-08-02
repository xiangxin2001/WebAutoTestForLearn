import pytest
import subprocess  # 导入进程模块

pytest.main()
cmd = "allure generate report-xml -o report --clean"
subprocess.call(cmd, shell=True)  # 通过进程调用命令生成allure报告
