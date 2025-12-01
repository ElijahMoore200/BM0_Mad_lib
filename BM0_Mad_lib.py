import time 
import random
choice = random.randint(1,2)
if choice == 1:
	noun = input("Today, me and my freinds are having a ___ party! (noun):")
	print(f"Today, me and my freinds are having a {noun} party")
	time.sleep(2)
	possesive_noun = input("We're going to ____(possesive_noun) house:")
	print(f"We're going to {possesive_noun} house")
	time.sleep(2)
	plural_noun = input("We're planning to float on ____(plural_noun):")
	print(f"We're planning to float on  {plural_noun}")
	time.sleep(2)
	noun2 = input("We'll go down the water___(noun):")
	print(f"We'll go down the water {noun2}")
	time.sleep(2)
	print(f"Today, me and my freinds are having a {noun} party.We're going to {possesive_noun} house.We're planning to float on {plural_noun}.We'll go down the water {noun2}")
if choice == 2:
	adjective = input("I always thought he was___(adjective):")
	print(f"I always thought he was {adjective}")
	time.sleep(2)
	plural_noun2 = input("He went all the way to ____(plural_noun): ")
	print(f"He went all the way to {plural_noun2}")
	time.sleep(2)
	noun3 = input("His sisters really nice though, in her room is a ____(noun):")
	print(f"His sisters really nice though, in her room is a {noun3}")
	time.sleep(2)
	verb = input("Mr.O on the other hand is always ___ his students(verb):")
	print(f"Mr.O on the other hand is always {verb} his students")
	time.sleep(2)
	print(f"I always thought he was {adjective}. He went all the way to {plural_noun2}. His sisters really nice though, in her room is a {noun3}. Mr.O on the other hand is always {verb} his students.")


