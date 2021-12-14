# Challenge 1

def sum_to(n):
  sum = 0
  for num in str(n):
    sum += int(num)
  return sum

n = 12
print(sum_to(n))

# Challenge 2

list = [1,29,3,26]
def largest(list):
  return max(list)
  
print(largest(list))