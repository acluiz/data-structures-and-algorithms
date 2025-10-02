from data_structures.linked_list import LinkedList


def split(linked_list):
  """
    Divide the unsorted list at midpoints into sublists
  """

  if linked_list == None or linked_list.head == None:
    left_half = linked_list
    right_half = None

    return left_half, right_half
  else:
    size = linked_list.size()
    midpoint = size // 2
    mid_node = linked_list.node_at_index(midpoint - 1)

    left_half = linked_list
    right_half = LinkedList()

    right_half.head = mid_node.next_node
    mid_node.next_node = None

    return left_half, right_half

def merge(left_half, right_half):
  """
    Merges two linked lists, sorting by data in nodes
    Returns a new, merged list
  """

  # Create a new linked list that contains nodes from merging left and right
  merged = LinkedList()

  # Add a fake head that is discarded later
  merged.add(0)

  # Set current at the head of the linked list
  current = merged.head

  # Obtain head nodes for leaft and right linked lists
  left_head = left_half.head
  right_head = right_half.head

  # Iterate over left and right until we reach the tail node
  while left_head or right_head:
    # If the head node of left is None, we're past the tail
    # Add the node from right to merged linked list
    if left_head is None:
      current.next_node = right_head
      # Call next on right to set loop condition to False
      right_head = right_head.next_node
    # If the head node of right is None, we're past the tail
    # Add the node from left to merged linked list
    elif right_head is None:
      current.next_node = left_head
      # Call next on left to set loop condition to False
      left_head = left_head.next_node
    else:
      # Not at either tail node
      # Obtain node data to perform comparison operations
      left_data = left_head.data
      right_data = right_head.data

      # If data on left is less than right, set current to left node
      if left_data < right_data:
        current.next_node = left_head
        # Move left head to next node
        left_head = left_head.next_node
      else:
      # If data on right is less than left, set current to right node
        current.next_node = right_head
        # Move right head to next node
        right_head = right_head.next_node
   
    # Move current to next node
    current = current.next_node

  # Discard fake head and set first node as head
  head = merged.head.next_node
  merged.head = head

  return merged

def merge_sort(linked_list):
  """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
  """

  if linked_list.size() == 1:
    return linked_list
  elif linked_list.head is None:
    return linked_list
  
  left_half, right_half = split(linked_list)

  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left, right)



linked_list = LinkedList()

linked_list.add(9)
linked_list.add(2)
linked_list.add(5)
linked_list.add(8)
linked_list.add(4)
linked_list.add(10)
linked_list.add(7)
linked_list.add(3)
linked_list.add(1)
linked_list.add(6)

print(linked_list)

sorted_linked_list = merge_sort(linked_list)

print(sorted_linked_list)