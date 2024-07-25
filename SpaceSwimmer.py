import time
import os
import msvcrt									


def getch():
    return msvcrt.getch()

astro = "( •_•)"
move_count_vertical = 0
move_count_horizontal = 0
direction = ""


def move(astro):
	right = " " * move_count_horizontal + astro
	down = "\n" * move_count_vertical + right
	print(down, end="\r", flush=True)

	
while True:
	direction = getch().decode("utf-8")
	if direction == 's':
		move_count_vertical += 1
		os.system('cls')
		move(astro)
		
	elif direction == 'z':
		move_count_vertical -= 1
		os.system('cls')
		move(astro)
	if direction == 'd':
		move_count_horizontal += 1
		os.system('cls')
		move(astro)
		
	elif direction == 'q':
		move_count_horizontal -= 1
		os.system('cls')
		move(astro)
