memory = {1:['**','**'],-1:['**','**']}
def wiatrak(n):
  if n in memory:
    odp = memory[n]
  elif n > 1:
    odp = []
    for i in range(0,2*n):
      if i == 0:
        line = '*' + (n-1)*'.' + n*'*'
      elif i in range(1,n):
        line = '*' + wiatrak(n-1)[i-1] + '.' 
      elif i in range(n,2*n-1):
        line = '.' + wiatrak(n-1)[i-1] + '*'
      elif i == 2*n-1:
        line = n*'*' + (n-1)*'.' + '*' 
      odp.append(line)
    memory[n] = odp
  elif n < -1:
    odp = []
    for i in range(0,-2*n):
      if i == 0:
        line = -n*'*' + (-n-1)*'.' + '*'
      elif i in range(1,-n):
        line = '.' + wiatrak(n+1)[i-1] + '*' 
      elif i in range(-n,-2*n-1):
        line = '*' + wiatrak(n+1)[i-1] + '.'
      elif i == -2*n-1:
        line = '*' + (-n-1)*'.' + -n*'*' 
      odp.append(line)
    memory[n] = odp
  return odp

while True:
  n = input()
  if n != 0:
    baza = wiatrak(n)
    for element in baza:
      print element
  else:
    break
