# onlinejudge-judger

The backend judger for online judge written in Python.

**NOTICE: this project is still prototype**
**PLEASE MAKE SURE WHAT HAPPEN ABOUT ANY STEP YOU DO**


## Deploy Environment

 - Python 2.7 only
 - Redis
 - Mysql

## Environment Variables

### Judge Queue Redis
the variables for judge queue redis, where store submissions which need judging.

 - `JUDGE_REDIS_HOST` should be `str` type, the default value of which is `127.0.0.1`
 - `JUDGE_REDIS_PORT` should be `int` type, the default value of which is `6379`
 - `JUDGE_REDIS_DB` should be `int` type, the default value of which is `0`
 - `JUDGE_REDIS_PASSWORD` should be `str` type, the default value of which is ``
 - `JUDGE_REDIS_NAMESPACE` should be `str` type, the default value of which is `JUDGE`

### Result Queue Redis
the variables for result queue redis, where store the message about judged submissions sent back to frontend.

 - `RESULT_REDIS_HOST` should be `str` type, the default value of which is `127.0.0.1`
 - `RESULT_REDIS_PORT` should be `int` type, the default value of which is `6379`
 - `RESULT_REDIS_DB` should be `int` type, the default value of which is `0`
 - `RESULT_REDIS_PASSWORD` should be `str` type, the default value of which is ``
 - `RESULT_REDIS_NAMESPACE` should be `str` type, the default value of which is `RESULT`

### MySQL
the variable for MySQl, which store the informations of submissions and problems.

 - `MYSQL_HOST` should be `str` type, the default value of which is `127.0.0.1`
 - `MYSQL_PORT` should be `int` type, the default value of which is `3306`
 - `MYSQL_USER` should be `str` type, the default value of which is ``
 - `MYSQL_PASSWORD` should be `str` type, the default value of which is ``
 - `MYSQL_DATABASE` should be `str` type, the default value of which is `judge`

### Multiple Thread
the number of sub thread.

 - `THREAD_NUM` should be `int` type, the default value of which is `5`
