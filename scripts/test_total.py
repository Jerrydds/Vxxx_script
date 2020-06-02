import random
import pytest
import requests, json, time, datetime
from base.connect_db import OperationMssql
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

# def yqids_list():
#     op_ql = OperationMssql()
#     return op_ql.search_all("SELECT TOP 1 FYQProductId FROM TYQProduct WHERE FYQMerchantLibraryId = '112229'")
'''

# 定义循环10000次,生成5位随机数拼接到列表中
def password_list():
    nums = list()
    for i in range(1):
      nums.append(i)
    return nums


#  产品点击量
'''
    def setup(self):

        self.url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        self.data = {
            "Id": "376417286290268641G_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": "01704EEB8AE4821659271D1D75C72C2A",
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-22T08:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-22T16:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "376417286290268641G_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 6524817783430316033,
                "ShareId": 0,
                "DeviceId": None
                },
                "ComissionInfo": None,
                "ClickInfo": {
                "PageName": None,
                "ModuleList": [
                    "CommonProduct"
                ],
                "ParamList": [],
                "DisplayOrderNumber": 0
                }
            },
            "ProductClickInfo": {
                "Name": "Bojie F186000 Print head for Epson DX5 solvent printhead for Galaxy Witcolor Mimaki Mutoh",
                "CategoryList": None,
                "Price": 1004,
                "RetailPrice": 1004,
                "Discount": 0,
                "Currency": "USD"
            },
            "LinkClickInfo": None,
            "MerchantClickInfo": {
                "Name": "AliExpress",
                "IdList": [
                112229
            ]
        }
    }

'''

#  广告点击量
'''
    def setup(self):
        self.url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        self.data = {
          "id": "0_66590246475873" + str(random.randint(10000,99999)),
          "BaseClickInfo": {
            "BaseInfo": {
              "ClickDataId": "2-13472373",
              "DataType": 2,
              "LangCode": "en",
              "SystemType": None,
              "SourceType": [
                "APP"
              ],
              "CountryCode": 0,
              "CreateDate": "2020-04-23T07:"+ str(random.randint(10,59)) + ":03.3678843Z",
              "ModifyDate": "2020-04-23T15:24:03.3678843+08:00",
              "Status": 0
            },
            "UserInfo": {
              "UserCountryCode": 301,
              "AppVersion": 0,
              "UserLangCode": "en",
              "Sid": "0_66590246475873" + str(random.randint(10000,99999)),
              "UserId": 6524817783430316033,
              "ShareId": 0,
              "DeviceId": None
            },
            "ComissionInfo": None,
            "ClickInfo": {
              "PageName": None,
              "ModuleList": [
                "CommonLink"
              ],
              "ParamList": [],
              "DisplayOrderNumber": 0
            }
          },
          "ProductClickInfo": None,
          "LinkClickInfo": {
            "Name": "Up to 57% Off Bags, Shoes & Accs",
            "CreateDate": "0001-01-01T00:00:00",
            "EndDate": "0001-01-02T23:10:16.68",
            "IsPromotion": False,
            "IsShippingFree": False,
            "IsDiscount": True,
            "IsHot": False
          },
          "MerchantClickInfo": {
            "Name": "DHgate",
            "IdList": [
              141815
            ]
          }

        }
'''

#  广告商点击量

class TestTotal:


    def setup(self):
        self.url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        self.data = {
          "id": "376417286290268641G_66590337091336" + str(random.randint(10000,99999)),
          "BaseClickInfo": {
            "BaseInfo": {
              "ClickDataId": "112229",
              "DataType": 1,
              "LangCode": "en",
              "SystemType": None,
              "SourceType": [
                "APP"
              ],
              "CountryCode": 0,
              # "CreateDate": "2020-04-30T02:"+ str(random.randint(10,59)) + ":03.82066Z",
              # "ModifyDate": "2020-04-30T10:11:03.82066+08:00",
              "CreateDate": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
              "ModifyDate": (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%S.%fZ') + "+08:00",
              "Status": 0
            },
            "UserInfo": {
              "UserCountryCode": 301,
              "AppVersion": 0,
              "UserLangCode": "en",
              "Sid": "376417286290268641G_66590337091336" + str(random.randint(10000,99999)),
              "UserId": 6524817783430316033,
              "ShareId": 0,
              "DeviceId": None
            },
            "ComissionInfo": None,
            "ClickInfo": {
              "PageName": None,
              "ModuleList": None,
              "ParamList": None,
              "DisplayOrderNumber": 0
            }
          },
          "ProductClickInfo": None,
          "LinkClickInfo": None,
          "MerchantClickInfo": {
            "Name": "AliExpress",
            "IdList": [
              112229
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
        