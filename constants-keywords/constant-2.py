#wap in python using frozen set

CONSTANT = {'GRAVITY':9.8,'PI':3.14}
frozenset(CONSTANT)
print(CONSTANT['GRAVITY'])

GRAVITY = {10}
NEW_GRAVITY = frozenset(GRAVITY)
print(NEW_GRAVITY)


