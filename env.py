import os


class EnvException(Exception):
    pass


def env(name, env_type, default):
    ret = os.environ.get(name, default=default)

    try:
        return env_type(ret)
    except:
        raise EnvException("Error in {} which should be {} type, but {} sent".format(name, str(env_type), type(name)))
