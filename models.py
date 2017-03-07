from peewee import *


class Singleton(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls, *args, **kwargs)
        return Singleton.__instance


class MysqlConnection(Singleton):
    connection = None

    def connect(self, *args, **kwargs):
        self.connection = MySQLDatabase(*args, **kwargs)


class BaseModel(Model):
    database = MysqlConnection().connection


class Problem(BaseModel):

    id = PrimaryKeyField()
    title = CharField()
    description = TextField()
    type = CharField()
    input = TextField()
    output = TextField()
    sampleInput = CharField()
    sampleOutput = CharField()
    inputData = TextField()
    outputData = TextField()
    submitCount = IntegerField()
    takeCount = IntegerField()
    userId = UUIDField()


class Submission(BaseModel):
    id = UUIDField(primary_key=True)
    problemId = ForeignKeyField(Problem, related_name="submissions")
    userId = UUIDField()
    code = TextField()
    type = CharField()

