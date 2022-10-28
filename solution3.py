# Write code for algorithm 3 below
#We want to define a function that takes a number, let's say n , 
# prints it, and calls itself again with the value of n-1. 
# The function will keep calling itself until the base case is met. 
# One way to do this is to determine if the number is equal to 0 and when it is, stop the function.
# Think about what the base case and recursive case would be.

def count_down(n):
  #inherent base case
  #(will stop if n <= 0)
  if n>0:
      #recursive case
      print(n)
      count_down(n-1)
   
#test case
n=8
count_down(n)
