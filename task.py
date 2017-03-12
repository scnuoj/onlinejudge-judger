from simple_queue import RedisQueue, LocalQueue
from copy import deepcopy
from config import ConfigManager
import threading
from models import Problem, Submission
import os
from json import loads
from time import sleep


class Task(object):

    def __init__(self, task_id):
        self.task_id = task_id

    def __load_problem_information(self):
        """
        load problem limit information
        """

        self.__limit = {
            "max_cpu_time": self.__problem.max_cpu_time,
            "max_real_time": self.__problem.max_real_time,
            "max_memory": self.__problem.max_memory,
            "max_process_number": self.__problem.max_process_number,
            "max_output_size": self.__problem.max_output_size,
        }

    def judge(self):

        return self.__judge()

    def __write_judge_file(self):
        """
        write submission file, sample input file, sample output file to {self.task_id} path
        """

        os.mkdir(self.task_id)
        with open("{}/{}".format(self.task_id, "user_judge_file"), "w") as f:
            f.write(self.__submission.code)
        with open("{}/{}".format(self.task_id, "sample_input"), "w") as f:
            f.write(self.__problem.sample_input)
        with open("{}/{}".format(self.task_id, "sample_output"), "w") as f:
            f.write(self.__problem.sample_output)

    def __judge(self):

        try:
            self.__submission = Submission.get(id=self.task_id)
            self.__problem = Problem.get(id=self.__submission.problem_id)

        except:
            return None

        self.__load_problem_information()
        self.__write_judge_file()

        # _judger.run()

        sleep(10)
        self.__clean()

        return True

    def __clean(self):

        """
        remove submission file
        """

        submission_dir = os.listdir(self.task_id)
        for file in submission_dir:
            os.remove("{}/{}".format(self.task_id, file))
        os.rmdir(self.task_id)


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

        self.__sub_thread_loop = True

    def __subprocess(self):

        while self.__sub_thread_loop:
            task = self.__local_queue.get()
            task_judger = Task(task)
            task_ret = task_judger.judge()

            if task_ret:
                self.__result_queue.put("{} OK".format(task))
            else:
                self.__result_queue.put("{} ERROR".format(task))

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
                task = loads(self.__judge_queue.get())
                self.__local_queue.put(task['payload']['submissionId'])
                print("get task {}".format(task['payload']['submissionId']))
        except KeyboardInterrupt:
            print("Waiting Jobs in Sub Thread Done ....")
            for one_thread in self.__threadpool:
                one_thread.join()
            print("All Job Done")
