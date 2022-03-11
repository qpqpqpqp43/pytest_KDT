import os
# from woniusales_project.pytest_kdt_ui.common.read_config import read_configini
# print()
os.system('pytest')
import subprocess
subprocess.run(f"allure generate report/allure_result -o report/allure_html --clean",shell=True,universal_newlines=True)
