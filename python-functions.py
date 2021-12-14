# Challenge 1---------------------------------------------

def sum_to(n):
  sum = 0
  for num in str(n):
    sum += int(num)
  return sum

n = 12
print(sum_to(n))

# Challenge 2---------------------------------------------

list = [1,29,3,26]
def largest(list):
  return max(list)
  
print(largest(list))

# Challenge 3---------------------------------------------

def occurances(string1, string2):
  count = string1.count(string2)
  return count
# print(occurances('brey', 'b'))
print(occurances('super-sonic-and-super-shadow', 's'))

# Challenge 4---------------------------------------------

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print(product(-1,4))
print(product(2,5,5))

