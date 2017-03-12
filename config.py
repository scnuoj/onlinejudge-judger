from env import env


class ConfigManager(object):

    judge_redis = {
        "host": env("JUDGE_REDIS_HOST", str, "127.0.0.1"),
        "port": env("JUDGE_REDIS_PORT", int, 6379),
        "db": env("JUDGE_REDIS_DB", int, 0),
        "password": env("JUDGE_REDIS_PASSWORD", str, ""),
        "namespace": env("JUDGE_REDIS_NAMESPACE", str, "JUDGE")
    }

    result_redis = {
        "host": env("RESULT_REDIS_HOST", str, "127.0.0.1"),
        "port": env("RESULT_REDIS_PORT", int, 6379),
        "db": env("RESULT_REDIS_DB", int, 0),
        "password": env("RESULT_REDIS_PASSWORD", str, ""),
        "namespace": env("RESULT_REDIS_NAMESPACE", str, "RESULT")
    }

    content_mysql = {
        "host": env("MYSQL_HOST", str, "127.0.0.1"),
        "port": env("MYSQL_PORT", int, 3306),
        "user": env("MYSQL_USER", str, ""),
        "password": env("MYSQL_PASSWORD", str, ""),
        "database": env("MYSQL_DATABASE", str, "judge")
    }

    thread_num = env("THREAD_NUM", int, 5)
