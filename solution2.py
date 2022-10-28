# Write code for algorithm 2 below
# Write a function that prints the natural numbers from 1 to n.

def natural_numbers(x,i):
	if x > i:
        return
    else:
        print(x)
        natural_numbers(x + 1, i)

n=10
natural_numbers(1,n)
#output: 1 2 3  