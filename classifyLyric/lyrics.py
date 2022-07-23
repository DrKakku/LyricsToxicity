from curses.ascii import isupper
import lyricsgenius as lg

genius = lg.Genius('', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

def get_lyrics(song:str )->str:
    """
    gets either song and or the artist for the song and the returns the lyrics for the same
    
    Keyword arguments:
    song -- Name of the song 
    artist -- Name of the artist who made the song

    Return: lyrics to the song specified for the artist
    """

    # if artist != "":
    #     artistList = genius.search_artist(artist,max_songs=100)
    #     song = artistList.song(song)
    # else:
    ##indent below
    song = genius.search_song(song)

    lyrics = song.lyrics
    lyrics = lyrics.split("\n")
    lyrics = ' '.join(lyrics)

    #TO DO
    ## Identify and translate the Lyrics form X lang to English


    return lyrics

def insert_break(string, index):
    return string[:index] + '\n' + string[index:]

def beautifyLyrics(lyr:str)->str:
    newLyr = lyr
    insertcount = 0
    for i in range(len(lyr)):
        if lyr[i].isupper():
            print(lyr[i-3:i+3])
            if lyr[i-1] in "()[]":
                newLyr = insert_break(newLyr,i-2+insertcount)
            else:
                newLyr = insert_break(newLyr,i-1+insertcount)
            insertcount +=1
    return newLyr.replace('\n',"<br>")

