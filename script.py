from textwrap import dedent
import media
from random import sample

"""
Project Brainstorming:
? What does your program do?
My program will take in general information to help you narrow down a form of entertainment to consume.
? What questions will you ask the user?
Guiding questions to help narrow down the type of entertainment the user is looking for

? How do the above questions combine to return a recommendation?
! Make sure it satisfies all the project requirements
"""


def greet():
    print(dedent("""\
        Welcome to the Entertainment Recommendation System!

        We have a vast collection of media to share,
        but in order to give you a recommendation,
        we need to narrow down your choices.
    """))


def choose_random_media_type() -> str:
    return sample(["movies", "tv_shows", "games", "songs"], 1)[0]


def choose_random_metric() -> str:
    return sample(["year", "genre", "length"], 1)[0]


def choose_media_type() -> str:
    choice = input("a) Movies\nb) TV Shows\nc) Games\nd) Songs\ne) Not sure\nf) Surprise me!\n").lower()
    media_type = ""
    if choice == "a":
        media_type = "movies"
    elif choice == "b":
        media_type = "tv_shows"
    elif choice == "c":
        media_type = "games"
    elif choice == "d":
        media_type = "songs"
    elif choice == "e":
        media_type = narrow_down_choices()
    elif choice == "f":
        media_type = choose_random_media_type()
    else:
        print("Invalid choice. Please try again.")
        choose_media_type()
    return media_type


def choose_metric() -> str:
    choice = input("What's most important to you,\na) Release date\nb) Genre\nc) Length\nd) Surprise me!\n").lower()
    metric = ""
    if choice == "a":
        metric = "year"
    elif choice == "b":
        metric = "genre"
    elif choice == "c":
        metric = "length"
    elif choice == "d":
        metric = choose_random_metric()
    else:
        print("Invalid choice. Please try again.")
        narrow_down_choices()
    return metric


def choose_media_by_year():
    sorted_games    = [*dict(sorted(media.games.items(), key=lambda item: item[1]["year"])).keys()]
    sorted_movies   = [*dict(sorted(media.movies.items(), key=lambda item: item[1]["year"])).keys()]
    sorted_tv_shows = [*dict(sorted(media.tv_shows.items(), key=lambda item: item[1]["year"])).keys()]
    sorted_songs    = [*dict(sorted(media.songs.items(), key=lambda item: item[1]["year"])).keys()]

    print("All right, we'll choose something based on when it's from.")
    print("Are you looking for something:")
    choice = input("a) Older\nb) Newer\n").lower()

    if choice == "a":
        print("Finding something older...")
        older_games     = sorted_games[:3]
        older_movies    = sorted_movies[:3]
        older_tv_shows  = sorted_tv_shows[:3]
        older_songs     = sorted_songs[:3]
        older_media = {
            "Games":    older_games,
            "Movies":   older_movies,
            "TV Shows": older_tv_shows,
            "Songs":    older_songs
        }
    else:
        print("Finding something newer...")
        newer_games     = [*sorted_games.keys()][-3:]
        newer_movies    = [*sorted_movies.keys()][-3:]
        newer_tv_shows  = [*sorted_tv_shows.keys()][-3:]
        newer_songs     = [*sorted_songs.keys()][-3:]
        newer_media = {
            "Games":    newer_games,
            "Movies":   newer_movies,
            "TV Shows": newer_tv_shows,
            "Songs":    newer_songs
        }
        return newer_media
    


def sort_media_by_genre():
    return "Sorting media by genre..."


def sort_media_by_length():
    return "Sorting media by length..."

# Currently returns None and gets passed to run(). 
# Will follow new functions instead
def choose_sort(metric):
    if metric == "year":
        media_choices = choose_media_by_year()
    elif metric == "genre":
        sort_media_by_genre()
    elif metric == "length":
        sort_media_by_length()


def narrow_down_choices():
    print("Not sure what to choose? No problem!")
    print("Let's use another metric to narrow down your choices.")
    metric = choose_metric()
    return choose_sort(metric)


def run():
    greet()
    print("Let's start by figuring out what kind of entertainment you're in the mood for.")
    print("What kind of media should we look at?")
    media_type = choose_media_type()
    print(f"All right! Let's take a look at some {media_type if media_type != 'tv_shows' else 'tv shows'}!")


if __name__ == "__main__":
    run()