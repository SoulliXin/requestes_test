import os
import sys
import unittest
base_path = os.path.abspath(os.path.dirname(__file__)).split('Run')[0]
sys.path.append(base_path)
from BeautifulReport import BeautifulReport




case_path = base_path + "/Run"
report_path = base_path + "/Report/report.html"
discover = unittest.defaultTestLoader.discover(case_path, pattern="run_case_*.py")
BeautifulReport(discover).report(filename='Aglione测试报告',description='Aglione_01模块',report_dir=report_path,theme='theme_cyan')