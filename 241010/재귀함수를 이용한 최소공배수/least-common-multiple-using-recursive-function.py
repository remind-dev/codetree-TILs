n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm(n):
    if n == 0:
        return arr[0]
    elif n == 1:
        return arr[1]
    
    return lcm(n-2) * lcm(n-1) // gcd(lcm(n-2), lcm(n-1))

print(lcm(n))