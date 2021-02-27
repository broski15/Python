import random as rdm

#Random intiger
print(rdm.random())

#Random number form given intigers
print(rdm.randint(1,50))

# Shuffle 
my_list = [1,2,3,4,5,6,7]
rdm.shuffle(my_list)
print(my_list)

# from choice of list
print(rdm.choice([1,2,3,4,5]))