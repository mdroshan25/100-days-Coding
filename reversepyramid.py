print(today)
n=10
k= 2*n 
for i in range(10):
    for j in range(0,k):
        print (end="")
    k=k-2
    for j in range(0, k-1):
        print(k, end=" ")
    print("\r")
    
    #output:
    '''
18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 

16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 

14 14 14 14 14 14 14 14 14 14 14 14 14 

12 12 12 12 12 12 12 12 12 12 12 

10 10 10 10 10 10 10 10 10 

8 8 8 8 8 8 8 

6 6 6 6 6 

4 4 4 

2
    '''
