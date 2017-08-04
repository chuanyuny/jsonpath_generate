# -*-coding:utf-8 -*-

ex_data={
    "_id":"58eb59e61cfb1e2eca23f222",
    "resCode":"0000",
    "resMsg":"SUCCESS",
    "data":[
        {
            "reason":"0",
            "match":[
                "national_id",
                "name",
                "email"
            ],
            "create_date_type":"6",
            "amount_type":3,
            "over_due_type":0,
            "legal_status":0
        },
        {
            "reason":3,
            "match":[
                "national_id",
                "name"
            ],
            "create_date_type":0,
            "amount_type":0,
            "over_due_type":0,
            "legal_status":0
        }
    ],
    "name":"黄潮炎",
    "idCard":"440524197307166614",
    "createDate":"1491818982193",
    "flag_view":"1"
}

ex_data2=[
["ll","oo"],

        {
            "reason":"0",
            "match":[
                "national_id",
                "name",
                "email"
            ],
            "create_date_type":"6",
            "amount_type":"3",
            "over_due_type":"3",
            "legal_status":"3"
        },
        {
            "reason":"3",
            "match":[
                "national_id",
                "name"
            ],
            "create_date_type":"3",
            "amount_type":"3",
            "over_due_type":"3",
            "legal_status":"3"
        }
    ]
  

def data_handle(data,jsonpath):   # 第一次调用这个函数的时候，jsonpath 设为 $. 或$
	templist=[]  #把为字典的value 都放在这里。  这是一个  [{...,jsonpath:jsonpath}]
	if isinstance(data,dict):   #  第一次jsonpath为 $.
		# print("111")
		for key in data:
			if isinstance(data[key],str) or isinstance(data[key],int):
				# print("22")
				jsonpath1=jsonpath+key
				if key!="jsonpath":
					print(jsonpath1)  #这是本次调用该函数可以直接计算出来jsonpath。 这个地方只输出，也可以写到一起txt中
				
			elif isinstance(data[key],dict):
				dict1={}
				dict1=data[key]
				jsonpath1=jsonpath+key+'.'
				dict1['jsonpath']=jsonpath1
				templist.append(dict1)
			elif isinstance(data[key],list):
				jsonpath1=jsonpath+key
				data_handle(data[key],jsonpath1)
	elif isinstance(data,list):   #第一次jsonpath为  $
		for each in data:
			if isinstance(each,dict):
				jsonpath1=jsonpath+'['+str(data.index(each))+']'+'.'
				dic2={}
				dic2=each
				dic2['jsonpath']=jsonpath1
				templist.append(dic2)
			elif isinstance(each,list):
				jsonpath1=jsonpath+"["+str(data.index(each))+"]"
				data_handle(each,jsonpath1)
			elif isinstance(each,str) or isinstance(each,int):
				jsonpath1=jsonpath+'['+str(data.index(each))+']'
				if each!="jsonpath":
					print(jsonpath1)
	for each in templist:
		data_handle(each,each['jsonpath'])

data_handle(ex_data,"$.")

