#This example is written using while loop
#Run this here :https://www.online-python.com/online_python_compiler

def sum():
    a=0
    b=1 
    c=1
    while (c<=100):
        print(f' ',a,' ')
        c=a+b
        a=b
        b=c 
sum()

output:
  0  
  1  
  1  
  2  
  3  
  5  
  8  
  13  
  21  
  34  
  55  
