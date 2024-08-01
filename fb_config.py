# 配置文件模块
# 负责创建、修改和读取配置文件，外加一个输出

from configparser import ConfigParser

config = ConfigParser() # 定义全局配置读写
config.read("config.ini") # 打开配置文件

# 程序输出日志
def debug_output(text:str):
    from main import complex_log
    if complex_log:
        print("[INFO]",text)
    pass

# 配置文件Section无中生有
def config_section_exist(section:str):
    global config
    if config.has_section(section) == False:
        config.add_section(section)
        debug_output(f"配置节 {section} 添加成功")
    return()

# 配置文件读取函数
def config_get(section:str, option:str, default_value:str, save_if_none:bool = True):
    global config # 引入全局配置变量
    if config.has_option(section,option) == False: # 判断是否存在
        config_section_exist(section) # Section补全
        config.set(section,option,default_value) # 不存在则创建
        debug_output(f"配置 {section} {option} 设置缺省: {default_value}")
        if save_if_none:
            config_save()
        return(default_value) # 返回缺省值
    else: # 存在
        value = config.get(section,option) # 读取值
        debug_output(f"配置 {section} {option} 读取成功: {value}")
        return(value) # 返回读取值

# 配置文件设置函数
def config_set(section:str, option:str, value:str):
    global config # 引入全局配置变量
    config_section_exist(section) # Section补全
    config.set(section,option,value) # 设置值
    debug_output(f"配置 {section} {option} 设置成功: {value}")
    return()

# 配置文件保存函数
def config_save():
    global config # 引入全局配置变量
    with open("config.ini","w") as f:
        config.write(f)
        debug_output(f"配置文件已保存")
    return
