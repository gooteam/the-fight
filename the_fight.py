from tkinter import *
import random

class hero:
	def __init__(person, name, points, power, life, shild):
		person.name = input("please enter your name:" )
		person.points = 100
		while person.points > 0:
			person.power = int(input("how much power do he have? "))
			person.points -= person.power
			person.life = int(input("how much life do he have? "))
			person.points -= person.life
			person.shild = person.number
		
	def attack(person, other):
		hit = person.power - other.shild
		other.life -= hit
		



class monster:
	def __init__(person, name, power, life, shild):
		person.name = name
		person.power = random.randint(5:15)
		person.life = 50
		person.shild = 3
		
	def attack(person, other):
		hit = person.power - other.shild
		other.life -= hit
		
