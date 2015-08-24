__author__ = 'trinhkhanh'
print('Multiplication Table')
print("   ", end = '') # Display tab in first line
for i in range(1, 10):
  print('   ',i, end='')
print() # Break line
print('--------------------------------------------------')
for j in range(1, 10):
  print(j, '|', end='')
  # Body content
  for i in range(1, 10):
     print(format(i * j, '5d'), end = '')
  print()