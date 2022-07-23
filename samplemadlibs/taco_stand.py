def madlib():
	adj1 = input("Adjective: ")
	verb = input("Verb: ")
	food1 = input("Foods (plural):" )
	saying = input("Saying: ")
	noun1 = input("Noun: ")
	food2 = input("Foods (plural): ")
	color = input("Color: ")
	ride = input("Something you would ride in: ")
	animal = input("Animal: ")
	person = input("Person: ")

	madlib = f"Today I went to my favorite Taco Stand called the {adj1} {animal}.\
Unlike most food stands, they cook and prepare the food in a {ride} while you {verb}.\n\
The best thing on the menu is the {color} {noun1}. \n\
Instead of ground beef they fill the taco \
with {food2}, cheese, and top it off with a salsa made from {food1}.\n\
 If that doesn't make \
your mouth water, then it's just like {person} always says:\n\
{saying}!"

	print(madlib)
