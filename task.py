from simple_queue import RedisQueue, LocalQueue
from copy import deepcopy
from config import ConfigManager
from pprint import pprint
import threading

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
        self.__judge_queue = RedisQueue(namespace=judge_redis_namespace, **judge_redis_config)

        result_redis_config = deepcopy(self.config.result_redis)
        result_redis_namespace = result_redis_config.pop("namespace")
        self.__result_queue = RedisQueue(namespace=result_redis_namespace, **result_redis_config)

        self.__local_queue = LocalQueue()

        self.__threadpool = []

    def __subprocess(self):

        pass

    def __thread_generator(self):
        self.__threadpool.append(threading.Thread(target=self.__subprocess))

    def run(self):
        print("Sub Thread generating ....")
        self.__thread_generator()
        print("Starting Sub Thread ....")
        for one_thread in self.__threadpool:
            one_thread.start()
        print("Start Listening Judge Queue ....")
        try:
            while True:
                task = self.__judge_queue.get()
                pprint(task)

        except KeyboardInterrupt:
            print("Waiting Jobs in Sub Thread Done ....")
            for one_thread in self.__threadpool:
                one_thread.join()
            print("All Job Done")
