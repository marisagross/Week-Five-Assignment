#!/usr/bin/env python
# encoding: utf-8

#Marisa Gross
#CIS 125
#Week 4 Assignment- Version 1 (collaborated with Rebekah Orth)

"""
GameOfWar.py

Created by Neumann, Daniel on 2015-10-06.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.

This is the shell copy. Fill this out to get it to work

"""

import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
		if gameCounter > 1000:
			print("Game is a draw")
			break
	
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	print("Player A has " + str(len(PlayerAHand)) + " cards, Player B has " + str(len(PlayerBHand)) + " cards")
	
def playRound(PlayerA, PlayerB):
	
	Acard= PlayerA.pop()
	Bcard= PlayerB.pop()
	
	rankA= getRank(Acard)
	rankB= getRank(Bcard)
	
	if rankA > rankB:
		
		#a wins
		PlayerA.insert(0,Acard)
		PlayerA.insert(0,Bcard)
	elif rankB > rankA:
		#b wins
		PlayerB.insert(0,Bcard)
		PlayerB.insert(0,Acard)
	else:
		PlayerA, PlayerB = WAR(PlayerA, PlayerB)
		
		
	return PlayerA, PlayerB
	
	
def WAR(PlayerA, PlayerB):
	
	
	'''
	This is the method that plays one round of War
	The method takes PlayerA and PlayerB as input parameters
	and returns PlayerA and PlayerB after modification
	for the round
	
	Remember, high card wins. I have included a convenience
	function getRank(anyCard) that will return the rank.
	
	See the README.md for the variations of
	the game to program.
	'''
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	
		
	# See the README.md file for instructions on coding 
	# This module.

	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()

