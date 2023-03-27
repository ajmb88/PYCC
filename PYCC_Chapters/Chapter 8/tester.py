
while True:

    answer = input("\nWhat color is the sky at night?")"
    if answer.lower() == 'black':
        break
    else:
        artist = answer.title()


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

