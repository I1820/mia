import redis
from ..conf.config import cfg


def main():
    redis.StrictRedis(host=cfg.redis_host, port=int(cfg.redis_port))
    print(" * Redis at %s:%d" % (cfg.redis_host, int(cfg.redis_port)))
