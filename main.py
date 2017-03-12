from config import ConfigManager
from task import TaskManager
from models import MySQLDatabase, database_proxy
from env import env
my_config = ConfigManager()
my_config.judge_redis = {
        "host": env("JUDGE_REDIS_HOST", str, "cloud.ruiming.me"),
        "port": env("JUDGE_REDIS_PORT", int, 12758),
        "db": env("JUDGE_REDIS_DB", int, 1),
        "password": env("JUDGE_REDIS_PASSWORD", str, "NQUZatQ7GM8fzv0ltlQboS3gedz0HlCG"),
        "namespace": env("JUDGE_REDIS_NAMESPACE", str, "JUDGER")
    }
my_config.result_redis = {
        "host": env("RESULT_REDIS_HOST", str, "cloud.ruiming.me"),
        "port": env("RESULT_REDIS_PORT", int, 12758),
        "db": env("RESULT_REDIS_DB", int, 1),
        "password": env("RESULT_REDIS_PASSWORD", str, "NQUZatQ7GM8fzv0ltlQboS3gedz0HlCG"),
        "namespace": env("RESULT_REDIS_NAMESPACE", str, "RESULT")
}
my_config.content_mysql = {
        "host": env("MYSQL_HOST", str, "cloud.ruiming.me"),
        "port": env("MYSQL_PORT", int, 6612),
        "user": env("MYSQL_USER", str, "scnuoj"),
        "password": env("MYSQL_PASSWORD", str, "ntsuv2o7x8naq7"),
        "database": env("MYSQL_DATABASE", str, "onlinejudge")
    }
my_config.thread_num = env("THREAD_NUM", int, 5)
database = MySQLDatabase(**my_config.content_mysql)

database_proxy.initialize(database)
manager = TaskManager(config=my_config)

if __name__ == "__main__":
    manager.run()
