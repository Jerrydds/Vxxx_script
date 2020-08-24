import random
import pytest,json,requests
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
    return op_ql.search_all("select FYQProductId from TYQProduct order by FYQProductId offset "+ str(num) + " rows FETCH NEXT 1000 rows only")

def base_activate(yqid):

    url = 'http://root:17track@192.168.1.216:9250/deals.statistics.click/_doc/'

    data = {
        "Id": "3838128107900185903_66583221267708" + str(random.randint(10000,99999)),
        "BaseClickInfo": {
            "BaseInfo": {
            "ClickDataId": yqid,
            "DataType": 3,
            "LangCode": "en",
            "SystemType": None,
            "SourceType": [
                "APP"
            ],
            "CountryCode": 0,
            "CreateDate": "2020-04-23T12:"+ str(random.randint(10,59)) + ":53.3630855Z",
            "ModifyDate": "2020-04-23T20:40:53.3630855+08:00",
            "Status": 0
            },
            "UserInfo": {
            "UserCountryCode": 112,
            "AppVersion": 0,
            "UserLangCode": "en",
            "Sid": "3838128107900185903_66583221267708" + str(random.randint(10000,99999)),
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
    return requests.post(url=url , json=data).json()

    # @pytest.mark.parametrize("args", analyze_with_file_name("total", "test_total"))
    # @pytest.mark.parametrize("args", yqids_list())
    # @pytest.mark.parametrize("password", password_list())

class TestPtotal:

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

