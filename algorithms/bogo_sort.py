import random
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.load_numbers import load_numbers

numbers = load_numbers(sys.argv[1])

def is_sorted(values):
  for index in range(len(values) - 1):
    if values[index] > values[index + 1]:
      return False
    
  return True
    

def bogo_sort(values):
  attempts = 0

  while not is_sorted(values):
    print(attempts)
    random.shuffle(values)
    attempts += 1
    
  return values


print(bogo_sort(numbers))