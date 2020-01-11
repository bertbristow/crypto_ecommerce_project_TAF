Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@bertbristow 
13
122215626626cdllp/Test
 Code Issues 1 Pull requests 2 Actions Projects 0 Wiki Security Insights
Test/Test_framework/test_baidu.py / 
@626626cdllp 626626cdllp change logging to python-logging
55f053d on 2 Aug 2019
54 lines (47 sloc)  1.98 KB
  
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more

You're using code navigation to jump to definitions or references.
Learn more or give us feedback
import os
import time
import unittest  # 单元测试模块
from selenium import webdriver  # 引入浏览器驱动
from selenium.webdriver.common.by import By  # 引入xpath查找模块
from .utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH  # 引入配置
from .utils.log import logger # 引入日志模块
from .utils.file_reader import ExcelReader  # 引入xls读取模块
from .utils.HTMLTestRunner import HTMLTestRunner
from .utils.mail import Email
from .test.page.baidu_result_page import BaiDuMainPage, BaiDuResultPage

class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        pass

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__ == '__main__':
    # unittest.main()

    report = REPORT_PATH + '\\report.html'
    print(report)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='栾鹏全栈', description='修改html报告')
        runner.run(TestBaiDu('test_search'))

    # e = Email(title='百度搜索测试报告',
    #           message='这是今天的测试报告，请查收！',
    #           receiver='...',
    #           server='...',
    #           sender='...',
    #           password='...',
    #           path=report
    #           )
    # e.send()
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
