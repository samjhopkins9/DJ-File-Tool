#!/usr/bin/python3

import eyed3
import webbrowser as web

all_songs = {}
all_files = {}
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
"Deep/Chill House": deep_chill_house,
"Drum & Bass": drum_and_bass,
"Future Bass/Chillstep": futurebass_chillstep,
"Hits/Throwbacks": hits_throwbacks,
"Rap/R&B": rap_rnb,
"Tech/Bass House": tech_bass_house,
"Trance/Progressive House": trance_progressive_house,
"Trap/Midtempo": trap_midtempo,
"REDWAVE.": redwave,
"All": all_songs
}

c = 1
n = 1
class Song:
    def __init__(self, title, artists, playlists, downloaded = False, filename = ""):
        global c
        self.title = title
        self.artists = artists
        self.playlists = playlists
        if filename != "":
            self.downloaded = True
        self.downloaded = downloaded
        self.file = filename
        all_songs[c] = self
        for p in playlists:
            playlist[p][c] = self
        c += 1
    def __repr__(self):
        artist_string = ""
        if type(self.artists) == str:
            artist_string = self.artists
        else:
            for a in self.artists:
                artist_string += a
                if a is self.artists[-2]:
                    artist_string += " & "
                elif a is not self.artists[-1]:
                    artist_string += ", "
        return ("{artists} - {title}".format(artists = artist_string, title = self.title))
    def filename(self):
        artist_string = ""
        if type(self.artists) == str:
            artist_string = self.artists
        else:
            for a in self.artists:
                artist_string += a
                if a is self.artists[-2]:
                    artist_string += " & "
                elif a is not self.artists[-1]:
                    artist_string += ", "
        return ("{artists} - {title}".format(artists = artist_string, title = self.title))

def songid(title, artists):
    for n, s in all_songs.items():
        if s.title == title and s.artists == artists:
            return n

def song(title, artists):
    return all_songs[songid(title, artists)]
    
def play(title, artists):
    insong = song(title, artists)
    if insong.downloaded == False:
        print("Song is not downloaded.")
    else:
        web.open(insong.file)

def download(title, artists, filename = ""):
    insong = song(title, artists)
    insong.downloaded = True
    insong.file = filename
   
def print_downloaded_songs():
    c = 0
    for i in all_songs.values():
        if i.downloaded == True:
            c += 1
            print(i)
    print(str(c) + " downloaded songs")

def print_undownloaded_songs():
    c = 0
    for i in all_songs.values():
        if i.downloaded == False:
            c += 1
            print(i)
    print(str(c) + " undownloaded songs")

def search_song(title, artists):
    artists_string = ""
    if type(artists) == str:
        artists_string = artists
    else:
        artists_string = artists[-1]
    # web.open_new("https://music.amazon.com/search/{t1} {a1}?filter=IsLibrary%7Cfalse&sc=none".format(t1=title, a1=artists_string))
    web.open_new("https://www.amazon.com/s?k={a1}+{t1}&i=digital-music&crid=J8V6U287ZTGH&sprefix={a1}+{t1}%2Cdigital-music%2C83&ref=nb_sb_noss_1".format(t1=title, a1=artists_string))
    
def search_undownloaded_songs():
    for i in all_songs.values():
        if i.downloaded == False:
            search_song(i.title, i.artists)
            
def find_songs(artist1):
    songs = []
    for s in all_songs.values():
        if type(s.artists) == str:
            if s.artists == artist1:
                songs.append(s)
        else:
            for i in s.artists:
                if i == artist1:
                    songs.append(s)
    print("{size} songs by {artist}".format(size=len(songs), artist=artist1))
    for i in songs:
        print(i)

def find_duplicates():
    duplicates = []
    for s in all_songs.values():
        if len(s.playlists) > 1:
            duplicates.append(s)
    for s in duplicates:
        print(s)
        print(s.playlists)
    
def print_playlist(string):
    p1 = playlist[string]
    print(string)
    for id, song in p1.items():
        print(song)
    print("{size} songs".format(size=len(p1)))

# Old Files
Song("FOUNDATION", "BRONSON", ["REDWAVE."])
Song("Heart Attack (feat. lau.ra)", "BRONSON", ["REDWAVE."])
Song("BLINE", "BRONSON", ["REDWAVE."])
Song("KNOW ME (feat. Gallant)", "BRONSON", ["REDWAVE."])
Song("CONTACT", "BRONSON", ["REDWAVE."])
Song("DAWN (feat. Totally Enormous Extinct Dinosaurs", "BRONSON", ["REDWAVE."])
Song("Falls (feat. Sasha Alex Sloan) [Golden Features Remix]", ["Golden Features", "ODESZA"], ["REDWAVE."])
Song("Underwater", "RÜFÜS DU SOL", ["REDWAVE."])
Song("Next To Me", "RÜFÜS DU SOL", ["REDWAVE."])
Song("Alive", "RÜFÜS DU SOL", ["REDWAVE."])
Song("Alive (Reprise)", "RÜFÜS DU SOL", ["REDWAVE."])
Song("On My Knees", "RÜFÜS DU SOL", ["REDWAVE."])
Song("Wildfire", "RÜFÜS DU SOL", ["REDWAVE."])
Song("Surrender (feat. Curtis Harding)", "RÜFÜS DU SOL", ["REDWAVE."])
Song("Devotion", "RÜFÜS DU SOL", ["REDWAVE."])
Song("Can't Sleep", "Above & Beyond", ["REDWAVE.", "Trance/Progressive House"])
Song("Flimic", "Above & Beyond", ["REDWAVE."])
Song("Worlds Apart (feat. Kerli) [Seven Lions 1999 Remix]", "Seven Lions", ["REDWAVE.", "Trance/Progressive House"])
Song("Alchemy (feat. Zoë Johnston)", "Above & Beyond", ["REDWAVE.", "Trance/Progressive House"])
Song("Sun & Moon (feat. Richard Bedford)", "Above & Beyond", ["REDWAVE.", "Trance/Progressive House"])
Song("Black Room Boy", "Above & Beyond", ["REDWAVE.", "Trance/Progressive House"])
Song("Thing Called Love (feat. Richard Bedford)", "Above & Beyond", ["REDWAVE.", "Trance/Progressive House"])
Song("We're All We Need (feat. Zoë Johnston)", "Above & Beyond", ["REDWAVE.", "Trance/Progressive House"])
Song("Another Angel", "Above & Beyond", ["REDWAVE.", "Trance/Progressive House"])
Song("Long Way From Home (feat. RBBTS)", ["Above & Beyond", "Spencer Brown"], ["REDWAVE.", "Trance/Progressive House"])
Song("Worlds Apart (feat. Kerli) [Seven Lions 1999 Remix]", "Seven Lions", ["REDWAVE.", "Trance/Progressive House"])
Song("The Last Goodbye (feat. Bettye LaVette)", "ODESZA", ["REDWAVE."])

# New Files
Song("Equal (feat. Låpsley)", "ODESZA", ["REDWAVE."])
Song("I Can't Sleep", "ODESZA", ["REDWAVE."])
Song("Light Of Day (feat. Ólafur Arnolds)", "ODESZA", ["REDWAVE."])
Song("Stuck", ["Spencer Brown", "Marieme"], ["REDWAVE.", "Trance/Progressive House"])
Song("LOW", ["Oliver Heldens", "Tchami", "Anabel Englund"], ["REDWAVE.", "Tech/Bass House"])
Song("Turn Off The Lights Again (feat. Future)", ["Fred again..", "Swedish House Mafia"], ["REDWAVE.", "Deep/Chill House"])
Song("Freeze (John Summit Remix)", ["John Summit", "Kygo"], ["REDWAVE.", "Deep/Chill House"])
Song("Nova", ["Noisia", "Camo & Krooked"], ["REDWAVE.", "Drum & Bass"])
Song("Shift", ["Noisia", "IMANU"], ["REDWAVE.", "Drum & Bass"])
Song("Horizon (feat. Noisia, thys & Sleepnet)", "Skrillex", ["REDWAVE.", "Drum & Bass"])
Song("Cleansing", ["Noisia", "Former"], ["REDWAVE."])
Song("Scrapped", "Noisia", ["REDWAVE."])
Song("Halcyon", ["Noisia", "The Upbeats"], ["REDWAVE.", "Drum & Bass"])
Song("Wordless", ["Noisia", "Halogenix"], ["REDWAVE.", "Drum & Bass"])
Song("Caps Lock", ["Noisia", "Black Sun Empire"], ["REDWAVE.", "Drum & Bass"])
Song("Supersonic (Vip)", ["Noisia", "Skrillex", "josh pan", "Dylan Brady"], ["REDWAVE.", "Drum & Bass"])
Song("Divide & Conquer (Noisia Remix)", ["Noisia", "What So Not"], ["REDWAVE."])
Song("Program (Sleepnet Remix)", ["Sleepnet", "Noisia", "Phace"], ["REDWAVE."])
Song("My World (feat. Giovanca) [Jon Casey Remix]", ["Jon Casey", "Noisia"], ["REDWAVE."])
Song("Shellshock (feat. Foreign Beggars) [Synergy Remix]", ["Synergy", "Noisia"], ["REDWAVE."])
Song("Overture", ["Camo & Krooked", "Mefjus"], ["REDWAVE."])
Song("Temper", ["IMANU", "Lia"], ["REDWAVE."])
Song("Pillow Talk (feat. What So Not)", ["IMANU", "Wingtip"], ["REDWAVE."])
Song("Empress", "IMANU", ["REDWAVE.", "Drum & Bass"])
Song("Need & Pleasure", "Blanke", ["REDWAVE.", "Drum & Bass"])
Song("Surface", "Blanke", ["REDWAVE.", "Drum & Bass"])
Song("Contact", ["ATLiens", "Blanke"], ["REDWAVE.", "Trap/Midtempo"])
Song("Flatline (feat. Calivania)", "Blanke", ["REDWAVE.", "Future Bass/Chillstep"])
Song("Watch Me (feat. Syrene Favero) [Jon Casey Remix]", ["Jon Casey", "The Upbeats"], ["REDWAVE."])
Song("Presudeos", "Alon Mor", ["REDWAVE."])
Song("Los Recuerdos", "Alon Mor", ["REDWAVE."])
Song("Farewell", "Buunshin", ["REDWAVE.", "Drum & Bass"])
Song("I'm Okay", ["Buunshin", "Idle Days"], ["REDWAVE.", "Drum & Bass"])
Song("Fade", "Shadient", ["REDWAVE."])
Song("Collider", "Shadient", ["REDWAVE."])
Song("Highest Building (feat. Oklou)", "Flume", ["REDWAVE."])
Song("I Can't Tell (feat. LAUREL)", "Flume", ["REDWAVE."])
Song("Get U", "Flume", ["REDWAVE."])
Song("Sirens (feat. Caroline Polachek)", "Flume", ["REDWAVE."])
Song("Crawl Outta Love (feat. Annika Wells)", "ILLENIUM", ["REDWAVE."])
Song("Take Me Daydreaming and Don't Look Backwards", "Jaron", ["REDWAVE."])
Song(">1000 [Miles]", "Jaron", ["REDWAVE."])
Song("Love [in Every Single Way", "Jaron", ["REDWAVE."])
Song("See You Go (feat. Courtney Paige Nelson)", "Moore Kismet", ["REDWAVE."])
Song("I Miss You More Than You Think (feat. Lunamatic)", "Moore Kismet", ["REDWAVE."])
Song("Rumor (feat. WYN)", "Moore Kismet", ["REDWAVE."])
Song("Wasteland", "Moore Kismet", ["REDWAVE."])
Song("Progress (Interlude)", "Moore Kismet", ["REDWAVE."])
Song("Flourish", ["Moore Kismet", "Laxcity"], ["REDWAVE."])
Song("Vendetta For Cupid (feat. Tygko)", "Moore Kismet", ["REDWAVE."])
Song("Blame Myself (Moore Kismet Remix)", ["Moore Kismet", "ILLENIUM", "Tori Kelly"], ["REDWAVE."])
Song("Prologue", ["Slumberjack", "Oddly Godly"], ["REDWAVE."])
Song("Arc Second", ["Slumberjack", "TINYKVT"], ["REDWAVE."])
Song("Inferno (feat. ShockOne & HWLS)", ["Slumberjack", "TWERL", "Loston"], ["REDWAVE."])
Song("Athena", "Slumberjack", ["REDWAVE."])
Song("Ripper", ["Mr. Carmack", "Shanghai Doom"], ["REDWAVE."])
Song("Ritual", ["AWAY", "Echoes"], ["REDWAVE."])
Song("Honest To Gød (feat. Charity)", "AWAY", ["REDWAVE."])
Song("Amends", "Laxcity", ["REDWAVE."])
Song("Stay with Me", "Kasbo", ["REDWAVE."])
Song("All Or Nothing", "Hex Cougar", ["REDWAVE."])
Song("Emoboy303 (SIDE)", "Leotrix", ["REDWAVE."])
Song("Heart Tones", "Leotrix", ["REDWAVE."])
Song("Lovin U", "Leotrix", ["REDWAVE."])
Song("Rising", "Duskus", ["REDWAVE."])
Song("To Ü (feat. AlunaGeorge)", ["Jack Ü", "Skrillex", "Diplo"], ["REDWAVE."])
Song("Lemniscate (The Place Between Sleeping and Awake)", "Crywolf", ["REDWAVE."])
Song("I'll Be Fine (Zes Remix)", ["Zes", "Sofie Letitre"], ["REDWAVE."])
Song("Stay", "Kaivon", ["REDWAVE."])
Song("Pressure", "RL Grime", ["REDWAVE.", "Trap/Midtempo"])
Song("Answers", "Au5", ["REDWAVE."])
Song("Never Enough", "Two Lanes", ["REDWAVE."])
Song("After Hours", "The Weeknd", ["REDWAVE."])
Song("United In Grief", "Kendrick Lamar", ["REDWAVE."])
Song("Silent Hill", ["Kendrick Lamar", "Kodak Black"], ["REDWAVE.", "Rap/R&B"])
Song("1st Quarter (feat. REASON)", "Denzel Curry", ["REDWAVE."])
Song("Melt Session #1 (feat. Robert Glasper)", "Denzel Curry", ["REDWAVE."])
Song("The Last", "Denzel Curry", ["REDWAVE."])
Song("Mental (feat. Saul Williams & Bridget Perez)", "Denzel Curry", ["REDWAVE."])
Song("X-Wing", "Denzel Curry", ["REDWAVE."])
Song("Zatoichi", ["Denzel Curry", "slowthai"], ["REDWAVE."])
Song("F*ck Up Some Commas", "Future", ["REDWAVE.", "Rap/R&B"])
Song("I'M DAT N****", "Future", ["REDWAVE.", "Rap/R&B"])
Song("KEEP IT BURNIN (feat. Kanye West)", "Future", ["REDWAVE.", "Rap/R&B"])
Song("PUFFIN ON ZOOTIEZ", "Future", ["REDWAVE."])
Song("VOODOO (feat. Kodak Black)", "Future", ["REDWAVE."])
Song("HOLY GHOST", "Future", ["REDWAVE."])
Song("Survivor's Guilt (feat. G Herbo)", "Saba", ["REDWAVE.", "Rap/R&B"])
Song("Still (feat. Smino & 6LACK)", "Saba", ["REDWAVE."])
Song("Soldier (feat. Pivot Gang)", "Saba", ["REDWAVE."])
Song("If I Had A Dollar (feat. Benjamin Earl Turner)", "Saba", ["REDWAVE.", "Rap/R&B"])
Song("Few Good Things (feat. Black Thought & Eryn Allen Kane)", "Saba", ["REDWAVE."])
Song("Freestyle", "Lil Baby", ["REDWAVE."])
Song("MAFIA", "Travis Scott", ["REDWAVE."])

# download("FOUNDATION", "BRONSON", "01 - FOUNDATION_0f7b2b51-2a1f-4301-9455-1db0b61fdc16.mp3")

download("Silent Hill", ["Kendrick Lamar", "Kodak Black"], "(Disc 2) 03 - Silent Hill [Explicit]_e0632c21-af0d-45fa-b57c-86d71ae9b7a9.mp3")
download("All Or Nothing", "Hex Cougar", "01 - All Or Nothing_00e1cea6-cb6d-4245-9fef-aed845476a13.mp3")
download("Honest To Gød (feat. Charity)", "AWAY", "01 - Honest To Gød (feat. Charity)_5c0957a9-8f00-4063-a1c5-aa12e2080cc2.mp3")
download("Inferno (feat. ShockOne & HWLS)", ["Slumberjack", "TWERL", "Loston"], "01 - Inferno_7b498df9-cd15-4253-b4d4-c64c917534d6.mp3")
download("Lemniscate (The Place Between Sleeping and Awake)", "Crywolf", "01 - Lemniscate (The Place Between Sleeping and Awake)_ee307721-0eb4-49c3-b77a-e61792d8d7a7.mp3")
download("Melt Session #1 (feat. Robert Glasper)", "Denzel Curry", "01 - Melt Session #1 [feat. Robert Glasper] [Explicit]_75bf7f95-3e9b-48ce-8211-423d7aa422dd.mp3")
download("Prologue", ["Slumberjack", "Oddly Godly"], "01 - Prologue_6df42634-7816-48e8-92a4-67ba1abbe4b7.mp3")
download("Ripper", ["Mr. Carmack", "Shanghai Doom"], "01 - Ripper_2c847bd2-f29e-441a-984e-6a292f558248.mp3")
download("Ritual", ["AWAY", "Echoes"], "01 - Ritual_474ba40d-2a33-42b4-a08b-3a8675b2e2b2.mp3")
download("Stay", "Kaivon", "01 - Stay_bb4b0a73-fce0-4b93-861c-ddc9eefba5f0.mp3")
download("Temper", ["IMANU", "Lia"], "01 - Temper_3100c22e-881e-413e-a8b0-b895080bfc89.mp3")
download("United In Grief", "Kendrick Lamar", "01 - United In Grief [Explicit]_e94af39d-668e-4a5f-81e2-2c4d442edcc6.mp3")
download("Amends", "Laxcity", "01 - ‎amends_707f8f80-97db-494b-b832-50e9d17a2d20.mp3")
download("Answers", "Au5", "02 - Answers (Extended Mix)_904bee73-14db-4412-a9b0-44712f9abd45.mp3")
download("Athena", "Slumberjack", "02 - Athena_47e84e01-7c7c-417c-aa67-d39304cba4e3.mp3")
download("I'M DAT N****", "Future", "02 - I'M DAT N____ [Explicit]_c8cbc09c-f66b-4979-ac2f-e4fc60199e83.mp3")
download("Blame Myself (Moore Kismet Remix)", ["Moore Kismet", "ILLENIUM", "Tori Kelly"], "03 - Blame Myself (Moore Kismet Remix)_9d0b2c2b-36c2-48ca-afd3-347651f007dd.mp3")
download("Heart Tones", "Leotrix", "03 - Heart Tones_710d3146-953f-4d02-9203-fbfc612f3eba.mp3")
download("KEEP IT BURNIN (feat. Kanye West)", "Future", "03 - KEEP IT BURNIN [Explicit]_9fb83eb8-2563-4b46-af9b-71af3e8aa9e2.mp3")
download("Lovin U", "Leotrix", "03 - Lovin U_24100d59-8d3e-40ec-9d54-7acafde0a237.mp3")
download("See You Go (feat. Courtney Paige Nelson)", "Moore Kismet", "03 - See You Go [feat. Courtney Paige Nelson]_a07f3dd8-4b79-4e46-ac9f-b5120213fccd.mp3")
download("Emoboy303 (SIDE)", "Leotrix", "04 - Emoboy303 (SIDE)_c16f25a1-be57-45e4-98b4-c6e1cb2d1b09.mp3")
download("I Miss You More Than You Think (feat. Lunamatic)", "Moore Kismet", "04 - I Miss You More Than You Think [feat. Lunamatic] [Explicit]_462fff80-5525-4ae5-891c-fcf9f65536c3.mp3")
download("PUFFIN ON ZOOTIEZ", "Future", "05 - PUFFIN ON ZOOTIEZ [Explicit]_50c76200-f0a9-49e8-8610-ca81fdc8ac48.mp3")
download("Rumor (feat. WYN)", "Moore Kismet", "05 - Rumor [feat. WYN]_149bd3c1-1d4c-42bf-b910-329102e13e67.mp3")
download("The Last", "Denzel Curry", "05 - The Last [Explicit]_8c1f08ef-f9c4-41c0-b1b5-42571c589b96.mp3")
download("To Ü (feat. AlunaGeorge)", ["Jack Ü", "Skrillex", "Diplo"], "05 - To Ü (feat. AlunaGeorge)_ee7f73c2-ce19-4fd7-8982-0323baeb5b9e.mp3")
download(">1000 [Miles]", "Jaron", "05 - _1000 [miles]_400b449d-b0f9-4b13-8289-8434fb216a41.mp3")
download("Mental (feat. Saul Williams & Bridget Perez)", "Denzel Curry", "06 - Mental [feat. Saul Williams & Bridget Perez] [Explicit]_4950e42d-285e-4fa2-9197-12ac923e5298.mp3")
download("Stay with Me", "Kasbo", "06 - Stay With Me_0f1a7745-83d5-4c6e-976b-13c67f308f16.mp3")
download("Arc Second", ["Slumberjack", "TINYKVT"], "07 - Arc Second_f9ac2fb1-bb81-432d-9b36-b44772073155.mp3")
download("I'll Be Fine (Zes Remix)", ["Zes", "Sofie Letitre"], "07 - I'll Be Fine (Zes Remix)_2fd88520-aa6d-4a5e-a1a7-de118ea8fd8a.mp3")
download("Still (feat. Smino & 6LACK)", "Saba", "07 - Still (feat. 6LACK and Smino) [Explicit]_9424a44d-1def-407c-9777-1fd24e41d9b6.mp3")
download("The Last Goodbye (feat. Bettye LaVette)", "ODESZA", "08 - The Last Goodbye (feat. Bettye LaVette)_a937e28f-2bd9-446a-bc2d-ce2a2aede64b.mp3")
download("Soldier (feat. Pivot Gang)", "Saba", "09 - Soldier (feat. Pivot Gang) [Explicit]_c3cbbac0-259a-48c1-badf-a6ceea722c6c.mp3")
download("X-Wing", "Denzel Curry", "09 - X-Wing [Explicit]_918af6ce-dc29-4e41-9fd3-78fa59ccce51.mp3")
download("If I Had A Dollar (feat. Benjamin Earl Turner)", "Saba", "10 - If I Had A Dollar (feat. Benjamin Earl Turner) [Explicit]_7397b177-6faa-4538-8820-9963cb4c4b53.mp3")
download("VOODOO (feat. Kodak Black)", "Future", "12 - VOODOO [Explicit]_966af0e8-9942-49cf-87aa-86496572a0ba.mp3")
download("After Hours", "The Weeknd", "13 - After Hours_2d53df15-ea6d-4cf5-bf1f-4a4333a62b89.mp3")
download("Freestyle", "Lil Baby", "13 - Freestyle [Explicit]_70419102-2f37-458a-904b-05b9ebbb436f.mp3")
download("HOLY GHOST", "Future", "13 - HOLY GHOST [Explicit]_f1101367-ef47-46e0-b315-8116085d77d2.mp3")
download("Zatoichi", ["Denzel Curry", "slowthai"], "13 - Zatoichi [Explicit]_f7050fac-2742-4542-82fd-3e356fc2bf27.mp3")
download("Few Good Things (feat. Black Thought & Eryn Allen Kane)", "Saba", "14 - Few Good Things (feat. Black Thought and Eryn Allen Kane) [Explicit]_84fa1f26-e14b-426f-b68e-70466a726429.mp3")
download("F*ck Up Some Commas", "Future", "18 - F_ck Up Some Commas [Explicit]_41adf26f-dd87-4376-94bd-db0154876c95.mp3")

# play("FOUNDATION", "BRONSON")
# find_songs("Future")
# find_duplicates()
# print_playlist("Rap/R&B")
# print_undownloaded_songs()
# find_undownloaded_songs()

all_files[n] = eyed3.load("../../../new_mp3s/" + "13 - Zatoichi [Explicit]_f7050fac-2742-4542-82fd-3e356fc2bf27.mp3")
Song(all_files[n].tag.title, all_files[n].tag.artist, ["REDWAVE."], all_files[n])
print(all_files[n].tag.artist + " - " + all_files[n].tag.title)
n += 1
