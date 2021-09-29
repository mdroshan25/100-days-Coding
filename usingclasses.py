class baseclass():
    def firstmethod(self):
        print("first method")
    def secondmethod(self,stringtest):
        print("second method",stringtest)

#inherit from baseclass
class childclass(baseclass):
    def childmethod(self):
        baseclass.firstmethod(self)
        print("child class1")
    def childmethod2(self,teststring2):
        print("child class2",teststring2)
        
def main():
    print("Calling base class")
    bc = baseclass()
    bc.firstmethod()
    bc.secondmethod("baseclass method")
    
    cc =childclass()
    cc.childmethod()
    cc.childmethod2("child class")
    
if __name__ == "__main__":
    main()
