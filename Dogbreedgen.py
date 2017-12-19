import sqlalchemy, random

class breed:
  def __init__(self, name):
    self.name = name

breed = ["husky","chocolate lab","greyhound","golden retriever","poodle","corgi","pitbull",
"boxer","German shepard","beagle","great dane","pug","bulldog","dacshund",
"chihuahua","yellow lab"]

def getNewBreed():
    breedA = random.choice(breed)
    breedB = random.choice(breed)
    return breedA[0:random.randint(4,5)] + breedB[random.randint(3,4):]


for i in range(100):
    howIsDog = getNewBreed()
    breed.append(howIsDog)
    print (howIsDog)

with open("breed.txt","w") as f: #in write mode
    f.write("{}".format(breed))

breed = input('enter new breed if want')
