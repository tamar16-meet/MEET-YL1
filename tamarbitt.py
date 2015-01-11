class Animal:
    def __init__(self,name,color,size,age):
        self.name=name
        self.color=color
        self.size=size
        self.age=age

    def print_all (self):
        print (self.name)
        print (self.color)
        print (self.size)
        print (self.age)
        print("#######################")
  
    def sleep(self):
        print(self.name+" "+"is sleeping")
    def eat(self,food):
        print(self.name+ "is eating"+food)
              



dog=Animal(name="Itamar",color="blue",size="small",age=6)
zebra=Animal(name="Sadek",color="green",size="small",age=22)
lizerd=Animal(name="Dina",color="red",size="small",age=16)

dog.print_all()
zebra.print_all()
lizerd.print_all()

zebra.sleep (zebra.name +" "+"is sleeping")




