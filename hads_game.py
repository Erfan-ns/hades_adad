import random
javab = random.randint(1, 100)
hads = input("hadset chie? ")
hads = int(hads)
while hads != javab:
    print("hadset balas mashti!") if hads > javab else print("hadset paeene mashti!")
    hads = input("hadset chie? ")
    hads = int(hads)
print("ay barikala")
