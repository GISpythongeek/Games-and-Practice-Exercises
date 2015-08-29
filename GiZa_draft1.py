# Script Name: GiZa_draft1.py
# Author: Melanie
# Date Created: 28 August 2015
# Last Modified: 28 August 2015
# Version: 1.0

# Modifications: <none>

"""
Description: This script is a painfully simple game aimed at kids learning
basic math skills and, to a lesser extent, about scientific data collection. 
The player is on their first archaeological dig, exploring the Pyramid of GiZa with
the goal of finding the hidden burial tomb of Pharaoh "Gi-Za-Tu-Tep." The player
enters the pyramid and sees a couple of chamber doors and has to solve super simple
math problems to unlock each door. Once inside a chamber, the player digs and collects
data in their database, then moves on to the other chambers in the level (currently 
there are only 2 chambers and 1 level - very basic!). Once the player has visited all
of the chambers on that level, a hidden door opens and they can go up a stairway to the 
next level (which is where the game stops for now).  

I created this script as a practice exercise for my "Learn Python the Hard Way" 
tutorial. 

I run this script via my command line on my Mac.
"""

import time

# all functions defined
def which_chamber():
	time.sleep(1)
	print "You see two chambers..."
	time.sleep(1)
	print "Do you want to enter the chamber on the right or the left?"
	time.sleep(1)
	chamber = raw_input("Enter 'right' or 'left': ")
		
	if chamber == "right":
		print "You picked the %s chamber." % chamber
		unlock_doorR()
	elif chamber == "left":
		print "You picked the %s chamber." % chamber
		unlock_doorL()
	else:
		print "Sorry, you must pick either the right or left chamber..."
		time.sleep(2)
		print "Please pick again."
		which_chamber()


def unlock_doorR():
	time.sleep(2)
	print "The door is locked..."
	time.sleep(2)
	print "Wait, there are some hieroglyphs here, let's translate..."
	time.sleep(2)
	print "\t* If you have a basket with 3 figs in it,..."
	time.sleep(3)
	print "\tand your friend has a basket with 2 figs in it,..."
	time.sleep(3)
	print "\thow many figs do you both have? *"
	answer = int(raw_input("> "))
	
	if answer == 5:
		print "Yes! You will have a total of %s figs. Great job!..." % answer
		time.sleep(2)
		print "The chamber door is opening!"
		collect_data()
	else:
		print "Hmmm, maybe we didn't translate that right..."
		time.sleep(2)
		print "Let's rest our eyes then look at it all over again..."
		unlock_doorR()


def unlock_doorL():
	time.sleep(2)
	print "The door is locked..."
	time.sleep(2)
	print "Wait, there are some hieroglyphs here, let's translate..."
	time.sleep(2)
	print "\t* You are a young Pharaoh planning your pyramid,..."
	time.sleep(3)
	print "\tand your uncle has a pyramid built with 25 stone blocks..."
	time.sleep(3)
	print "\tbut you want to build yours with 3 times that many blocks..."
	time.sleep(3)
	print "\thow many stone blocks will you need to build your pyramid? *"
	answer = int(raw_input("> "))

	if answer == 75:
		print "Perfect! It will take %s stone blocks. Amazing work!" % answer
		time.sleep(2)
		print "The chamber door is opening!"
		collect_data()
	else:
		print "Hmmm, I'm a little rusty with my hieroglyph reading..."
		time.sleep(2)
		print "Let's do a bit of studying then look one more time..."
		unlock_doorL()


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
	time.sleep(2)
	print "You are in search of the tomb of the famous Pharaoh 'Gi-Za-Tu-Tep'..."
	time.sleep(3)
	print "(but her friends just called her GiZa)..."
	time.sleep(2)
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
	time.sleep(2)
	print "You look around and see various chambers..."
	time.sleep(1)
	

def stats():
	time.sleep(1)
	print "You've been in this many chambers so far: ", chambers_visited

	time.sleep(1)
	print "You've collected %d items of data so far." % len(data_list)
	time.sleep(3)
	print "You've collected the following data so far: ", data_list
	time.sleep(3)


def add_chamber():
	global chambers_visited
	chambers_visited += 1

# - main sequence defined in one function -
def main_sequence():
	print "Before you go into a chamber,..."
	time.sleep(1)
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

while chambers_visited < 2:
	main_sequence()

print "Congratulations! You've collected data from all the chambers..."
time.sleep(2)
print "A door opens. You see stairs leading to next level of the pyramid..."
time.sleep(2)
print "You go up to the stairs..."
time.sleep(2)
print "****** script complete *******"
