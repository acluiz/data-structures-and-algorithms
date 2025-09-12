def binary_search(list, target):
  runs = 0
  first_index = 0
  last_index = len(list) - 1

  while(first_index <= last_index):
    runs = runs + 1
    midpoint = (first_index + last_index) // 2

    if list[midpoint] == target:
      print("Total runs: ", runs)
      return midpoint
    elif list[midpoint] > target:
      last_index = midpoint - 1
    else:
      first_index = midpoint + 1
  
  return None
  

def log_target_position(target_index):
  if target_index is not None:
    print("Target found at index: ", target_index)
  else:
    print("Target not found")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_index = binary_search(numbers, 6)

log_target_position(target_index)