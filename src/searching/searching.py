import math

def linear_search(arr, target):
  # Your code here
  for i, item in enumerate(arr):
    if item == target:
      return i
  return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
  # Your code here
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = math.floor((left + right) / 2)
    if arr[mid] < target:
      left = mid + 1
    elif arr[mid] > target:
      right = mid - 1
    else:
      return mid
  return -1   # not found
