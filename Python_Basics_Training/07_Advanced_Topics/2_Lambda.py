m=lambda x,y,z : max(x,y,z) 
print(m(3, 5, 2)) 

temparatures=[34,46,51,52,53,54,55]
x=map(lambda x: (x*9)/5+32, temparatures)
print(list(x))