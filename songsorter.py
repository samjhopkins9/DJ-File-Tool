#!/usr/bin/python3
playlists = []

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
    print("10. REDWAVE.")
    pln = input("How many playlists would you like to add this song to?: ")
    range1 = int(pln)
    playlists.append("All")
    for _ in range(range1):
        i = input("Enter playlist: ")
        if i == "1":
            playlists.append("Hits_Throwbacks")
        elif i == "2":
            playlists.append("Rap")
        elif i == "3":
            playlists.append("Deep_ChillHouse")
        elif i == "4":
            playlists.append("Tech_BassHouse")
        elif i == "5":
            playlists.append("Trance_ProgHouse")
        elif i == "6":
            playlists.append("Trap_Dubstep")
        elif i == "7":
            playlists.append("Drum&Bass")
        elif i == "8":
            playlists.append("Other")
        elif i == "9":
            playlists.append("Original")
        elif i == "10":
            playlists.append("REDWAVE.")
        else:
            print("Invalid choice. Try again.")
            sort_song(song);

