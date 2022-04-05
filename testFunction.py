import logging
import random
import sys

def count(var):
  num_var = int(0)
  if (var):
    ++num_var

  if num_var < 2:
    print(var, end="")
    print(" has run ", end="")
    print(num_var, end="")
    print(" time.")
  else:
    print(var, end="")
    print(" has run ", end="")
    print(num_var, end="")
    print( " times.")

random_var = 'hello'
count(random_var)

random_var
random_var
random_var

def turnToFrac(a, b):
  print(a, end="")
  print("/", end="")
  print(b)

turnToFrac(6,7)

sys.exit()