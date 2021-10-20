"""Q1. Byte converter. Define a function using tuples and loops to convert bytes into other units.

units = ('B', 'KB', 'MB', 'GB')
conversion = (1, 10**3, 10**6, 10**9)
"""

cdict = {'B': 1, 'KB':2**10, 'MB':2**20, 'GB':2**30, 'TB':2**40}

# first converter stops when the unit is too large (defined as 10x the actual size, using < 0.1 of the unit)
def stopping_converter(input):
  for i in cdict:
    unit = round(input/cdict[i],2)
    if unit > 0.1: # To return 'the correct number', interpreted as >0.1 units
      print(unit, i)
    else:
      break

print('The stopping converter :')
stopping_converter(1271251)
print('\n')

def continuing_converter(input):
  for i in cdict:
    unit = input/cdict[i]
    print(unit, i)


print('The stopping converter :')
continuing_converter(1271251)
print('\n')


