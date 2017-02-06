from ..conf.config import cfg


def main():
    if cfg.redis_host == '-':
        print(" * Without Redis we are old but gold")
    else:
        import redis
        redis.StrictRedis(host=cfg.redis_host, port=int(cfg.redis_port))
        print(" * Redis at %s:%d" % (cfg.redis_host, int(cfg.redis_port)))
