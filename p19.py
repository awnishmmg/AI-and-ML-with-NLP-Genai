#wap in python to show shuffling
import random as r 

hearts_cards = ["A","J","K","Q",2,3,4,5,6,7,8,9,10]

print('Before Shuffling:',hearts_cards)

r.shuffle(hearts_cards)

print('After Shuffling:',hearts_cards)

print('Pickup 1 Card :',r.choice(hearts_cards))


