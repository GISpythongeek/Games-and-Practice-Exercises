# Script Name: GiZa_draft2.py
# Author: Melanie
# Date Created: 29 August 2015
# Last Modified: 29 August 2015
# Version: 1.0

# Modifications: Set the game to include 7 chambers, and at each chamber door the 
# 'Hiero-Puzzle' is now different everytime.

"""
Description: This script is a painfully simple game aimed at kids learning
basic math skills and, to a lesser extent, about scientific data collection. 
The player is on their first archaeological dig, exploring the Pyramid of GiZa with
the goal of finding the hidden burial tomb of Pharaoh "Gi-Za-Tu-Tep." The player
enters the pyramid and sees various chamber doors and has to solve super simple
math problems to unlock each door. Once inside a chamber, the player digs and collects
data to add to their database, then moves on to the other chambers in the level (currently 
there is only one level with 7 chambers). Once the player has visited all
of the chambers on that level, a hidden door opens and they can go up a stairway to the 
next level (which is where the game stops for now).  

I created this script as a practice exercise for my "Learn Python the Hard Way" 
tutorial. 

I run this script via my command line on my Mac.
"""

import time
import random
from operator import add, sub, mul

# all functions defined
def which_chamber():
	time.sleep(1)
	print "Which chamber do you want to explore now?"
	time.sleep(1)
	chamber = int(raw_input("Enter a number from 1 to 7: "))
		
	if chamber >= 1 and chamber <= 7:
		print "You picked chamber number %s." % chamber
		unlock_door()
	else:
		print "Sorry, you must pick a chamber number between 1 and 7..."
		time.sleep(2)
		print "Please pick again."
		which_chamber()


def unlock_door():
	time.sleep(2)
	print "The door is locked..."
	time.sleep(2)
	print "Wait, there are some hieroglyphs here, let's translate..."
	time.sleep(2)
	print "It's a Hiero-Puzzle, and if you solve it the door will open..."
	time.sleep(2)
	print "but you need to be careful, the answer could be a negative number..."
	time.sleep(2)

	easy_puzzle()
	

def easy_puzzle():
	ops = (add, sub, mul)
	op = random.choice(ops)

	a = random.randint(1,10)
	b = random.randint(1,10)
	o = ""
	
	if op == add:
		o = "+"
	elif op == sub:
		o = "-"
	elif op == mul:
		o = "*"
	else:
		print "Something is wrong!!!"
		easy_puzzle()

	c = op(a, b)

	print "Hiero-Puzzle: %d %s %d =" % (a, o, b)
	answer = int(raw_input("--> "))

	if answer == c:
		time.sleep(0.5)
		print "Great Work!"
		collect_data()
	else:
		time.sleep(0.5)
		print "That was a hard one to translate. Let's try another one..."
		time.sleep(1)
		easy_puzzle()

	
def collect_data():
	time.sleep(2)
	print "You enter the chamber and look around for the best place to dig..."
	time.sleep(3)
	print "You pick your spot, open your backpack, and get out your tools..."
	time.sleep(3)
	print "and you start to dig..."
	time.sleep(1)

	for i in range(3):
		print "\t~ dig ~"
		time.sleep(1)

	print "You've found a new item of data! You add it to your database."
	time.sleep(2)

	for i in range(3):
		print "\t~ type ~"
		time.sleep(1)

	new_data = "data%d" % (len(data_list) + 1)
	return data_list.append(new_data)

		
def start_game():
	print "\t\t*** WELCOME TO GiZa ***"
	time.sleep(1)
	print "You are an archaeologist on your first dig..."
	time.sleep(3)
	print "You are in search of the tomb of the famous Pharaoh 'Gi-Za-Tu-Tep'..."
	time.sleep(3)
	print "(but her friends just called her GiZa)..."
	time.sleep(3)
	print "So you are here along the mighty Nile River,..."
	time.sleep(3)
	print "standing outside the Great Pyramid of GiZa..."
	time.sleep(3)
	print "With your shovel, you clear away the sand from the main entrance,..."
	time.sleep(3)
	print "you put your shovel in your backpack with your brush, trowel, and laptop..."
	time.sleep(4)
	print "And you step inside..."
	time.sleep(2)
	print "You have entered the first level of GiZa's pyramid..."
	time.sleep(3)
	print "You look around and see various chambers..."
	time.sleep(2)
	print "You count a total of 7 chambers..."
	time.sleep(2)
	print "and make a note of it in your field notebook..."
	time.sleep(1)
	

def stats():
	time.sleep(1)
	print "You've visited %d chambers." % chambers_visited
	time.sleep(2)
	print "You've collected %d items of data." % len(data_list)
	time.sleep(2)
	print "You've collected the following data so far: ", data_list
	time.sleep(1)


def add_chamber():
	global chambers_visited
	chambers_visited += 1

# - main sequence defined in one function -
def main_sequence():
	if chambers_visited == 0:
		print "Before you go into a chamber,..."
		time.sleep(1)
	elif chambers_visited >= 1 and chambers_visited <= 7:
		print "Before you go into another chamber..."
		time.sleep(2)

	print "Here's what you have written in your field notebook:"
	time.sleep(2)
	stats()
	
	which_chamber()
	add_chamber()
	
##########
# master variables:
chambers_visited = 0
data_list = []

# game operating...

start_game()

while chambers_visited < 7:
	main_sequence()

print "Congratulations! You've collected data from all the chambers..."
time.sleep(2)
print "A door opens. You see stairs leading to next level of the pyramid..."
time.sleep(2)
print "You go up to the stairs..."
time.sleep(2)
print "****** script complete *******"
