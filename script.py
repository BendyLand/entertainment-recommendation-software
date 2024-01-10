from textwrap import dedent
""" 
Idea Planning:
? What topics will be searchable in your recommendation system?
Users can input general information such as a media type as well as guidance information, such as a decade or a genre, and the system will return a recommendation of some form of entertainment.
---------------------------

Project Brainstorming:
? What does your program do?
My program will take in general information to help you narrow down a form of entertainment to consume.
? What data do you need?
I need a large collection of various pieces of entertainment; songs, movies, tv shows, games, etc. 
? What questions will you ask the user?
Guiding questions to help narrow down the type of entertainment the user is looking for

? How do the above questions combine to return a recommendation?
! Make sure it satisfies all the project requirements
"""

# It might be good to have a list of three options as a result.

# To get to that point, find out what the user wants to prioritize (media, date, length, feel, etc.) 
# then narrow it down from that point. 

# Use letters for user input a) action, b) action, etc.

games = {}
movies = {}
tv_shows = {}
songs = {}

def greet():
    print(dedent("""\
        Welcome to the Entertainment Recommendation System!

        We have a vast collection of media to share,
        but in order to give you a recommendation,
        we need to narrow down your choices.
    """))

def start():
    greet()


start()