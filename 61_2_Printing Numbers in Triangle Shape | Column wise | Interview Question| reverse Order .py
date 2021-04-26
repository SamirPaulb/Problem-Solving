'''
28 
27 21 
26 20 15 
25 19 14 10 
24 18 13 9  6  
23 17 12 8  5  3  
22 16 11 7  4  2  1 
'''
def  num(n1):
    if n1 == 1:
        return 1
    else:
        return n1 + num(n1-1)

n = int(input("Enter how many rows:   "))

k = num(n)

for row in range(n):
    val = k - row 
    dec = n -1
    for col in range(row+1):
        print(format(val,"<3"),end="")
        val = val - dec
        dec = dec -1
    print()
