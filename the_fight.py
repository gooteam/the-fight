    
from tkinter import *
import random

class hero:
	def __init__(person):
		person.name = input("please enter your name:" )
		person.points = 100
		answer = "yes"
		while person.points > 0 and answer != "no":
			person.power = int(input("how much power do he have? "))
			if person.power >= person.points:
				print("no, you should choose less then " + person.points + "points")
			else:
				person.points -= person.power
				person.life = int(input("how much life do he have? "))
				if person.life>= person.points:
					print("no, you should choose less then " + person.points + "points")
				else:
					person.points -= person.life
					person.shild = int(input("how much shild do he have? "))
					answer = input("is this ok now? ")
		
	def attack(person, other):
		hit = person.power - other.shild
		other.life -= hit
		



class monster:
	def __init__(person, name, power, life, shild):
		person.name = name
		person.power = random.randint(5,15)
		person.life = 50
		person.shild = 3
		
	def attack(person, other):
		hit = person.power - other.shild
		other.life -= hit	
