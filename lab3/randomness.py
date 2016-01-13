import msvcrt
import random
tries = 0
def coin_Toss():
	coin = random.randint(1, 2)
	if coin == 1:
	    print('Heads')
	elif coin == 2:
	    print ('Tails')
key=msvcrt()
if key==enter:
	coin_Toss()