# Fanbook请求底层模块
# 负责处理对API的直接请求，不含返回JSON处理

from fb_config import config_get,config_set,config_save,debug_output # 引入配置文件读写保存函数
import requests
import main
import json

# 判断ok或status
def ok_status(data) -> bool:
    if data == None: return(False)
    if "ok" in data:
        if data["ok"] == False: return(False)
    elif "status" in data:
        if data["status"] == False: return(False)
    return(True)

# POST请求函数，失败则返回None
def post_request(extra_url:dict = "/getMe", arguments:dict = { }, bot_token:str = config_get("base","bot_token",""), base_url:str = config_get("base","base_url","https://a1.fanbook.cn/api/bot/")):
    request_url = base_url + bot_token + extra_url
    request_data = json.dumps(arguments)
    request_header = {"Content-Type" : "application/json"}
    try:
        response = requests.post(request_url,request_data,headers=request_header)
    except requests.RequestException as e: # 判断请求错误
        print("[ERROR] POST请求错误",e.errno,e.args)
        return(None)
    if response.status_code != 200: # 判断状态码错误
        print("[ERROR] POST请求状态码错误",response.status_code)
        return(None)
    debug_output("POST请求成功")
    json_response = json.loads(response.text)
    if ok_status(json_response):
        return(json_response["result"])
    else:
        return(None)
    

# POST请求函数（x-www-form-urlencoded），失败则返回None
def post_request_form(extra_url:dict = "/", arguments:str = "", bot_token:str = config_get("base","bot_token",""), base_url:str = config_get("base","base_url","https://a1.fanbook.cn/api/bot/")):
    request_url = base_url + bot_token + extra_url
    request_header = {"Content-Type" : "application/x-www-form-urlencoded"}
    try:
        response = requests.post(request_url,arguments,headers=request_header)
    except requests.RequestException as e: # 判断请求错误
        print("[ERROR] POST请求错误",e.errno,e.args)
        return(None)
    if response.status_code != 200: # 判断状态码错误
        print("[ERROR] POST请求状态码错误",response.status_code)
        return(None)
    debug_output("POST请求成功")
    json_response = json.loads(response.text)
    if ok_status(json_response):
        return(json_response["result"])
    else:
        return(None)