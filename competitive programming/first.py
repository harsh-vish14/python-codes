def distrebution(f,c):
   final = []
   person = 0
   for x in range(0, c):
      if x >= f:
         person -= 1
         final.append((person, 1))
      else:
         final.append((person, 1))
         person += 1
      if (x == c):
         break
   print(final)
   finalresult = [0] * c
   for x in range(0, c - 1):
      a = final[x].count(x)
      print(a)
      finalresult[x] = a + 1
   finalresult.sort(reverse=True)
   return finalresult


t = int(input())
f = int(input())
c = int(input())
print(distrebution(f, c))