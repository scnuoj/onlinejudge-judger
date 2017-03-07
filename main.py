from config import ConfigManager
from task import TaskManager
from models import MysqlConnection


my_config = ConfigManager()

MysqlConnection().connect(**my_config.content_mysql)


manager = TaskManager(config=my_config)

if __name__ == "__main__":
    manager.run()
