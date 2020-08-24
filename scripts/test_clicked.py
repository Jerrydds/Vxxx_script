import random
import pytest
import requests, json, time, datetime
from multiprocessing.dummy import Pool
import threading

'''
# 定义循环5次,生成0~9随机数
def random_password():
    password = ""
    for i in range(5):
        password += str(random.randint(0, 9))
    return password

# 定义循环10000次,生成5位随机数拼接到列表中
def password_list():
    passwords = list()
    for i in range(1):
        passwords.append(random_password())
    return passwords
'''

# 定义循环10000次,生成5位随机数拼接到列表中
def password_list():
    nums = list()
    for i in range(3):
      nums.append(i)
    return nums


# def yqids_list():
#     op_ql = OperationMssql()
#     return op_ql.search_all("SELECT TOP 1 FYQProductId FROM TYQProduct WHERE FYQMerchantLibraryId = '112229'")


#  产品点击事件
'''
class TestClicked:
  
    def setup(self):
        self.url = 'http://root:17track@192.168.1.216:9250/deals.statistics.events-2020-06/_doc/'

        self.data = {
          "ID": "ClickES_Click-3838128107900185903_66583221267708" + str(random.randint(10000,99999)),
          "EventInfo": {
            "EventType": 12,
            "EventTime": (datetime.datetime.utcnow() - datetime.timedelta(days=4)).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "CreateTime": (datetime.datetime.utcnow() - datetime.timedelta(days=4)).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
          },
          "ItemInfo": {
            "ItemID": "01704EEB8AE4821659271D1D75C72C2A",
            "DealDataType": 3,
            "MerchantID": "None"
          },
          "UserInfo": {
            "UserID": "6524817783430316033",
            "DealsSite": 0,
            "UserCountry": 0,
            "Source": "app",
            "DeviceID": None,
            "UserLanguage": None
          },
          "ModuleInfo": {
            "FrontendModules": [],
            "BackendModules": [
              "CommonProduct"
            ]
          }
        }

'''


# 广告商点击事件

'''
class TestClicked:


    def setup(self):
        self.url = 'http://root:17track@192.168.1.216:9250/deals.statistics.events-2020-06/_doc/'

        self.data = {
          "ID": "ClickES_Click-20200509-1" + str(random.randint(10000,99999)),
          "EventInfo": {
            "EventType": 12,
            "EventTime": (datetime.datetime.utcnow() - datetime.timedelta(days=4)).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "CreateTime": (datetime.datetime.utcnow() - datetime.timedelta(days=4)).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
          },
          "ItemInfo": {
            "ItemID": "111711",
            "DealDataType": 1,
            "MerchantID": "None"
          },
          "UserInfo": {
            "UserID": "6524817783430316033",
            "DealsSite": 0,
            "UserCountry": 0,
            "Source": "app",
            "DeviceID": None,
            "UserLanguage": None
          },
          "ModuleInfo": {
            "FrontendModules": [
              "App搜索结果页-广告商模块"
            ],
            "BackendModules": [
              "Search"
            ]
          }
        }
        
'''

#  广告点击事件

class TestClicked:

    def setup(self):
        self.url = 'http://root:17track@192.168.1.216:9250/deals.statistics.events-2020-06/_doc/'

        self.data = {
          "ID": "ClickES_Click-0_66583221267708" + str(random.randint(10000,99999)),
          "EventInfo": {
            "EventType": 12,
            "EventTime": (datetime.datetime.utcnow() - datetime.timedelta(days=4)).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "CreateTime": (datetime.datetime.utcnow() - datetime.timedelta(days=4)).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
          },
          "ItemInfo": {
            "ItemID": "3-275938",
            "DealDataType": 2,
            "MerchantID": "112229"
          },
          "UserInfo": {
            "UserID": "6524817783430316033",
            "DealsSite": 0,
            "UserCountry": 0,
            "Source": "app",
            "DeviceID": None,
            "UserLanguage": None
          },
          "ModuleInfo": {
            "FrontendModules": [],
            "BackendModules": [
              "CommonLink"
            ]
          }
        }


    # @pytest.mark.parametrize("args", analyze_with_file_name("total", "test_total"))
    # @pytest.mark.parametrize("args", yqids_list())
    @pytest.mark.parametrize("password", password_list())
    def test_total_001(self, password):
        requests.post(url=self.url , json=self.data).json()

    @pytest.mark.parametrize("password", password_list())
    def test_total_002(self, password):
        requests.post(url=self.url , json=self.data).json()

    @pytest.mark.parametrize("password", password_list())
    def test_total_003(self, password):
        requests.post(url=self.url , json=self.data).json()

    @pytest.mark.parametrize("password", password_list())
    def test_total_004(self, password):
        requests.post(url=self.url , json=self.data).json()

    @pytest.mark.parametrize("password", password_list())
    def test_total_005(self, password):
        requests.post(url=self.url , json=self.data).json()

    @pytest.mark.parametrize("password", password_list())
    def test_total_006(self, password):
        requests.post(url=self.url , json=self.data).json()

    @pytest.mark.parametrize("password", password_list())
    def test_total_007(self, password):
        requests.post(url=self.url , json=self.data).json()

    @pytest.mark.parametrize("password", password_list())
    def test_total_008(self, password):
        requests.post(url=self.url , json=self.data).json()

    @pytest.mark.parametrize("password", password_list())
    def test_total_009(self, password):
        requests.post(url=self.url , json=self.data).json()

    @pytest.mark.parametrize("password", password_list())
    def test_total_010(self, password):
        requests.post(url=self.url , json=self.data).json()



if __name__ == '__main__':
    pytest.main(['-s', __file__, '--workers=1','--tests-per-worker=10'])  