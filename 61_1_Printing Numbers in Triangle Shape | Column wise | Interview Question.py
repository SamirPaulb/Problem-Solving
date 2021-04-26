'''
1  
2  8  
3  9  14 
4  10 15 19 
5  11 16 20 23 
6  12 17 21 24 26 
7  13 18 22 25 27 28 
'''
n = int(input("Type number of rows:  "))

for row in range(n):
    val = row +1
    dec = n -1
    for col in range(row+1):
        print(format(val,"<3"), end="")
        val = val + dec 
        dec = dec - 1
    print()
