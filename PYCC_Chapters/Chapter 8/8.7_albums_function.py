def make_album(artist, title, song_count = ''):
    """Build and display a dictionary about an album."""
    album = {'Artist': artist, 'Title': title}
    if song_count:
        album['Song Count'] = song_count

    return album

rap = make_album('Jay-Z', 'the black album', '22')
print(f"\n{rap}")

rock = make_album('red hot chilli peppers', 'suck my kiss')
print(f"\n{rock}")

elec = make_album('daft punk', 'tron', '14')
print(f"\n{elec}")