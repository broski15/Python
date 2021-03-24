# "#" pattern printing

# # # # 
# # # # 
# # # #
# # # #
for i in range(4):
    for j in range(4):
        print("# ",end="")
 
    print()

#
# #
# # #
# # # #
for a in range(4):
    for b in range(a+1):
        print("# ",end="")
 
    print()

# # # #
# # #
# #
#
for a in range(4):
    for b in range(4-a):
        print("# ",end="")
 
    print()