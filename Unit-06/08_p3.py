#recursive function for sum of n natural numbers
def sum(n):
    if(n==0):
        return 0
    return n+sum(n-1)

n=int(input("Enter a number: "))
s=sum(n)
print(f"Sum of first {n} natural numbers=",s)