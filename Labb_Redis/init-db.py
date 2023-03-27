import json
import redis
import requests

"""Här connectar vi till redis databasen och skapar en ny databas med namnet quotes."""

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True, charset="utf-8", encoding="utf-8")

"""Vår URL som vi VILL hämta data ifrån."""
url = 'https://dummyjson.com/quotes'

"""Här hämtar vi data från URL:en"""
response = requests.get("https://dummyjson.com/quotes?skip=5&limit=100")

"""Här parsar vi JSON datan till python."""
data = response.json()

"""Här lägger vi in datan i vår redis databas."""
for quote in data['quotes']:
    r.rpush('quotes', json.dumps(quote))
