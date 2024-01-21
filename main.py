def gcd(numberOne, numberTwo):
  if numberTwo == 0:
     return numberOne
  return gcd(numberTwo, numberOne % numberTwo)

def lcmNaive (numberOne, numberTwo):
  lowestCommonMultiple = (numberOne * numberTwo) / gcd(numberOne, numberTwo)
  return lowestCommonMultiple

numberOne = 5
numberTwo = 10

print(lcmNaive(numberOne, numberTwo))