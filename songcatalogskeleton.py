#!/usr/bin/python3

import eyed3
import webbrowser as web

all_songs = {}
deep_chill_house = {}
drum_and_bass = {}
futurebass_chillstep = {}
hits_throwbacks = {}
rap_rnb = {}
tech_bass_house = {}
trance_progressive_house = {}
trap_midtempo = {}
redwave = {}
playlist = {
    "Deep_ChillHouse": deep_chill_house,
    "Drum&Bass": drum_and_bass,
    "FutureBass_Chillstep": futurebass_chillstep,
    "Hits_Throwbacks": hits_throwbacks,
    "Rap_R&B": rap_rnb,
    "Tech_BassHouse": tech_bass_house,
    "Trance_ProgressiveHouse": trance_progressive_house,
    "Trap_Midtempo": trap_midtempo,
    "REDWAVE.": redwave,
    "All": all_songs
}

c = 1
class Song:
    def __init__(self, title, artists, filename = "", file = ""):
        global c
        self.title = title
        self.artists = artists
        self.filename = filename
        self.file = file
        # self.file1 = file[17:]
        self.keynum = c
        all_songs[c] = self
        self.downloaded = False
        if self.file != "":
            self.downloaded = True
        self.playlists = []
        self.sorted = False
        c += 1
    def __repr__(self):
        return ("{artists} - {title}".format(artists = self.artists, title = self.title))
    def addto_playlists(self):
        for p in self.playlists:
            playlist[p][self.keynum] = self
            self.sorted = True
            
def load_song(filename):
    # filename = "../../../new_mp3s/" + filename
    global c
    ts = eyed3.load(filename)
    Song(ts.tag.title, ts.tag.artist, filename, ts)

def sort_song(ss):
    print(ss)
    print("Playlists")
    print("1. Deep/Chill House")
    print("2. Drum & Bass")
    print("3. Future Bass/Chillstep")
    print("4. Hits/Throwbacks")
    print("5. Rap/R&B")
    print("6. Tech/Bass House")
    print("7. Trance/Progressive House")
    print("8. Trap/Midtempo")
    print("9. REDWAVE.")
    pln = input("How many playlists would you like to add this song to?: ")
    range1 = int(pln)
    ssp = []
    ss.playlists.append("All")
    for _ in range(range1):
        i = input("Enter playlist: ")
        if i == "1":
            ss.playlists.append("Deep_ChillHouse")
        elif i == "2":
            ss.playlists.append("Drum&Bass")
        elif i == "3":
            ss.playlists.append("FutureBass_Chillstep")
        elif i == "4":
            ss.playlists.append("Hits_Throwbacks")
        elif i == "5":
            ss.playlists.append("Rap_R&B")
        elif i == "6":
            ss.playlists.append("Tech_BassHouse")
        elif i == "7":
            ss.playlists.append("Trance_ProgressiveHouse")
        elif i == "8":
            ss.playlists.append("Trap_Midtempo")
        elif i == "9":
            ss.playlists.append("REDWAVE.")
    ss.addto_playlists()
    ss.sorted = True
    
def songid1(filename):
    for n, s in all_songs.items():
        if s.filename == filename:
            return n
   
def song1(filename):
    return all_songs[songid1(filename)]

