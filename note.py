'''
Name: note.py
Author: Trinity Hedman
Created: 2025
Purpose: Keep my notes handy
'''

"""
Week One: line 41
Week Two: line 83
Python Crash Course Video: line 142
Week Three: line 522
Week Four: line 540
Week Five: line 566
Week Six: line 578
Week Seven: line 585
Week Eight: line 591
Week Nine: line 606
Week Ten: line 614
Week Eleven: line 641
Week Twelve: line 667
Week Thirteen: line 678
Week Fourteen: line 811
Week Fifteen: line 822
Week Sixteen: line 870
Finals Week: line 










"""



''' Week One '''
# Always use notes to explain what you are doing.
num_1 = 1, num_2 = 2, num_3 = 3
ans = num_1 + num_2 / num_3
# Use parentheses. It does not know PEMDAS.

mod = num_1 % 2
#modulus operator gives the remainder. (#)

print("mod:", mod)

intdiv = num_1 // 3.46645134
# intager division gives the answer as an integer
print("intdiv:", intdiv)

#plan your program first. either on paper or in a TODO list.
#use TODO lists to remember what you are doing where.
#use agile programing, aka only fix one thing at a time. then you know if it worked.
#if there is a convention, such as using all caps for TODO, keep it.
#in python you can use single quotes ' ' or double quotes " " just keep them in pairs
#ctrl + s = save
#microsoft steals stuff and does a better job marketing it. you have to be good at marketing.
#in security, you don't want anyone to have more access than they need. Jailbraking is when you remove those restrictions
#run a device at user level as much as possible to prevent malware from getting extra access
#security is a balancing act between security and inconvenience

#solve the problem first, then write the code

# to convert an imputed number to something you can use, use float(variable)
# you can combine it with input as var = float(imput("Enter your number:"))

#to use an exponent use pow(base,power) ex. a1 = pow(2,5)
#Or use 2 ** 5 to do the exact same thing.

d1 = 1, d2 = 2, a1 = 3
#Ex of if then
if d1 < d2:
    a2 = a1 + 1
else:
    a2 = a1 + 0


'''Week Two'''
#WET: We Love Typing
    #Retyping everything over and over again. We don't want this.
#DRY: Don't Repeat Yourself
    #As the name sugests, don't repeat yourself over and over again.


"""
A veriable changes each run. Dependent on the imput.
A constant is set to be the same every single run.
Don't type 'magic numbers' in your code, assign them to a constant at the
beginning. Then you only have to change it once if you have to.
"""

#This class makes me feel really fance while I sit here and listen
#to the freshmen learn how to open word and type in it...

#To clear the screen:
"""
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
"""

#You can use a while loop and set it to run while the variable you are testing is equal to itself to check for user error.
    #The loop allows for you have it corrected and then checked again.
    #just make sure you remember the break to end it.
"""
while unit == unit:
    if unit.lower() == c:
        temp_2 = (9 * float(t) / 5) + 32
        break
    elif unit.lower() == f:
        temp_2 = float(t)
        break
    else:
        unit = input("There has been an error in the calculation.\nReminder, C is for Celcuis and F is for Farenheight.\nPlease re-enter your unit:")

"""

#You can also use a test within the loop to see if it is possible to do something.
"""
while t == t:
    try:
        float(t)
        break

    except:
        t = input("Are you trying to pull a fast one on me?\nI'm pretty sure that temperature doesn't exist.\nPlease try again:")
"""

#Using \n in a text display creates a line break.
"""
print("----------------------------------\n-- Weather Small Talk Generator --\n----------------------------------\n ")
"""

""" Python Crash Course Video """

#Four Types of Data
"""
Int
135654
-5412654

Float
526.3
-698412.0

String
'Hello'
"Hello"

Bool
True
False
"""

#Output
"""
print()

you can define the end of the line as end = whatever
automaticaly is end = \n
"""

#Variables
"""
Variables can be set equal to each other.
If you set a variable equal to another variable then change that second
varables value later in the program the first variable does not change
because it reads top to bottom.
"""

#String Methods
"""
len() tells you the length of the string. (number of characters)
type() tells you what type of data a variable contains
var.upper() puts the entire string in upper case
var.lower() lowercases the entire phrase
var.capitalize() capitalizes the first letter and lowercases the rest
var.count() counts the number of times whatever is in the parinthesis is in the string.
    upper and lower case count seperately.
    you can do var.lower().count('whatever')
"""

#String Multiplication and Addition
"""
x = 'hello'
y = 3
z = 'yes'
print(x * y) -> hellohellohello

print(x + z) -> helloyes
"""

#Conditions and Conditional Opperators
"""
== equals
!= is not equal to
<= less than or equal to
>= greater than or equal to
<  less than
>  greater than

Every charicter has an aski code. You can vew this with the ord() function.
Strings can be evaluated for greater or less than bassed on these values.
Upper case letters are less than lower case letters.
for whole strings, the first letters are compaired,
    then if they are the same it moves to the second, ect.
        Like alphabetical order.

If you print these conditions it gives either true or false.
    print(x == y)
"""

#Chained Contitionals
"""
result1 = x == y
result2 = y > x
result3 = z < x + 2

#There is an order of opperations to these. It goes like this:
not
and
or

result4 = result1 or result2 -> if either or both are true, four is true
result5 = result1 and result2 -> only true if both are true

not reverses whatever is after it. so if result1 is true, then not result1 is false.

"""

#Lists
"""
x = [4, True, 'whatever']
    elements do not need to be the same type.
    ordered collection.
print(x) -> will print the list.
print(len(x)) -> will print the length of the list

*
If you make changes to the list later in the program, 
it changes it earlier in the program unless it was refered
to as x[:], which means it is a copy, not the orignial list.
*

x.append('whatever') adds whatever to the end of the list.
    now stored as just x
x.extend([4,5,5,5,5,5,5]) adds that list to the end of the x list.
    now stored as just x
x.pop() removes the last item from the list.

index:
Starts counting at zero. 
[4, True, 'whatever', 'whatever', 4, 5, 5, 5, 5, 5, 5]
index number:
0 == 4
1 == True
2 == 'whatever'
3 == 'whatever'
4 == 4
5 == 5
6 == 5
7 == 5
8 == 5
9 == 5
10 == 5

x.pop(1) will remove index 1 from the list.
[4, 'whatever', 'whatever', 4, 5, 5, 5, 5, 5, 5]
    new list now stored as x
    everything now has a new index to adjust.

    
print(x[1]) acesses index 1

x[1] = 'hello' changes the index one spot to 'hello'

You can have lists and tuples inside of a list.
x = [[4, 5, 6], (2, 1), True, [4, 7, 8, 7]]
"""

#Tuples
"""
Uses parinthesis rather than brackets like a list.

cannot be changed once it is set. 
    No .extend, .append, or .pop.
    Also no x[1] = 2e

you can still print(x[4]) and get the fourth item in the tuple.
"""

#For Loops
"""
for i in range(start, stop, step):
start =  where do you start
stop = where do you stop (does not inclued this)
step = by how much are we going

ex: 
for i in range(0, 10, 2):
    print(i)
This would print:
0
2
4
6
8

You can have not all three of these numbers.
one is stop
two is start, stop
three is start, stop, step

Start is automatic zero if not defined.
Step is automatic 1

If your start value is higher than your stop you must include
step as a negative or it will print nothing.

If your start value is lower than your stop and your step
is negative, it will print nothing.

You can print a list.
for i in [42, 5, 7, 9, 25]:
    print(i)
This will print:
42
5
7
9
25

To print list x (x = [4, True, 'whatever']):

for i in range(len(x)):
    print(x[i])
This will print:
4
True
whatever

for i, element in enumerate(x)
    print(i, element)

This will number the items in your list and print them:
0 4
1 True
2 whatever
"""

#While loop
"""
while condition == true:
    print('run')
    do something
    do something

break tells it to end.
"""

#Slice 
"""
y = [0,1,2,3,4,5,6,7,8,9,10,11]
var = y[start:stop:step]
    all of these values are index numbers.
r = y[0:11:2]
print(r) will print
[0, 2, 4, 6, 8, 10]

r = y[:2] only defines the stop starts at the beginning
    step is one
r = y[2:] only defines the start stops at the end
    step is one
r = y[::2] only defines the step
    starts at beginning and stops at the end

r = y[::-1] reverses the list

Tuples work the exact same as lists in this situation.

This can all also be done on a string.
s = 'The quick brown fox jumped over the lazy dog'
r = s[::2] prints as
Teqikbonfxjme vrtelz o
"""

#Sets
"""
unordered collection.
only used when you care if something does on does not exist,
not about how often or where it exists.

create a set as x = set()
    you can only put one iterable argument in here.
    If you want lots of things in a set, add them to a list.

x = set([3,5,4,7,6,2,3,8,9,7,6,5,3])

print(x) prints
{2, 3, 4, 5, 6, 7, 8, 9}

You can also define a set as x = {3,5,4,7,6,2,3,8,9,7,6,5,3}
This creates a dictionary.

x = {3,5,4,7,6,2,3,8,9,7,6,5,3}

print(x) prints
{2, 3, 4, 5, 6, 7, 8, 9} as well

x.add(12) would add the number 12 to the set.
x.remove(5) would remove all instances of the number 5

print(5 in x) will give you a true or false of if it is there.
"""

#Dictionaries
"""
x = {key:value}

x = {1:5, 2:6, 3:2, 4:9}
print(x) prints
{1: 5, 2: 6, 3: 2, 4: 9}

These do not have to be numbers.
y = {1:'hello', 'key2':4, 12:True}
print(y) prints
{1: 'hello', 'key2': 4, 12: True}

you can add to or redefine with x[key] = value.
If the key already exists, it will redefine. 
If the key does not exits, it will add.

values can also be lists.
z = {1:'hello', 'key2':4, 12:True, 'l':[5,6,7,8]}
print(z) prints
{1: 'hello', 'key2': 4, 12: True, 'l': [5, 6, 7, 8]}

print(key in x) will print true or false of if the key exists.

print(x.values()) prints out all the values:
dict_values([5, 6, 2, 9])

list(x.values) creates a list out of all of the values of x

del x[key] deleates the key specified

for key, value in x.items():
    print(key, value)

prints back the keys and values:
1 5
2 6
3 2
4 9

print(x.get(1))
prints 5
"""

#Comprehenstions
"""
Create a for loop within a line

#TODO: Make a set that contains all multiples between zero and 1000
x = {i for i in range(1000) if i % 5 == 0}
print(x) will print
{0, 515, 5, 520, 10, 525, 15, 530, 20, 535, 25, 540, 30, 
545, 35, 550, 40, 555, 45, 560, 50, 565, 55, 570, 60, 575, 
65, 580, 70, 585, 75, 590, 80, 595, 85, 600, 90, 605, 95, 
610, 100, 615, 105, 620, 110, 625, 115, 630, 120, 635, 125, 
640, 130, 645, 135, 650, 140, 655, 145, 660, 150, 665, 155, 
670, 160, 675, 165, 680, 170, 685, 175, 690, 180, 695, 185, 
700, 190, 705, 195, 710, 200, 715, 205, 720, 210, 725, 215, 
730, 220, 735, 225, 740, 230, 745, 235, 750, 240, 755, 245, 
760, 250, 765, 255, 770, 260, 775, 265, 780, 270, 785, 275, 
790, 280, 795, 285, 800, 290, 805, 295, 810, 300, 815, 305, 
820, 310, 825, 315, 830, 320, 835, 325, 840, 330, 845, 335, 
850, 340, 855, 345, 860, 350, 865, 355, 870, 360, 875, 365, 
880, 370, 885, 375, 890, 380, 895, 385, 900, 390, 905, 395, 
910, 400, 915, 405, 920, 410, 925, 415, 930, 420, 935, 425, 
940, 430, 945, 435, 950, 440, 955, 445, 960, 450, 965, 455, 
970, 460, 975, 465, 980, 470, 985, 475, 990, 480, 995, 485, 
490, 495, 500, 505, 510}

if you create it as a list rather than a set it will put them
in order.
"""

#functions
"""
To define:
def funcname():
    do something

when you call funcname(something) it will do it.

def func(x,y,z)
    return (x * y) + z

print func(3,4,5)
will print out the answer.

You have to add the return or it displays None.
"""

#F strings
"""
name = 'Tim'
x = f'hello {name}. You are {6 + 8} years old.' 
print(x) prints
hello Tim. You are 14 years old.
"""

''' Week Three '''
"""
total = 0
for i in range(1, 101):
    total = total + i

Between the initialize and the loop it will add all of the numbers in the range together.

ctr + / toggles a comment on and off.

time.sleep delays execution for a given number of seconds.
    you have to import time
    time.sleep(1) sleeps for one second.

if you want a double quote to print out inside of the double quotes in the print function use \" to ignore the meaning of the quotes.

"""

''' Week Four '''

"""
.strip gets rid of spaces and punctuation
you can create a function that includes getting input and then call it with the prompt.
     def get_int_imput(prompt):
        user_input = ""
        while user_input == "":
            user_input = input(prompt)
            try:
                user_input = int(user_input)
            except:
                user_input = ""
        return(user_input)
Then you call it var = get_int_input("This is what i want the prompt to say")

if you are defining i in a for loop, do not use for i in range(x): use a different variable. for s in range(x):

you can use lots of loops within loops. 

if you want to see if a word is in a string you can use if "word" in var: and then use the standard if else set.
you can also look for multiple words within that string as if "word" or "letter" in var:


"""

''' Week Five '''

"""
avoid break when possible

look at dictionary section. more notes added there.

most of the stuff you are teaching i have already found from different totorials and such, so my notes are kinda nothing, sorry.

i did go on my own and generate and use an api key, which is kinda this weeks stuff.
"""

''' Week Six '''

"""
If you put multiple files within a folder, you can call one with the other by importing the file name. Then you can use any functions within the other
file the same way you would call a function from a module you import from anywhere else.
"""

''' Week Seven '''

"""
Turned in elsewhere.
"""

''' Week Eight '''

"""
Your MAC adress is unique to your device. If you have an iphone, it likes to hide it and it can make staying connected to some types of internet
very difficult. You can turn that off in settings.

Steel studs make a sort of faraday cage and keep wifi from working well. I assume that the mettle in the mirrors was the same principle when we 
moved into this house. 

If you need things to be able to be kept after a crash, make sure there are lots of different backups.

You don't want a .0 version of python or another coding language because it hasn't had all the bugs worked out and the third party libraries don't
all work yet.
"""

''' Week Nine '''

"""
This was fall break week and we did not have a notes assignment.
"""

''' Week Ten '''

"""
pygame = 2d game engine

COUGAR_GOLD = (249,190,0)
COUGAR_BLUE = (0,58,112)
RGB values.

CMYK is what printers use.

Game loop
1. handle events
2. update game state
3. draw screen
    loop back

pixels have coordinates. Always in quadrent IV except |(x,y)|

typically ahve a program ignore any unexpected input.

movies have 30 fps.

x['hello'] = 'hola' puts the entry 'hello':'hola' into dictionary x. It will override if you use a key that
already has a value.

Deleting a key deletes the value, too.
"""

''' Week Eleven '''

"""
Classes are like groups of things you will create lots of. Then you can set atributes and things that they will do inside of them and it gets re-used over and over again without
lots of typing. This is the structure.

class Customer:  # Class names should be capitalized
    
    def __init__(self):
        self.character = self.pick_character()
        self.order = self.order_amount()
        self.patience = self.patience_level()
    
    def pick_character(self):
        character_1 = pygame.image.load('character_1.png')
        character_2 = pygame.image.load('character_2.png')
        characters = [character_1, character_2]
        return choice(characters)
    
    def order_amount(self):
        return randint(1, 5)
    
    def patience_level(self):
        return randint(1, 10)
"""

''' Week Twelve '''

"""
If you accidentally call the init method instead of the car class and don't put self first it breaks. Also, if you forget to
put anything but a print statement in a while True loop it prints forever.

use y=mx+b in pong, but you have to set up the m with value changes rather than just a fraction. It actually changes the coordinate.
"""

''' Week Thirteen '''

"""
If you ask AI to give you slightly sarcastic notes, it is halarious. 

Week Notes - Weather APIs & GUIs (Because Who Doesn't Love Windows?)
Date: 11/16/2025
Topics: Making the computer tell us it's raining (we have windows for that) & Making buttons do things

OpenWeatherMap API - AKA "How to Overcomplicate Checking the Weather"
The Basics (Week 12 - Part 1)

Step 1: Get an API key from OpenWeatherMap (it's free, like the weather outside)
Step 2: Make a weather_utils.py file to hide your API key (security through obscurity™)
Step 3: Use requests library because apparently we can't just look outside

Important Command:
bashpip install requests  # or pip3 or python -m pip or whatever works on your cursed machine
What Even Is JSON?

Stands for JavaScript Object Notation (yes, JavaScript invades everything)
It's basically a dictionary but make it ✨fancy✨
Format: {"key": "value", "another_key": 42}
Use .get() to extract stuff from the nested nightmare

Accessing JSON data:
pythonweather_data.get("weather")[0].get("description").title()
# Translation: "Go into weather, grab first item, get description, capitalize it"
Week 13 - Part 2: Now With User Input!

Let users type in their city (because hardcoding Lincoln, Nebraska gets old)
Add exception handling (because users WILL break your code)
Optional: Use Rich library to make it pretty (because we're fancy now)

Week 14 - Part 3: Time Is An Illusion

Sunrise/sunset comes as GMT Unix timestamp (thanks, I hate it)
Convert it to local time with datetime module
Add a menu loop so users can check weather for multiple cities (living their best meteorologist life)

Pro tip: The assignment wants 3+ weather items. Look at Tutorial 3 for ideas (temperature, humidity, wind speed, etc.)

Tkinter GUIs - Making Windows Do Things
Chapter 9: Why CLI When You Can Click?
Import Statement:
pythonfrom tkinter import *  # import ALL the things
from tkinter.ttk import *  # import the PRETTIER things
Tutorial 9.1: Hello, Useless Window!

Create a window that does nothing (peak programming)
Use .grid() to organize widgets in rows and columns (like Excel but worse)
root.mainloop() keeps the window alive (otherwise it dies immediately, rude)

Widgets You'll Actually Use:

Label - displays text (revolutionary)
Entry - text input box (where users type lies)
Button - clickable thing that runs functions

Use command=function_name (NO PARENTHESES or it runs immediately)



Entry Widget Methods:

.get() - read what user typed
.delete(0, END) - clear the box
.insert(0, "text") - put text in the box
.config(text="new text") - change label text

Assignment 9.1: Contact Form
Make a form that:

Has name and email entry boxes
Submit button displays the info
Clear button resets everything
Use .grid() with row, column, columnspan

Tutorial 9.2: Square Calculator (Now With OOP!)

Everything goes in a class now (because we're professional™)
Use self. for everything (self.window, self.button, self.existential_crisis)
Actually calculates squares (finally, something useful)

ttk Widgets: Tkinter But Less Ugly
pythonfrom tkinter.ttk import *  # Override default widgets with themed ones

Looks more modern (still not great, but better)
Platform-native styling (fits your OS slightly better)
Grid options: padx, pady, ipadx, ipady, columnspan, rowspan, sticky

Tutorial 9.3: Temperature Converter GUI

Old friend returns in GUI form
Can add .ico file for Windows (Mac/Linux: don't even try)
Degree symbol: ° (copy from degreesymbol.net because typing it is impossible)
Use frames to organize widgets (frames contain other widgets)

Assignment 9.2: Feet to Meters Converter

Literally just copy the temperature converter and change the math
Easy points

Tutorial 9.4: Sun Valley Theme
Because default Tkinter looks like Windows XP had a bad day.
bashpip install sv-ttk  # Make it pretty
pythonimport sv_ttk
sv_ttk.set_theme("light")  # or "dark" if you're edgy

Key Takeaways:

APIs are just fancy data fetchers
JSON is dictionaries with an identity crisis
Tkinter exists and we have to use it
pip install fixes most problems
Always use try/except because users are chaos agents
OOP makes everything "cleaner" (allegedly)
Themes can't save Tkinter, but they try


Assignment Checklist:

 Get OpenWeatherMap API key
 Make weather program with 3+ data items
 Add menu loop for multiple cities
 Make contact form GUI
 Make feet to meters converter GUI
 Add screenshots (proof you didn't just copy-paste)
 Zip and submit (because Blackboard loves zips)

Estimated Time: 180 minutes (or 3 hours of questioning your life choices)

Notes compiled while wondering why we don't just use a weather app like normal people 🌦️💻
"""

''' Week Fourteen '''

"""
If you have imput functions in a moduel that you try and put into a GUI, it will crash. Then you have to do lots of work
to go and fix it. Designing for a GUI from the start is better, but not always possible if you didn't know that was what you
were going to do.

Also, I opened this file differetnly this week and it opened all of the minimized notes and that makes it very long, lol. That's cause
over 800 lines is a lot of lines.
"""

''' Week Fifteen '''

"""
AI fill in got turned on for a different project, and it has some really interesting (in a weird way) ideas about what to put here.
I got it turned off again, now. Anywho, emojis have codes. You can use them. I still don't get why you would, but whatever.

According to Bill in class, he would not like all of my clocks because I exist on a 24 hour format and apparently that is hard.

Here is a table of strftime() codes. Building a table in python comments is hard, lol.

+-----------------+--------------------------------------------------------------------------------------------+-----------------------------+
|   Directive     |   Discription                                                                              |   Format                    |
+-----------------+--------------------------------------------------------------------------------------------+-----------------------------+
|   %a	          |   Abbreviated weekday name.	                                                               |   Sun, Mon,....             |
|   %A	          |   Full weekday name.	                                                                   |   Sunday, Monday,.....      |
|   %w	          |   Weekday as a decimal number.	                                                           |   0, 1,....., 6             |
|   %d	          |   Day of the month as a zero added decimal.	                                               |   01, 02,...., 31           |
|   %-d	          |   Day of the month as a decimal number.	                                                   |   1, 2,...., 30             |
|   %b	          |   Abbreviated month name.	                                                               |   Jan, Feb,...., Dec        |
|   %B	          |   Full month name.	                                                                       |   January, February,....    |
|   %m	          |   Month as a zero added decimal number.	                                                   |   01, 02,...., 12           |
|   %-m	          |   Month as a decimal number.	                                                           |   1, 2,....., 12            |
|   %y	          |   Year without century as a zero added decimal number.	                                   |   00, 01,..., 99            |
|   %-y	          |   Year without century as a decimal number.	                                               |   0, 1,..., 99              |
|   %Y            |   Year with century as a decimal number.	                                               |   2013, 2019 etc.           |
|   %H	          |   Hour (24-hour clock) as a zero added decimal number.	                                   |   00, 01,....., 23          |
|   %-H	          |   Hour (24-hour clock) as a decimal number.	                                               |   0, 1,...., 23             |
|   %I	          |   Hour (12-hour clock) as a zero added decimal number.	                                   |   01, 02,..., 12            |
|   %-I	          |   Hour (12-hour clock) as a decimal number.	                                               |   1, 2,...,12               |
|   %p	          |   Locale’s AM or PM.	                                                                   |   AM, PM                    |
|   %M	          |   Minute as a zero added decimal number.	                                               |   00, 01,...., 59           |
|   %-M	          |   Minute as a decimal number.	                                                           |   0, 1,..., 59              |
|   %S	          |   Second as a zero added decimal number.	                                               |   00, 01,..., 59            |
|   %-S	          |   Second as a decimal number.	                                                           |   0, 1,...., 59             |
|   %f	          |   Microsecond as a decimal number, zero added on the left.	                               |   000000 - 999999           |
|   %z	          |   UTC offset in the form                                                                   |   +HHMM or -HHMM.	         |
|   %Z	          |   Time zone name.	                                                                       |                             |
|   %j	          |   Day of the year as a zero added decimal number.	                                       |   001, 002,....., 366       |
|   %-j	          |   Day of the year as a decimal number.	                                                   |   1, 2,...., 366            |
|   %U	          |   Week number of the year (Sunday as the first day of the week).                           |   00, 01,....., 53          |
|                 |   All days in a new year preceding the first Sunday are considered to be in week 0.	       |                             |
|   %W	          |   Week number of the year (Monday as the first day of the week).                           |   00, 01,....., 53          |
|                 |   All days in a new year preceding the first Monday are considered to be in week 0.	       |                             |
+-----------------+--------------------------------------------------------------------------------------------+-----------------------------+
"""

''' Week Sixteen '''

"""
Why do the AI notes keep turning on? And why does it know that it is finals week? That slighty terrifies me...
I don't really have a whole lot this week. It was basically just working on stuff we have already done some of. 
I will note, tho, that I phrased my discussion post weird. I can make interfaces and have them funciton, they have just
not become anywhere near as second nature as other parts of python.
Also, when I went to put the line number in the index at the top I realized that I had the weeks all set up allready and that 
is how it knew how many weeks there are.
"""