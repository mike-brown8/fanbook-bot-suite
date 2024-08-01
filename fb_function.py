# Fanbook方法调用模块
# 负责API方法调用，对fb_basic的返回数据做处理

from fb_basic import post_request,post_request_form
import json

# 获取机器人基本信息
def fb_getMe() -> bool:
    """获取机器人基本信息，并打印到控制台。
    成功返回True
    失败返回False"""
    data = post_request("/getMe")
    if data == None: return(False)
    print("机器人名字:",data["first_name"])
    print("机器人ID:",data["username"])
    print("所有者名字:",data["last_name"])
    return(True)