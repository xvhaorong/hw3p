# Author: Haorong Xu hxx5086@psu.edu 

def digit_sum(n):
  if(n>0):
    return n%10 + digit_sum(n//10)
  else:
    return n%10

def run():
  a=int(input("Enter an int: "))
  print (f"sum of digits of {a} is {digit_sum(a)}.")

if __name__ == "__main__":
    run()