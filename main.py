def main():
	print("Hello World")
if __name__ == '__main__':
	main()

# Exercise 1
x = 52633
for i in range(x+1):
	if i == 0:
		continue
	if x % i == 0:
		print(i)

# Exercise 2
def print_factor(x):
	factors = []
	for i in range(1, x+1):
		if x % i == 0:
			factors.append(i)
	return factors

print_factor(18)

# Exercise 3
l = [52633, 8137, 1024, 999]

for num in l:
	b = print_factor(num)
	print(f"All factors of {num} are :", b)