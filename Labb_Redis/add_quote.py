import json
import redis


def add_quote(quote, author):
    r = redis.Redis(host='localhost', port=6379, db=0,
                    decode_responses=True, charset="utf-8", encoding="utf-8")
    quote_dict = {"quote": quote, "author": author}
    r.rpush('quotes', json.dumps(quote_dict))

