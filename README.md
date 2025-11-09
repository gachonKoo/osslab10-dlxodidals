[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Ofco1r63)
import sys

number = int(sys.argv[1])

for i in range(1, 101):
    if number % i == 0: 
        print(i, end=" ")

print()
