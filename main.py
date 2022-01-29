def isPrime(x):
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

luka = [1, 0]

while luka[-1] <= 1000000000:
    luka.append(luka[-1] + luka[-2])

for i in range(len(luka)):
    if luka[i] > 100000 and isPrime(luka[i]) and luka[i] < 1000000000:
        print(i, luka[i])

