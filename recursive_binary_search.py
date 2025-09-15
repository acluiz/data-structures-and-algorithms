def recursive_binary_search(list, target):
  if len(list) == 0 or target not in list:
    return False

  midpoint = len(list) // 2

  if list[midpoint] == target:
    return True
  elif list[midpoint] > target:    
    return recursive_binary_search(list[:midpoint], target)
  else:
    return recursive_binary_search(list[midpoint:], target)
  

def log_target_position(target_index):
  if target_index:
    print("Target found ", target_index)
  else:
    print("Target not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_index = recursive_binary_search(numbers, 9)

log_target_position(target_index)