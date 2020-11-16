# Yahtzee Game

# MODULES
import pygame
import random
import sys
from dice import Dice
from scorecard import ScoreCard



# INITIALIZE
pygame.init()
WIN_X, WIN_Y = 400, 700
window = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.display.set_caption('Yahtzee')
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()
run = True
FPS = 60
stored_value = 0 		# If == 0, then you can reroll, else, store value in scorecard box.



# COLORS
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255, 127, 127)



# INITIALIZE OBJECTS
# Dice: Initial value = 0
dice_list = []
x = 50
y = 625
sq = 50
for i in range(5):
	d = Dice(window, WHITE, x, y, sq, 0)
	dice_list.append(d)
	x += 60


# LIST OF ALL TEXT: Same length as 'scorecard_list[]'
# 
text_list = ["ACES: Coun"]


# Score Card = Two sections...clickable boxes and static text box to the left.
# 6 Upper / 8 Lower / 14 Total clickable boxes
scorecard_list = []

x = 325
y = 60
sq = 30

# UPPER
for i in range(6):
	s = ScoreCard(window, WHITE, x, y, sq, 'Hello World!')
	scorecard_list.append(s)

	y += 30

# LOWER
y = 270
for i in range(8):
	s = ScoreCard(window, WHITE, x, y, sq, 'Hello World!')
	scorecard_list.append(s)
	y += 30





# MAIN LOOP
while run:


	# INITIALIZE
	clock.tick(FPS)
	window.fill(0)
	MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
	pygame.draw.rect(window, RED, (167, 542, 66, 66)) 	# BIG RED BUTTON


	# FOR EACH EVENT...
	for event in pygame.event.get():
		# IF QUIT...
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	
		# ROLL: If transfered value OR new game.
		if stored_value == 0:

			# BUTTON: If clicked on button... 		# Q: ROLL DICE: Q: How do I do this with SPACEBAR, rather than MOUSEBUTTONDOWN?
			if 167 <= MOUSE_X <= 233 and 542 <= MOUSE_Y <= 608 and event.type == pygame.MOUSEBUTTONDOWN:

				# RESET DICE TOTAL, before rolling.
				dice_total 	= 0

				# Roll the 5 dice.
				for i in range(len(dice_list)):

					# ROLL: Dice
					dice_list[i].roll()

					# ADD: Die roll to total value.
					dice_total += dice_list[i].number

				# STORE VALUE: Once stored value is transfered to a box, we may reroll again.
				stored_value = dice_total

			# Q: How about...
			# mouse click
			# 	for loop for scorecard boxes
			# 		if self.number == 0:
			# 			

		# If stored_value != 0, transfer the value to a scorecard box.
		else:

			# CHECK: scorecard_list[]
			for i in range(len(scorecard_list)):

				# If mouse on a scorecard box AND clicked AND OPEN box...
				if scorecard_list[i].x <= MOUSE_X <= scorecard_list[i].x+60 and scorecard_list[i].y < MOUSE_Y < scorecard_list[i].y+30:
					if event.type == pygame.MOUSEBUTTONDOWN:
						if scorecard_list[i].number == 0:

						# CHECK: If mouse is over a box that is EMPTY.
						# If mouse OVER box...

							# THEN: Put value IN scorecard box.
							scorecard_list[i].number = stored_value

							# RESET: After transfering value over.
							stored_value = 0

							# Interupt loop AFTER we select a scorecard box.
							break

		# Next Action is to then click on a score card box, BEFORE we roll again.



	# DRAW SCORECARD TEXTS
	# pygame

	# DRAW SCORECARD BOXES
	for i in range(len(scorecard_list)):
		scorecard_list[i].draw()

	# DRAW DICE
	for i in range(len(dice_list)):
		dice_list[i].draw()

	# UPDATE: Pygame
	pygame.display.update()











"""
text_list[] to add to scorecard_list[].
Only with strings. no need for a for loop, as each index is a unique phrase.

	ACES: Count ONLY Aces (Ones).
	TWOS: Count ONLY Twos.
	THREES: Count ONLY Threes.

"""
