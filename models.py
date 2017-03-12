from peewee import *
from pprint import  pprint


database_proxy = Proxy()


class Problem(Model):

    id = PrimaryKeyField()
    title = CharField()
    description = TextField()
    type = CharField()
    input = TextField()
    output = TextField()
    sample_input = CharField()
    sample_output = CharField()
    input_data = TextField()
    output_data = TextField()
    submit_count = IntegerField()
    pass_count = IntegerField()
    user_id = CharField()
    max_cpu_time = IntegerField()
    max_real_time = IntegerField()
    max_memory = IntegerField()
    max_process_number = IntegerField()
    max_output_size = IntegerField()

    class Meta:
        db_table = 'problems'
        database = database_proxy


class Submission(Model):
    id = CharField(primary_key=True)
    problem_id = IntegerField()
    user_id = UUIDField()
    code = TextField()
    type = CharField()

    cpu_time = IntegerField()
    real_time = IntegerField()
    signal = IntegerField()
    memory = IntegerField()
    exit_code = IntegerField()
    result = IntegerField()
    error = IntegerField()

    class Meta:
        db_table = 'submissions'
        database = database_proxy
