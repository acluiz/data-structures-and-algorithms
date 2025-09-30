def split(list):
  """
    Divides the unsorted list at midpoint into sublists
    Returns two sublists: left_half and right_half

    Takes overall O(k log n) time
  """

  midpoint = len(list) // 2

  left_half = list[:midpoint]
  right_half = list[midpoint:]

  return left_half, right_half

def merge(left_half, right_half):
  """
    Merges two lists, sorting them in the process
    Returns a new merged list

    Takes overall O(n) time
  """

  merged_list = []

  i = 0
  j = 0

  while i < len(left_half) and j < len(right_half):
    if left_half[i] < right_half[j]:
      merged_list.append(left_half[i])
      i += 1
    else:
      merged_list.append(right_half[j])
      j += 1

  while i < len(left_half):
    merged_list.append(left_half[i])
    i += 1

  while j < len(right_half):
    merged_list.append(right_half[j])
    j += 1

  return merged_list

def is_sorted(list):
  size = len(list)

  if size == 0 or size == 1:
    return True
  
  return list[0] < list[1] and is_sorted(list[1:])

def merge_sort(list):
  """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in previous step

    Takes overall O(kn log n) time
  """

  if len(list) <= 1:
    return list

  left_half, right_half = split(list)

  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left, right)


list = [9, 2, 5, 8, 4, 10, 7, 3, 1, 6]
sorted_list = merge_sort(list)

print("Original list: %s" % list)
print("Is sorted?: %s" % is_sorted(list))
print("Sorted list: %s" % sorted_list)
print("Is sorted?: %s" % is_sorted(sorted_list))
