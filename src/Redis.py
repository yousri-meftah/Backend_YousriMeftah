import redis.asyncio as redis
import json

redis_client = redis.from_url("redis://localhost:6379", decode_responses=True)

async def get_cached_response(key: str):
    data = await redis_client.get(key)
    if data:
        return json.loads(data)
    return None

async def set_cached_response(key: str, value: dict, ttl: int):
    await redis_client.set(key, json.dumps(value), ex=ttl)
