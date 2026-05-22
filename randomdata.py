from numpy import random

L =[]

for i in range(100):
    L.append(random.randint(1, 100))
print(L)

X = random.choice(L, size=(3, 4))

print(X)