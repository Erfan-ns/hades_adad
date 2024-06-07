import random
javab = random.randint(1 , 100)
hads = input("hadset chie? ")
hads = int(hads)
while hads!= javab:
    print("hadset paeene mashti! \nboro bala tar") if hads < javab else print("hadset balas mashti! \nboro paeen tar")
    hads = input("dobare hads bezan ")
    hads = int(hads)
print("ahaa hala shod")
