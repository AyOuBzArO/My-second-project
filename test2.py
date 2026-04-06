# test2.py

def sum(n1, n2):
	sum = n1 +n2
	return sum

if __name__ == "__main__":
	a = int(input("Enter an integer N1: \n"))
	b = int(input("Enter an integer N2: \n"))
	result = sum(a, b)
	print("the sum of a and b is: ", result)
