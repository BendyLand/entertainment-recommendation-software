import media 
media_types = [media.games, media.movies, media.tv_shows, media.songs]

def extract_genres(media_type, title):
    return media_type[title]["genre"]


def filter_dictionary(dictionary, media_type):
    for single_media_type in dictionary.items():
        if single_media_type[0].lower().replace(' ', '_') == media_type:
            return single_media_type
    return "Error finding media. Please start your search over."


def group_genres():
    genres = []
    for media_type in media_types:
        media_genres = map(lambda title: extract_genres(media_type, title), media_type)
        genres += media_genres
    genres = sorted(set([x for sublist in genres for x in sublist]))
    return genres


def find_related_genres(selected_genre):
    related_genres = []
    for media_type in media_types:
        grouped_genres = sorted(list(map(lambda title: extract_genres(media_type, title), media_type)))
        for list_of_genres in grouped_genres:
            if selected_genre in list_of_genres and selected_genre in list_of_genres:
                related_genres += list_of_genres
                break
    return sorted([*set(related_genres)])

