#print("for loop")
#word = ["this", "is","roshan"]

# for w in word:   print(w, len(w))
    
#give range of each word for w in range(len(word)): print(w, word[w])

#get odd or even
"""
for x in range(0,5):
    x+=1
    #print(x)
    if x % 2 == 0:
        print(f"{x}::Even No")
    else:
        print(f"{x}::Odd No")

print("PRime No's")
for n in range(1,10):
    for x in range(2,n):
        if n % x ==0:
            
            print(f"{n}  get by multiple of {x}  and is divisible of {x}, So it is not a prime no")
            break
    else:
        print(f"{n} is prime no")
"""
#Loop while for the printing numbers
def whileloop(x):
    y=0
    while(y<x):
        print(y)
        y=y+1
        
#print number using for loop
def forloop(x):
    y=0
    for i in range(y,x):
        print(i)
        
 #print even or odd based on the condition
def printodd(x):
     y=0
     for i in range(y,x):
         if(i%2 != 0): continue
         print("Even No: ",i)
         
     for i in range(y,x):
         if(i%2 == 0): continue
         print("Odd No: ",i)

printodd(10)
#whileloop(10)
#forloop(10)
