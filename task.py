from redis_queue import RedisQueue
from copy import deepcopy
from config import ConfigManager
from pprint import pprint


class Task(object):

    def __init__(self, task_id, judge_file_content):
        self.task_id = task_id
        self.judge_file_content = judge_file_content

    def __load_task_information(self):

        pass

    def judge(self):

        pass

    def __write_judge_file(self):

        pass

    def __judge(self):

        pass

    def __load_result(self):

        pass


class TaskManager(object):

    def __init__(self, config=None):

        if config:
            self.config = config
        else:
            self.config = ConfigManager()

        judge_redis_config = deepcopy(self.config.judge_redis)
        judge_redis_namespace = judge_redis_config.pop("namespace")
        self.judge_queue = RedisQueue(namespace=judge_redis_namespace, **judge_redis_config)

        result_redis_config = deepcopy(self.config.result_redis)
        result_redis_namespace = result_redis_config.pop("namespace")
        self.result_queue = RedisQueue(namespace=result_redis_namespace, **result_redis_config)

    def run(self):
        print("start listening....")
        try:
            while True:
                task = self.judge_queue.get()
                pprint(task)

        except KeyboardInterrupt:
            print("stop listening....")
