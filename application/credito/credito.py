import random


def credito(renda):
    aux = random.randint(1, 999)

    if 1 <= aux <= 299:
        credito = 0

    elif 300 <= aux <= 599:
        credito = 1000

    elif 600 <= aux <= 799:
        credito = max(1000, renda/2)

    elif 800 <= aux <= 950:
        credito = 2*renda

    else:
        credito = 1000000

    return credito
