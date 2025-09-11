def linear_search(list, target):
  runs = 0

  for index in range(0, len(list)):
    runs = runs + 1

    if list[index] == target:
      print("Total runs: ", runs)
      return index

  print("Total runs: ", len(list))
  return None

def log_target_position(target_index):
  if target_index is not None:
    print("Target found at index: ", target_index)
  else:
    print("Target not found")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_index = linear_search(numbers, 9)

log_target_position(target_index)