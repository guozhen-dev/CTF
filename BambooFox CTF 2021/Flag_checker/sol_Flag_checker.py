def enc3(i):
  f = init >> 6
  f = f % 4
  if f == 0 :
    res  = (i >> 3) | ((i << 5)%256)
  elif f==1 :
    res = ((i << 2)%256) | (i >> 6)
  elif f == 2:
    res = i + 0b110111
  else :
    res = i ^ 55
  return res
def enc2(i):
  f = init >> 4
  f = f % 4
  if f == 0 :
    res  = (i >> 3) | ((i << 5)%256)
  elif f==1 :
    res = ((i << 2)%256) | (i >> 6)
  elif f == 2:
    res = i + 0b110111
  else :
    res = i ^ 55
  return res

def enc1(i):
  f = init >> 2
  f = f % 4
  if f == 0 :
    res  = (i >> 3) | ((i << 5)%256)
  elif f==1 :
    res = ((i << 2)%256) | (i >> 6)
  elif f == 2:
    res = i + 0b110111
  else :
    res = i ^ 55
  return res
def enc0(i):
  f = init % 4
  if f == 0 :
    res  = (i >> 3) | ((i << 5)%256)
  elif f==1 :
    res = ((i << 2)%256) | (i >> 6)
  elif f == 2:
    res = i + 0b110111
  else :
    res = i ^ 55
  return res

a = [182,199,159,225,210,6,246,8,172,245,6,246,8,245,199,154,225,245,182,245,165,225,245,7,237,246,7,43,246,8,248,215]
init = 0 
for k in a:
  for i in range(0,128)[::-1]:
    init = i
    if enc3(enc2(enc1(enc0(i))))==k:
      if chr(i).isprintable():
        print (chr(i),end='')
      # pass
  print ('')
