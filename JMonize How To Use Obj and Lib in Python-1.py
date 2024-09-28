import emoji #importing emoji library

#Options and Emojis and inputs
print (emoji.emojize("\t:star: Hello and welcome!"+\
    " Please enter your name :star:"))
name = input()
print("Hello " +name)
print ("\nAre you male or female? Type m for male or f for female")
gender = input()
if gender == 'f': #if female
    print(emoji.emojize("You chose female :woman:"))
else: #else male
    print(emoji.emojize("You chose male :man:"))

print(emoji.emojize("\nWhich animal do you like the most? Choose"+\
    " 'b' for bird :bird:, 'd' for dog :dog:, or 'c' for cat :cat:."))
animals = input()
if animals== 'b': #if bird
    print(emoji.emojize("You chose bird! :bird:\n"))
elif animals== 'd': #else if dog
    print(emoji.emojize("You chose dog! :dog:\n"))
else: #else cat
    print(emoji.emojize ("You chose cat! :cat:\n")) #end of options

#choose your age
print(emoji.emojize("What is your age? :calendar:"))
age = input()
print(emoji.emojize("Sweet! You are " + age + " years old! :thumbs_up:\n"))

#tuple options chosen.
myTuple=(name + " "+ gender + " " + animals + " " + age)
print ("You chose " + myTuple)


#Dictionary:
myDict ={
    "Name ": name,
    "Gender ": gender,
    "Animal ": animals,
    "Age ": age
}
print(myDict)#end dictionary

print(emoji.emojize("\n\tGoodbye! :waving_hand:\n")) #end