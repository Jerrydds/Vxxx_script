import random
import pytest, json, requests
from base.connect_db import OperationMssql

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
def yqids_lists(num):
    op_ql = OperationMssql()
    return op_ql.search_all("select FPrimaryKeyId from TYQLink order by FPrimaryKeyId offset " + str(num)+ " rows FETCH NEXT 1000 rows only")

def base_activate(yqid):
        
    url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

    data = {
        "id": "3838128107900185903_66593211083047" + str(random.randint(10000,99999)),
        "BaseClickInfo": {
        "BaseInfo": {
            "ClickDataId": yqid,
            "DataType": 2,
            "LangCode": "zh-CN",
            "SystemType": None,
            "SourceType": [
            "APP"
            ],
            "CountryCode": 0,
            "CreateDate": "2020-04-23T13:"+ str(random.randint(10,59)) + ":53.3630855Z",
            "ModifyDate": "2020-04-23T21:40:53.3630855+08:00",
            "Status": 0
        },
        "UserInfo": {
            "UserCountryCode": 112,
            "AppVersion": 0,
            "UserLangCode": "en",
            "Sid": "3838128107900185903_66593211083047" + str(random.randint(10000,99999)),
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
        "Name": "UP TO 30% OFF PHONE PARTS & TOOLS",
        "CreateDate": "0001-01-01T00:00:00",
        "EndDate": "0001-01-04T23:32:58.56",
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

    return requests.post(url=url , json=data).json()
   

class TestLtotal:

    @pytest.mark.parametrize("yqid",yqids_lists(0))
    def test_total_001(self, yqid):
    	base_activate(yqid)

    @pytest.mark.parametrize("yqid",yqids_lists(1000))
    def test_total_002(self, yqid):
    	base_activate(yqid)

    @pytest.mark.parametrize("yqid",yqids_lists(2000))
    def test_total_003(self, yqid):
    	base_activate(yqid)

    @pytest.mark.parametrize("yqid",yqids_lists(3000))
    def test_total_004(self, yqid):
    	base_activate(yqid)

    @pytest.mark.parametrize("yqid",yqids_lists(4000))
    def test_total_005(self, yqid):
    	base_activate(yqid)

    @pytest.mark.parametrize("yqid",yqids_lists(5000))
    def test_total_006(self, yqid):
        base_activate(yqid)
 
    @pytest.mark.parametrize("yqid",yqids_lists(6000))
    def test_total_007(self, yqid):
     	base_activate(yqid)

    @pytest.mark.parametrize("yqid",yqids_lists(7000))
    def test_total_008(self, yqid):
    	base_activate(yqid)

    @pytest.mark.parametrize("yqid",yqids_lists(8000))
    def test_total_009(self, yqid):
    	base_activate(yqid)

    @pytest.mark.parametrize("yqid",yqids_lists(9000))
    def test_total_010(self, yqid):
    	base_activate(yqid)









if __name__ == '__main__':
    pytest.main(['-s', __file__, '--workers=1','--tests-per-worker=2'])  