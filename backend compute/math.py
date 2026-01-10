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
