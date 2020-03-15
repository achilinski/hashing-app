import random


def generator(number):
    for i in range(number):
        a = str()
        for i in range(5):
            a += chr(random.randint(97, 122))
        yield a


def hasher(slowo):
    gotowy_hash = 1
    for indeks, slowo in enumerate(slowo):
        gotowy_hash *= ord(slowo) * (indeks + 1)
    return gotowy_hash % 2069


def hashtablica(lista):
    hashtabela = [None for i in range(2069)]
    for i in lista:
        hashkod = hasher(i)
        j = 0
        while 1:
            if hashtabela[(hashkod + j) % 2069] == None:
                hashtabela[(hashkod + j) % 2069] = (hashkod, i)
                break
            else:
                j += 1
            if j > 2071:
                print(hashtabela)
                print("tablica pelna ")
                raise IndexError
    return hashtabela


l = [i for i in generator(3000)]
print(hashtablica(l))
