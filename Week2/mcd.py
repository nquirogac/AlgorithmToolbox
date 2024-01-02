import sys
input = sys.stdin.readline

def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

num = input().split()

num1 = int(num[0])
num2 = int(num[1])

mcd = calcular_mcd(num1, num2)
print(mcd)