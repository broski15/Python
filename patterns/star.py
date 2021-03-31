# "*" pattern printing

# * * * * 
# * * * *  
# * * * * 
# * * * * 
for a in range(4):
    for b in range(4):
        print("* ",end="")
 
    print()

# *      
# * *   
# * * *    
# * * * * 
for a in range(4):
    for b in range(a+1):
        print("* ",end="")
 
    print()

# * * * * 
# * * *   
# * *  
# * 
for a in range(4):
    for b in range(4-a):
        print("* ",end="")
 
    print()


print( (3**2)//2 )