import random
javab = random.randint(1, 100)
hads = input("hadset chie? ")
hads = int(hads)
while hads != javab:
    if hads > javab:
        print("hadset balas!")
    else:
        print("hadset paeene!")
    hads = input("hadset chie? ")
    hads = int(hads)
print("ay barikala")