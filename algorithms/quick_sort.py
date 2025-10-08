import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.load_numbers import load_numbers

numbers = load_numbers(sys.argv[1])

def quick_sort(values):
  if len(values) <= 1:
    return values
  
  less_than_pivot = []
  greater_than_pivot = []
  pivot = values[0]

  for value in values[1:]:
    if value <= pivot:
      less_than_pivot.append(value)
    else:
      greater_than_pivot.append(value)

  # print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
  return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

sorted_numbers = quick_sort(numbers)
print(sorted_numbers)