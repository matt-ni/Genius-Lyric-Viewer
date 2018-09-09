#Libraries and important info.
# Time for pauses, lyricsgenius - self-explanitory, api key, and welcome message.
import time
import lyricsgenius as genius
api = genius.Genius("b9oy4hrgqBbeeFyjWIpXE6XVp17c1ree-2XAm-ixJLt3_bt3wOf42Lyjlyas3uno")
print ("Welcome to the Lyrics Viewer. Please choose a song.")
time.sleep(2)

# Function to repeat song search if needed
def lyrics_search():
    while True:
        print ("Choose a song.")
        songnumber = input("""1. Reese LAFLARE - Stutter (feat. Yung Bans), 
2. G Herbo - Malcolm, 
3. Kap G - Marvelous Day (feat. Gunna & Lil Uzi Vert)
4. A song of your choice
        """)
        # Pre-made options. Self explanitory.
        if songnumber == str(1):
            song = api.search_song("Stutter", "Reese LAFLARE")
        elif songnumber == str(2):
            song = api.search_song("Malcolm", "G Herbo")
        elif songnumber == str(3):
            song = api.search_song("Marvelous Day", "Kap G")
        elif songnumber == str(4):
            # This option will allow the user to enter their own choice.
            artist = input("What artist? ")
            time.sleep(2)
            songname = input("What song? ")
            time.sleep(2)
            song = api.search_song(songname, artist)
        else:
            print("Wrong. Try again.")
            time.sleep(2)
            continue
        # Repeats code if song is not first result
        try:
            print(song.lyrics)
        except AttributeError:
            print("Sorry! That song is not the first result. Try again.")
            time.sleep(2)
            continue
            time.sleep(5)
        another_song()

#Function incase answer for "another song" prompt is not "Yes" or "No".
def another_song():
    while True:
        # Program asks user if they want to search again
        another_song = input("Would you like to look for another song? Yes or no? ")
        if another_song == "Yes":
            lyrics_search()
        elif another_song == "No":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid answer. Please try again.")
            continue

#Function called on to activate search
lyrics_search()
