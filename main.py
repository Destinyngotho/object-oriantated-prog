# class fruit:
#       taste="sweet" #class variable
#       def __init__(self,name,color): #__init__ constructor method.name and color is instance variable
#         self.fruitname=name
#         self.fruitcolor=color

# objapp=fruit("apple","red") #objapp is a object for fruit class
# print(objapp.fruitname)
# print(objapp.fruitcolor)
# print("Apples's taste is",objapp.taste)

# objban=fruit("banana","yellow") #objban is a object for fruit class
# print(objban.fruitname)
# print(objban.fruitcolor)
# print("Banana's taste is",objban.taste)
# class parrot:
#   species="bird"
#   def __init__(self,name,age):
#     self.birdname=name
#     self.birdage=age

# blu=parrot("Blu",10)
# woo=parrot("Woo",15)

# print("Blu is a",blu.species)
# print("Woo is also a ",woo.species)

# print(blu.birdname,"is",blu.birdage,"years old")
# print(woo.birdname,"is",woo.birdage,"years old")
class parrot:
  species="bird"
  def __init__(self,name,age):#constrctor method
    self.birdname=name
    self.birdage=age
  def sing(self,song):#instance method
    return "{} sings {}".format(self.birdname,song)
  def dance(self): #instance method
    return "{} is now dancing".format(self.birdname)

blu=parrot("Blu",10)
woo=parrot("Woo",15)

print("Blu is a",blu.species)
print("Woo is also a ",woo.species)

print(blu.birdname,"is",blu.birdage,"years old")
print(blu.sing("beliver..beliver.. "))
print(woo.birdname,"is",woo.birdage,"years old")
print(woo.dance())