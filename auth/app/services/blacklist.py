import redis


class BlacklistService:
    redis = redis.Redis(host="localhost", port=6379, decode_responses=True)
    blacklist_name = "token_blacklist"

    @classmethod
    def add(cls, token) -> bool:
        num_added = cls.redis.sadd(cls.blacklist_name, token)
        return num_added == 1

    @classmethod
    def is_token_blacklisted(cls, token) -> bool:
        return cls.redis.sismember(cls.blacklist_name, token)
