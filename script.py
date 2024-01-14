from textwrap import dedent
from random import sample
import media
import utils

"""
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
    sorted_games    = [*dict(sorted(media.games.items()   , key=lambda item: item[1]["year"])).keys()]
    sorted_movies   = [*dict(sorted(media.movies.items()  , key=lambda item: item[1]["year"])).keys()]
    sorted_tv_shows = [*dict(sorted(media.tv_shows.items(), key=lambda item: item[1]["year"])).keys()]
    sorted_songs    = [*dict(sorted(media.songs.items()   , key=lambda item: item[1]["year"])).keys()]

    print("All right, we'll choose something based on when was released.")
    print("Are you looking for something:")
    choice = input("a) Older\nb) Newer\n").lower()

    if choice == "a":
        print("Finding something older...")
        older_games     = sorted_games[:3]
        older_movies    = sorted_movies[:3]
        older_tv_shows  = sorted_tv_shows[:3]
        older_songs     = sorted_songs[:3]
        older_media     = {
            "Games":    older_games,
            "Movies":   older_movies,
            "TV Shows": older_tv_shows,
            "Songs":    older_songs
        }
        return older_media
    else:
        print("Finding something newer...")
        newer_games     = sorted_games[-3:]
        newer_movies    = sorted_movies[-3:]
        newer_tv_shows  = sorted_tv_shows[-3:]
        newer_songs     = sorted_songs[-3:]
        newer_media     = {
            "Games":    newer_games,
            "Movies":   newer_movies,
            "TV Shows": newer_tv_shows,
            "Songs":    newer_songs
        }
        return newer_media


def choose_media_by_length():
    sorted_games    = [*dict(sorted(media.games.items(), key=lambda item: item[1]["length"])).keys()]
    sorted_movies   = [*dict(sorted(media.movies.items(), key=lambda item: item[1]["length"])).keys()]
    sorted_tv_shows = [*dict(sorted(media.tv_shows.items(), key=lambda item: item[1]["length"])).keys()]
    sorted_songs    = [*dict(sorted(media.songs.items(), key=lambda item: item[1]["length"])).keys()]

    print("All right, we'll choose something based on its length.")
    print("Are you looking for something:")
    choice = input("a) Shorter\nb) Longer\n").lower()

    if choice == "a":
        print("Finding something shorter...")
        shorter_games     = sorted_games[:3]
        shorter_movies    = sorted_movies[:3]
        shorter_tv_shows  = sorted_tv_shows[:3]
        shorter_songs     = sorted_songs[:3]
        shorter_media     = {
            "Games":    shorter_games,
            "Movies":   shorter_movies,
            "TV Shows": shorter_tv_shows,
            "Songs":    shorter_songs
        }
        return shorter_media
    else:
        print("Finding something longer...")
        longer_games     = sorted_games[-3:]
        longer_movies    = sorted_movies[-3:]
        longer_tv_shows  = sorted_tv_shows[-3:]
        longer_songs     = sorted_songs[-3:]
        longer_media     = {
            "Games":    longer_games,
            "Movies":   longer_movies,
            "TV Shows": longer_tv_shows,
            "Songs":    longer_songs
        }
        return longer_media


def choose_media_by_genre():
    genres = utils.group_genres()
    print(dedent(
        """
        All right, we'll choose something based on its genre.
        We have a huge selection of genres across multiple forms of media,
        so don't worry about choosing anything too specific.
        Just choose whatever sounds most appealing to you right now!
        """
    ))
    print("Let's start by choosing some genres to narrow down your options.")
    
    for i in range(len(genres)):
        print(f"{i+1}) {genres[i].capitalize()}")

    choice = genres[int(input("Enter the number of a genre you're interested in: ")) - 1]
    related_genres = utils.find_related_genres(choice)
    # Right now it just returns the related genres, not the related titles
    return related_genres


def choose_sort(metric):
    if metric == "year":
        return choose_media_by_year()
    elif metric == "genre":
        return choose_media_by_genre()
    elif metric == "length":
        return choose_media_by_length()


def narrow_down_choices():
    print("Not sure what to choose? No problem!")
    print("Let's use another metric to narrow down your choices.")
    metric = choose_metric()
    return choose_sort(metric)


def narrow_down_single_media_type():
    pass


def run():
    greet()
    print("Let's start by figuring out what kind of entertainment you're in the mood for.")
    print("What kind of media should we look at?")
    media_type = choose_media_type()
    if type(media_type) == str:
        print(f"All right! Let's take a look at some {media_type if media_type != 'tv_shows' else 'tv shows'}!")
        #? to-do: narrow_down_single_media_type()
    else:
        print("All right, based on your input, we've found a few options:")
        print(media_type)


if __name__ == "__main__":
    run()