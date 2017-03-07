import redis
from threading import Lock
from time import sleep


class RedisQueue(object):

    def __init__(self, namespace, **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""
        self.__db= redis.Redis(**redis_kwargs)
        self.namespace = namespace

    def qsize(self):
        """Return the approximate size of the queue."""
        return self.__db.llen(self.namespace)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.namespace, item)

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue.

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.__db.blpop(self.namespace, timeout=timeout)
        else:
            item = self.__db.lpop(self.namespace)

        if item:
            item = item[1]
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        return self.get(False)


class LocalQueue(object):
    """
    Simple Thread Safety Queue
    """

    def __init__(self, lock=None, len_limit=10):
        self.__lock = lock or Lock()
        self.__len_limit = len_limit
        self.__queue = []

    def put(self, item):
        insert = Flase
        while insert is False:
            with self.__lock:
                if len(self.__queue) < self.__len_limit:
                    self.__queue.append(item)
                    insert = True

            sleep(0.5)

    def get(self):

        with self.__lock:
            return self.__queue.pop()
