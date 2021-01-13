import math

print ("First const", True)

print ("Second const", False)

print(abs(-12.5), f"є рівним {abs(12.5)}")

print(math.sqrt(9), f"equal 3")

A = True
print("Значить А=True" if A else "Значить А=False")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

Z = False
if Z:
	print("Not False")
else:
	print("Not True")

try:
	print(a)
except NameError:
	print("a not defined")
except:
	print("error occurred")
with open("./text.txt", "r") as f:
	for line in f:
		print(line)

sum_help = lambda a, b:f"sum of a&b"
print("function:", sum_help)
print("function use:", sum_help(7,3))
