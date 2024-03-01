import random,itertools

deck=list(itertools.product(range(1,14),["spade","club","hearts","Diamond"]))

random.shuffle(deck)
print(deck)



