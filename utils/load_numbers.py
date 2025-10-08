import sys

def load_numbers(filename):
  """Load numbers from a file, one number per line"""
  numbers = []

  try:
    with open(filename, 'r') as f:
      for line in f:
        cleaned_line = line.strip()
        if cleaned_line:  
          numbers.append(int(cleaned_line))
    return numbers
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)
  except ValueError as e:
    print(f"Error: Invalid number in file: {e}")
    sys.exit(1)