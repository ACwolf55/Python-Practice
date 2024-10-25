Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> inventory = {'Gold':500,'Sword':1, 'Bow':1, 'Arrows':25}
>>> for Total in inventory.values():
	print(Total)

	
500
1
1
25
>>> for Items in inventory.items():
	print(Items)

	
('Gold', 500)
('Sword', 1)
('Bow', 1)
('Arrows', 25)
>>> for Items in inventory.keys():
	print(Items)

	
Gold
Sword
Bow
Arrows
>>> PKM_moves = {'Thunder':'Electric', 'Ice Beam':'Ice','ExtremeSpeed':'Normal','Stone Edge':'Rock','Hurricane':'Flying'}
>>> for type in PKM_moves.values():
	print(type)

	
Electric
Ice
Normal
Rock
Flying
>>> for moves in PKM_moves.keys():
	print(moves)

	
Thunder
Ice Beam
ExtremeSpeed
Stone Edge
Hurricane
>>> 'Ice Beam' in PKM_moves.keys()
True
>>> 'Fire Blast' in PKM_moves()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    'Fire Blast' in PKM_moves()
TypeError: 'dict' object is not callable
>>> 'Fire Blast' in PKM_moves.moves()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    'Fire Blast' in PKM_moves.moves()
AttributeError: 'dict' object has no attribute 'moves'
>>> 'Fire BLast' in PKM_moves.keys()
False
>>> PKM_moves[Accelerock] = 'Rock'
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    PKM_moves[Accelerock] = 'Rock'
NameError: name 'Accelerock' is not defined
>>> PKM_moves['Accelerock'] = 'Rock'
>>> for moves in PKM_moves.keys():
	print(moves)

	
Thunder
Ice Beam
ExtremeSpeed
Stone Edge
Hurricane
Accelerock
>>> del PKM_moves['Ice Beam']['Thunder']
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    del PKM_moves['Ice Beam']['Thunder']
TypeError: 'str' object does not support item deletion
>>> del PKM_moves['Ice Beam','Thunder']
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    del PKM_moves['Ice Beam','Thunder']
KeyError: ('Ice Beam', 'Thunder')
>>> del PKM_moves['Ice Beam']
>>> del PKM_moves['Thunder']
>>> for moves in PKM_move.keys():
	print(moves)

	
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    for moves in PKM_move.keys():
NameError: name 'PKM_move' is not defined
>>> for moves in PKM_moves.keys():
	print(moves)

	
ExtremeSpeed
Stone Edge
Hurricane
Accelerock
>>> 
