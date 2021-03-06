# Улитка ползет по вертикальному шесту высотой H метров, поднимаясь за день на A метров, а за ночь спускаясь на B метров.
# На какой день улитка доползет до вершины шеста?
import math

h = int(input())
a = int(input())
b = int(input())
print(math.ceil((h - a) / (a - b) + 1))

# За последний день улитка проползет a метров
# За все первые, кроме последнего (h-a) метров.
# В день улитка проползает (a-b) метров.
# Значит (h-a) метров улитка проползет за (h-a)/(a-b) дней.
# Имеем (h-a)/(a-b) дней - это без последнего дня. Добавляем последний день, и имеем:
# (h-a)/(a-b)+1 день.
