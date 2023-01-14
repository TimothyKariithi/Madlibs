#String Concatenation ( aka how to put strings together)
# suppose we want to crea a string that says " subscribe to ______"
#youtuber = "Timothy ariithi" # some string variable

# a few ways to do this
#print("subscriber to " + youtuber)
#print(" subscribe to {}".format(youtuber))
#print(f"subrcribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person:")

madlib = f"Computer programming is so {adj}! It makes me so exited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!" 

print(madlib)