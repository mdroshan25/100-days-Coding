
# Print Left, Right and triangle

def left_triangle(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        
        for j in range(0,i+1):
            print('*',end=" ")
        print('\r')
        
def right_triangle(n):
    
    for i in range(0,n):
        for j in range(0,i+1):
            print('*',end=" ")
        print('\r')
def triangle(n):
    k=n-1
    for i in range(0,n):
        print(end=" ")
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i):
            print('* ',end=" ")
        print('\r')
n=4
left_triangle(n)
right_triangle(n)
triangle(n)

