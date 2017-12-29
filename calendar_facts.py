import json
import random

def construct_fact(db):
    # Generate the fact at random
    fact = ""
    for clause in db:
        path = random.choice(clause)
        for wordlist in path:
            nextword = random.choice(wordlist)
            fact += nextword + " "

    # Fix spaces before punctuation
    fact = fact.replace(" ?", "?")
    fact = fact.replace(" .", ".")

    return fact


with open('facts_db.json') as f:
    db = json.load(f)

input(construct_fact(db))
