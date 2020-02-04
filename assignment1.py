# Author: Ben Nichols

# Recieve user input from keyboard.

a = float(input("Enter number A: "))
b = float(input("Enter number B: "))
print()

# Output calculations, round answer to 4 decimal points

print("A + B", "A - B", "A × B", "A ÷ B", sep = '\t')
print(format(round(a + b, 4), '.2f'), format(round(a - b, 4), '.2f'), format(round(a * b, 4), '.2f'), format(round(a / b, 4), '.2f'), sep = '\t')

# Notify user the program has ended

print()
print("End")
