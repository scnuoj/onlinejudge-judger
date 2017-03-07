class ConfigManager(object):

    judge_redis = {
        "host": "127.0.0.1",
        "port": 6379,
        "db": 0,
        "password": None,
        "namespace": "JUDGE"
    }

    result_redis = {
        "host": "127.0.0.1",
        "port": 6379,
        "db": 0,
        "password": None,
        "namespace": "RESULT"
    }

    content_mysql = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "",
        "password": "",
        "database": "judge",
    }

    thread_num = 5
