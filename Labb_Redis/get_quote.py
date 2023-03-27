
import random
import json
import redis


def get_random_quote():
    r = redis.Redis(host='localhost', port=6379,
                    db=0, decode_responses=True, charset="utf-8", encoding="utf-8")
    quote_count = r.llen('quotes') # Här hämtar vi antal citat från redisdatabasen
    random_index = random.randint(0, quote_count - 1)
    quote_json = r.lindex('quotes', random_index)
    quote = json.loads(quote_json)
    return quote

