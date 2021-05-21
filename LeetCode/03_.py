s = "is2 sentence4 This1 a3"
s = s.split()
STr1 = ""
for i in range(1,len(s)+1):
    STr1 += f"{i} "
            
        
for i in range(len(s)):
    a = s[i][-1]
    b = s[i].replace(s[i][-1], "")
    STr1 = STr1.replace(a,b)
    STr1 =  STr1.strip()

print(STr1)            