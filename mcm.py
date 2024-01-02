import sys
input = sys.stdin.readline

def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a


def calcular_mcm(a, b):
    return a * b // calcular_mcd(a, b)


num = input().split()

num1 = int(num[0])
num2 = int(num[1])

mcm = calcular_mcm(num1, num2)
print(mcm)