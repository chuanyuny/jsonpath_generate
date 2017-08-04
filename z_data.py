# -*-coding:utf-8 -*-

ex_data={
    "_id" : "595c74ddac72760be08e3902",
    "resCode" : "0000",
    "resMsg" : "SUCCESS",
    "data" : {
        "resultFlag" : "0",
        "message" : "查询成功有数据",
        "result" : [{
            "phone" : "180XXXX13",
            "netStatus" : "0",
            "netStatusMsg" : "在网状态正常"},
             {
            "pahone" : "180XXXX13",
            "anetStatus" : "0",
            "anetStatusMsg" : "在网状态正常"}
        ]
    },
"aa": [{
            "phone" : "180XXXX13",
            "netStatus" : "0",
            "netStatusMsg" : "在网状态正常"}
        ],
    "phone" : "17744561767",
    "resStatus" : "1",
    "checkStatus" : "0",
    "resAdress" : "sjt",
    "resNum" : "PLCS1116YY006",
    "resDate" : "2017-07-05 13:09:19",
    "orderNo" : "20170705130919fc4c68c6",
    "code" : "111106",
    "idCard" : "430302197903283058",
    "accountNo" : "null",
    "phoneNum" : "17744561767",
    "userName" : "陈杨名"
}    

ex_data2=[{
            "phone" : "180XXXX13",
            "netStatus" : "0",
            "netStatusMsg" : "在网状态正常"},
             {
            "pahone" : [{"mm":"123"},"nn"],
            "anetStatus" : "0",
            "anetStatusMsg" : "在网状态正常"},
"aa",
"bb"
        ]
  

def data_handle(data,jsonpath):   # 第一次调用这个函数的时候，jsonpath 设为 $. 或$
	templist=[]  #把为字典的value 都放在这里。  这是一个  [{...,jsonpath:jsonpath}]
	if isinstance(data,dict):   #  第一次jsonpath为 $.
		# print("111")
		for key in data:
			if isinstance(data[key],str):
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
				for each in data[key]:
					if isinstance(each,dict):
						jsonpath1=jsonpath+key+'['+str(data[key].index(each))+']'+'.'
						data_handle(each,jsonpath1)
	elif isinstance(data,list):   #第一次jsonpath为  $
		for each in data:
			if isinstance(each,dict):
				jsonpath1=jsonpath+'['+str(data.index(each))+']'+'.'
				dic2={}
				dic2=each
				dic2['jsonpath']=jsonpath1
				templist.append(dic2)
			elif isinstance(each,list):
				for item in each:
					if isinstance(item,dict):
						jsonpath1=jsonpath+'['+str(data.index(each))+']'+'['+str(each.index(item))+']'+'.'
						data_handle(item,jsonpath1)
			elif isinstance(each,str):
				jsonpath1=jsonpath+'['+str(data.index(each))+']'
				if each!="jsonpath":
					print(jsonpath1)
	for each in templist:
		data_handle(each,each['jsonpath'])

data_handle(ex_data2,"$")

