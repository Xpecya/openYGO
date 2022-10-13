import yaml
import logger


def read_config():
    # 打开配置文件并读取配置文件内容
    file = open("config.yml", "r", encoding="UTF-8")
    file_data = file.read()
    file.close()
    config_data = yaml.safe_load(file_data)
    # 开始进行配置
    do_config(config_data)


def do_config(config_data):
    # 日志组建初始化
    logger.init(config_data)
    config_logger = logger.get_logger("config")
    config_logger.debug("日志组件配置完成! log config: %s", config_data["log"])

    config_logger.info("开始配置YGOpro")
    config_ygo_pro(config_data)


# todo 研究YGOpro咋玩儿的
def config_ygo_pro(config_data):
    pass
