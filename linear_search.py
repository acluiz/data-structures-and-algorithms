
def linear_search(list, target):
    runs = 0
    
    for index in range(0,len(list)):
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



numbers = [3, 7, 12, 18, 21, 25, 32, 38, 41, 47, 53, 59, 62, 70, 74, 81, 85, 90, 96]
target_index = linear_search(numbers, 38)

log_target_position(target_index)