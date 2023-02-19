#!/usr/bin/python3


# Playlists array is declared empty, to contain names of playlists to add a song file to
playlists = []

# Function takes a song filename as an input, prints its name, and prompts the user to select which playlist folders they would like to add it to, and how many. It then adds the names of the folders to the playliss array, which later is read by the Bash script and used to copy the songs into organized directories.
def sort_song(song):

    print(song)
    print("Playlists")
    
    print("1. Hits/Throwbacks")
    print("2. Rap")
    print("3. Deep/Chill House")
    print("4. Tech/Bass House")
    print("5. Trance/Prog House")
    print("6. Trap/Dubstep")
    print("7. Drum & Bass")
    print("8. Other")
    print("9. Originals")
    
    
    # All songs are automatically added to 'All' playlist
    playlists.append("All")
    
    i = input("Enter playlist: ")
        
    if i == "1":
        playlists.append("Hits_Throwbacks")
        return
        
    elif i == "2":
        playlists.append("Rap")
        return
        
    elif i == "3":
        playlists.append("Deep_ChillHouse")
        return

    elif i == "4":
        playlists.append("Tech_BassHouse")
        return

    elif i == "5":
        playlists.append("Trance_ProgHouse")
        return

    elif i == "6":
        playlists.append("Trap_Dubstep")
        return

    elif i == "7":
        playlists.append("Drum&Bass")
        return

    elif i == "8":
        playlists.append("Other")
        return

    elif i == "9":
        playlists.append("Originals")
        return

    # If a value that doesn't correspond to anything is inputted, the function is called recursively until they do
    else:
        print("Invalid choice. Try again.")
        sort_song(song)
        
# end of sort_song function
