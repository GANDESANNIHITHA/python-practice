def print_nth_fibonacci_numbers(n):
    if n<=0:
        return n
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
def print_nth_fibonacci_numbers(n):
    for i in range(start_number,n+1,3):
        print(nth_fibonacci_namber(i),end="")
        print(n)
if __name__=="__main__":
    n = int(input("Enter the value of n:"))
    print(n)
    
