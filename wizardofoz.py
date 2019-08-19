# Author: @bensauer, idea by @jonesabi
# Source: https://github.com/bensauer/saywizard
# Minor edits done by @gracepchen July 2019

# TODO
# Print newlines or comments as needed on the terminal without taking up keys

import inspect,os,sys

# Keys to exit Say Wizard and reload the script
EXIT = "~"
RELOAD = "!"

# To hold list of phrases
linePos = 0
lines = []
keysIndex = []

def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result

def printLines(lines):

	for line in lines:
		print(line[0] + ") " + line[1] + "\r")

def load():
	# Clear the screen
	os.system("clear")

	# Change this list according to whatever and however many 
	# keys you want. Capital and lowercase letters are 
	# separate keys.
	keys = "1234567890qwertyuiopasdfghjklzxcvbnm,./?;:'[{]}\|QWERTYUIOP"
	keyList = list(keys)

	#print os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

	# Open script.txt
	# OPTIONAL: replace this with an argument to read from files 
	# other than script.txt
	f = open(os.path.dirname(os.path.abspath(inspect.stack()[0][1])) + 
		"/script2.txt")

	# Reset list of phrases
	linePos = 0
	del lines[:]
	del keysIndex[:]

	# Read in script.txt
	next = f.readline()
	while next != "":
		# Clean up empty array entries and allow comments in script
		if next == '\n' or next[0] == "#":
			next = f.readline()
			continue
		next = next.rstrip('\n')
		lines.append([])
		lines[linePos].append(keyList[linePos])
		keysIndex.append(keyList[linePos])
		lines[linePos].append(next)

		linePos = linePos + 1
		next = f.readline()
	
	# Get user input and say corresponding lines
	print("Press the key to say the phrase:")
	printLines(lines)

# Initial load
load()

# Get user input
while True:
	choice = wait_key()
	
	# Exit key
	if choice == EXIT:
		print("\nEnding Say Wizard. Goodbye.\n")
		exit()
	
	# Reload script.txt
	if choice == RELOAD:
		print("\nReloading script...\n")
		load()
	
	# Check if keypress is in range
	if choice in keysIndex:
		keyItem = keysIndex.index(choice)
		os.system("say -v Samantha \"" + lines[keyItem][1] + "\"")
	# else:
		# print("Try another key.")


