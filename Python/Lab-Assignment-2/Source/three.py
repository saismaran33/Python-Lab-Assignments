#Hotel Management System
class Hotel:
    def __init__(self, name):
        self.hname = name
        self.__value=5 #private member of the class
    def dis(self):
        print("The name of the Hotel is: ",self.hname)

class Employee(Hotel): #Inheritance
    def __init__(self,name, n,age,salary):
        super().__init__(name) # Super call to instatntiate directly from the parent call
        self.ename = n
        self.eage = age
        self.__esalary = salary #private of the class
    def display(self):
        print("Name: ",self.ename,"Age: ",self.eage)
class Room():
    def __init__(self,number,type,status):
        self.roomnumber = number
        self.roomtype = type
        self.roomstatus = status

class Guest(Room,Hotel): #Mutiple Inheritance
    def __init__(self, name,phone,id,roomnumber):
        self.roomnumber=roomnumber
        self.oname = name
        self.oid = id
        self.ophone = phone
    def display(self):
        print("Name: ",self.oname,"Phone ",self.ophone,"ID: ",self.oid,"Roomate: ",self.roomnumber)

class Manager(Hotel):
    def __init__(self, name,myhotel):
        self.name = name
        super().__init__(myhotel)
    def dis2(self):
        print("I am the Manager: ", self.name,"to the hotel: ",self.hname)
a=input("Enter the Name of the Hotel: ")
obj=Hotel(a) #obect creation
obj.dis()
print(obj._Hotel__value)

b = input("enter the employee name: ")
c = input("enter the employee age: ")
obj2=Employee(a,b,c,20000)
obj2.display()

obj2.dis()
#print(obj2,_Hotel__value) #This creates an error because we are accesing a private member of base/parent class

obj3 = Room(101,"single","Occupied")

x=input("Enter the name")
i=input("Enter the phone number")
d=input("Enter the id number")
r=input("Enter room number")
obj4 = Guest(x,i,d,r)
obj4.display()
obj5 = Manager("Ben","Marriott")
obj5.dis2()