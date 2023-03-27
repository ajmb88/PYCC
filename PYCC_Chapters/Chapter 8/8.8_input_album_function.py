def create_album(artist, title, genre=''):
    """Use input to create and display a dictionary of an album."""
    album = {'Artist': artist, 'Title': title}
    if genre:
        album['Genre'] = genre

    print(album)

while True:

    artist_name = input("\nBuild your own album!!! Enter your Artist Name, or press "
                        "'q' at anytime to quit: ")
    if artist_name.lower() == 'q':
        break
    else:
        artist = artist_name.title()


    title_name = input(f"Now, what's the name of your Album?!??: ")
    if title_name.lower() == 'q':
        break
    else:
        title = title_name.title()


    possible_genre = input("Do you have a style in mind yet?? Enter, it or just type 'n' "
                         "to continue: ")
    if possible_genre.lower() == 'q':
        break
    elif possible_genre.lower() == 'n':
        pass
    else:
        genre = possible_genre.title()


    create_album(artist, title, genre)

