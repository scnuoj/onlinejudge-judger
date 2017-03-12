from config import ConfigManager
from task import TaskManager
from models import MySQLDatabase, database_proxy

my_config = ConfigManager()

database = MySQLDatabase(**my_config.content_mysql)
database_proxy.initialize(database)

manager = TaskManager(config=my_config)

if __name__ == "__main__":
    manager.run()
