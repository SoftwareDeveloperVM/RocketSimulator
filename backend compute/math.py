def derivative(function, x, limit):
  dydx = (function(x+limit)-function(x))/limit 
  return dydx

def integral (start, stop, function, step):
  sumvalue = 0
  val = start + ((stop-start)/step)
  count = 0
  while True:
    sumvalue += function(val)
    val += ((stop-start)/step)
    count += 1
    if count >= (step):
      break
  return (sumvalue*(stop-start)/step)

def matrix (rows, columns, characters=0):
  matrix = []
  for element in range(rows):
     for element in range(columns):
       matrix.append(characters)
  print(matrix)