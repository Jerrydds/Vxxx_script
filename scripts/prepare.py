import random
import pytest,json,requests
from base.base_analyze import analyze_with_file_name
from multiprocessing.dummy import Pool



url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

data = {
        "Id": "0_6658352426770876528",
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
            "CreateDate": "2020-04-22T06:50:53.3630855Z",
            "ModifyDate": "2020-04-22T14:50:53.3630855+08:00",
            "Status": 0
            },
            "UserInfo": {
            "UserCountryCode": 0,
            "AppVersion": 0,
            "UserLangCode": None,
            "Sid": "0_6658352426770876528",
            "UserId": 0,
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
# res = requests.post(url=url , json=data).json()

# print(json.dumps(res, indent=2, sort_keys=False))


futures = list()
for x in range(10):
     futures.append(pool.apply_async(requests.post, [url], {'data': data}))
for future in futures:
    print(future.get()) # For each future, wait until the request 


'''
class TestPrepare:

    @pytest.mark.parametrize("args", analyze_with_file_name("prepare", "test_prepare_01"))
    def test_total_001(self, args):
        yqid = args["yqid"]

        url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        data = {
            "Id": "0_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": yqid,
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-23T03:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-23T11:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "0_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 0,
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
        requests.post(url=url , json=data).json()

    @pytest.mark.parametrize("args", analyze_with_file_name("prepare", "test_prepare_02"))
    def test_total_002(self, args):
        yqid = args["yqid"]

        url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        data = {
            "Id": "0_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": yqid,
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-23T03:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-23T11:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "0_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 0,
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
        requests.post(url=url , json=data).json()
    @pytest.mark.parametrize("args", analyze_with_file_name("prepare", "test_prepare_03"))
    def test_total_003(self, args):
        yqid = args["yqid"]

        url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        data = {
            "Id": "0_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": yqid,
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-23T03:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-23T11:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "0_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 0,
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
        requests.post(url=url , json=data).json()
    @pytest.mark.parametrize("args", analyze_with_file_name("prepare", "test_prepare_04"))
    def test_total_004(self, args):
        yqid = args["yqid"]

        url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        data = {
            "Id": "0_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": yqid,
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-23T03:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-23T11:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "0_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 0,
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
        requests.post(url=url , json=data).json()
    @pytest.mark.parametrize("args", analyze_with_file_name("prepare", "test_prepare_05"))
    def test_total_005(self, args):
        yqid = args["yqid"]

        url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        data = {
            "Id": "0_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": yqid,
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-23T03:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-23T11:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "0_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 0,
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
        requests.post(url=url , json=data).json()

    @pytest.mark.parametrize("args", analyze_with_file_name("prepare", "test_prepare_06"))
    def test_total_006(self, args):
        yqid = args["yqid"]

        url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        data = {
            "Id": "0_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": yqid,
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-23T03:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-23T11:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "0_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 0,
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
        requests.post(url=url , json=data).json()

    @pytest.mark.parametrize("args", analyze_with_file_name("prepare", "test_prepare_07"))
    def test_total_007(self, args):
        yqid = args["yqid"]

        url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        data = {
            "Id": "0_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": yqid,
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-23T03:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-23T11:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "0_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 0,
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
        requests.post(url=url , json=data).json()
    @pytest.mark.parametrize("args", analyze_with_file_name("prepare", "test_prepare_08"))
    def test_total_008(self, args):
        yqid = args["yqid"]

        url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        data = {
            "Id": "0_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": yqid,
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-23T03:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-23T11:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "0_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 0,
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
        requests.post(url=url , json=data).json()

    @pytest.mark.parametrize("args", analyze_with_file_name("prepare", "test_prepare_09"))
    def test_total_009(self, args):
        yqid = args["yqid"]

        url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        data = {
            "Id": "0_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": yqid,
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-23T03:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-23T11:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "0_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 0,
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
        requests.post(url=url , json=data).json()

    @pytest.mark.parametrize("args", analyze_with_file_name("prepare", "test_prepare_10"))
    def test_total_010(self, args):
        yqid = args["yqid"]

        url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        data = {
            "Id": "0_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": yqid,
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-23T03:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-23T11:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "0_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 0,
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
        requests.post(url=url , json=data).json()


    @pytest.mark.parametrize("args", analyze_with_file_name("prepare", "test_prepare_11"))
    def test_total_011(self, args):
        yqid = args["yqid"]

        url = 'http://root:17track@192.168.1.216:9200/deals.statistics.click/info/'

        data = {
            "Id": "0_66583221267708" + str(random.randint(10000,99999)),
            "BaseClickInfo": {
                "BaseInfo": {
                "ClickDataId": yqid,
                "DataType": 3,
                "LangCode": "zh-CN",
                "SystemType": None,
                "SourceType": [
                    "APP"
                ],
                "CountryCode": 0,
                "CreateDate": "2020-04-23T03:"+ str(random.randint(10,59)) + ":53.3630855Z",
                "ModifyDate": "2020-04-23T11:40:53.3630855+08:00",
                "Status": 0
                },
                "UserInfo": {
                "UserCountryCode": 0,
                "AppVersion": 0,
                "UserLangCode": None,
                "Sid": "0_66583221267708" + str(random.randint(10000,99999)),
                "UserId": 0,
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
        res = requests.post(url=url , json=data).json()

        print(json.dumps(res, indent=2, sort_keys=False))
'''