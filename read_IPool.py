import random
def get_one():
    k =[]
    with open('IPool.txt') as f:
        k.append(f.read())
    ip = k[0].split('\n')
    IP0 = []


    for x in ip:
        if x :
            IP0.append(x)

    IP = list(set(IP0))
    return random.choice(IP)

def get_all():
    k = []
    with open('IPool.txt') as f:
        k.append(f.read())
    ip = k[0].split('\n')
    IP0 = []

    for x in ip:
        if x:
            IP0.append(x)

    IP = list(set(IP0))
    return IP


