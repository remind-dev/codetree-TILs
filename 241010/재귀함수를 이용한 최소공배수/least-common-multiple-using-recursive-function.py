n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm(n):
    if n == 0:
        return arr[0]
    
    return lcm(n-1) * arr[n] // gcd(lcm(n-1), arr[n])

print(lcm(n-1))