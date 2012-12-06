# Oblicza NWD
def gcd(num1, num2):
  if num1 > num2:
    for i in range(1,num2+1):
      if num2 % i == 0:
        if num1 % i == 0:
          result = i
    return result
  elif num2 > num1:
    for i in range(1,num1+1):
      if num1 % i == 0:
        if num2 % i == 0:
          result = i
    return result
  else:
    result = num1
    return result

# Oblicza NWW
def lcm(num1, num2):
  result = num1*num2/gcd(num1,num2)
  return result
  
t = input()
while t > 0:
  liczby = raw_input()
  x = int(liczby.split()[0])
  y = int(liczby.split()[1])
  print lcm(x,y)  
  t -= 1
