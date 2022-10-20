#!/usr/bin/python3

import eyed3

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
    
def print_playlist(string):
    p1 = playlist[string]
    print(string)
    for id, song in p1.items():
        print(song)
    print("{size} songs".format(size=len(p1)))

load_song("../../../sorted_mp3s/All/(Disc 2) 03 - Say Go_145e3af5-c93c-4d42-975d-aa6745304b75.mp3")
song1("../../../sorted_mp3s/All/(Disc 2) 03 - Say Go_145e3af5-c93c-4d42-975d-aa6745304b75.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/(Disc 2) 03 - Silent Hill [Explicit]_e0632c21-af0d-45fa-b57c-86d71ae9b7a9.mp3")
song1("../../../sorted_mp3s/All/(Disc 2) 03 - Silent Hill [Explicit]_e0632c21-af0d-45fa-b57c-86d71ae9b7a9.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/(Disc 2) 14 - Fortress (feat. Joni Fatora) (Seven Lions Roots Mix)_4393bdb5-6261-4a3a-9a48-187b48d0e7b1.mp3")
song1("../../../sorted_mp3s/All/(Disc 2) 14 - Fortress (feat. Joni Fatora) (Seven Lions Roots Mix)_4393bdb5-6261-4a3a-9a48-187b48d0e7b1.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - 4Me_0689f91d-95ad-45c4-be4d-cf5fd744ae2b.mp3")
song1("../../../sorted_mp3s/All/01 - 4Me_0689f91d-95ad-45c4-be4d-cf5fd744ae2b.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - 5 Seconds Before Sunrise_d1871ad3-3e73-457c-ad76-17928d852e87.mp3")
song1("../../../sorted_mp3s/All/01 - 5 Seconds Before Sunrise_d1871ad3-3e73-457c-ad76-17928d852e87.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - ANGEL VOICES_dbac2fda-5d3f-42c0-bea8-51815304b407.mp3")
song1("../../../sorted_mp3s/All/01 - ANGEL VOICES_dbac2fda-5d3f-42c0-bea8-51815304b407.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - About You_087beed2-09b6-4af9-91c7-196c0ead83fb.mp3")
song1("../../../sorted_mp3s/All/01 - About You_087beed2-09b6-4af9-91c7-196c0ead83fb.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Above The Tide_5bbb13fd-3b12-469c-a1ab-cb73f5a66e36.mp3")
song1("../../../sorted_mp3s/All/01 - Above The Tide_5bbb13fd-3b12-469c-a1ab-cb73f5a66e36.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Absence of Association_fc03eaab-5c99-47ae-b639-239e16b5baaa.mp3")
song1("../../../sorted_mp3s/All/01 - Absence of Association_fc03eaab-5c99-47ae-b639-239e16b5baaa.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - After Life (feat. Stacy Barthe)_ea919dc7-606f-452d-85fa-ddce00035043.mp3")
song1("../../../sorted_mp3s/All/01 - After Life (feat. Stacy Barthe)_ea919dc7-606f-452d-85fa-ddce00035043.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Alive_25d23a1a-0635-49cc-b610-8fdba405c679.mp3")
song1("../../../sorted_mp3s/All/01 - Alive_25d23a1a-0635-49cc-b610-8fdba405c679.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - All Or Nothing_00e1cea6-cb6d-4245-9fef-aed845476a13.mp3")
song1("../../../sorted_mp3s/All/01 - All Or Nothing_00e1cea6-cb6d-4245-9fef-aed845476a13.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - All the Things I Hate About You [Explicit]_993219d2-a38a-41c5-b34f-97f199932811.mp3")
song1("../../../sorted_mp3s/All/01 - All the Things I Hate About You [Explicit]_993219d2-a38a-41c5-b34f-97f199932811.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Alone With You_1e2efceb-06bd-4927-867e-b7c93fa9b45d.mp3")
song1("../../../sorted_mp3s/All/01 - Alone With You_1e2efceb-06bd-4927-867e-b7c93fa9b45d.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Alone_6a80051d-eff9-4f21-98aa-a5c083a3a8bf.mp3")
song1("../../../sorted_mp3s/All/01 - Alone_6a80051d-eff9-4f21-98aa-a5c083a3a8bf.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Amanhã_310be24b-0129-4223-89c2-5941ffbb862e.mp3")
song1("../../../sorted_mp3s/All/01 - Amanhã_310be24b-0129-4223-89c2-5941ffbb862e.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Backup_f24baae0-bdbd-4a01-ad4f-d706f306f6ac.mp3")
song1("../../../sorted_mp3s/All/01 - Backup_f24baae0-bdbd-4a01-ad4f-d706f306f6ac.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Be Right There_239d679a-ba8d-42c0-b41d-0afcdcffdb9b.mp3")
song1("../../../sorted_mp3s/All/01 - Be Right There_239d679a-ba8d-42c0-b41d-0afcdcffdb9b.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Beautiful Heartbeat (feat. Frida Sundemo) [Radio Edit]_24653661-9f56-4100-8803-8d85b68b6eaa.mp3")
song1("../../../sorted_mp3s/All/01 - Beautiful Heartbeat (feat. Frida Sundemo) [Radio Edit]_24653661-9f56-4100-8803-8d85b68b6eaa.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Belong (Extended Mix)_bc5960b0-6575-43bb-9c1a-60dcfc95fe1f.mp3")
song1("../../../sorted_mp3s/All/01 - Belong (Extended Mix)_bc5960b0-6575-43bb-9c1a-60dcfc95fe1f.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Bill Graham_829d408b-27dd-411d-a251-616f0e5a443e.mp3")
song1("../../../sorted_mp3s/All/01 - Bill Graham_829d408b-27dd-411d-a251-616f0e5a443e.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Body_326e2f2f-8735-4769-8227-f875f99d0abd.mp3")
song1("../../../sorted_mp3s/All/01 - Body_326e2f2f-8735-4769-8227-f875f99d0abd.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Breaking the Doors (Extended Mix)_b9fd2edc-08f9-4677-81d2-f53c14e8de61.mp3")
song1("../../../sorted_mp3s/All/01 - Breaking the Doors (Extended Mix)_b9fd2edc-08f9-4677-81d2-f53c14e8de61.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Breathe 2.0_bd77b57b-24d3-446b-adbc-527ca4a64053.mp3")
song1("../../../sorted_mp3s/All/01 - Breathe 2.0_bd77b57b-24d3-446b-adbc-527ca4a64053.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Breathe_058e076e-d636-4388-b524-bb234197f054.mp3")
song1("../../../sorted_mp3s/All/01 - Breathe_058e076e-d636-4388-b524-bb234197f054.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Brothers (Extended Mix)_d7b51835-dafb-458d-84ae-be68f914c7ba.mp3")
song1("../../../sorted_mp3s/All/01 - Brothers (Extended Mix)_d7b51835-dafb-458d-84ae-be68f914c7ba.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - By Your Side (Oliver Heldens Remix)_07b66d04-cbe0-405e-b9de-a6bb299f0fb1.mp3")
song1("../../../sorted_mp3s/All/01 - By Your Side (Oliver Heldens Remix)_07b66d04-cbe0-405e-b9de-a6bb299f0fb1.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Caliente (Na Na Na)_88b82f31-670a-498e-b556-41c2a8db4925.mp3")
song1("../../../sorted_mp3s/All/01 - Caliente (Na Na Na)_88b82f31-670a-498e-b556-41c2a8db4925.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/01 - Christ Person, Woman God_e99a8670-38d3-480b-a2dd-6178385d7405.mp3")
song1("../../../sorted_mp3s/All/01 - Christ Person, Woman God_e99a8670-38d3-480b-a2dd-6178385d7405.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Chronos_fb2bc6d6-cd9f-4c1f-af45-470cdcb3bc63.mp3")
song1("../../../sorted_mp3s/All/01 - Chronos_fb2bc6d6-cd9f-4c1f-af45-470cdcb3bc63.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Closer_a8984481-f16d-40bc-b119-81aa9b6bd57f.mp3")
song1("../../../sorted_mp3s/All/01 - Closer_a8984481-f16d-40bc-b119-81aa9b6bd57f.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Coco [Explicit]_f5adcb36-e99c-4cf5-b36e-56b62e4efd12.mp3")
song1("../../../sorted_mp3s/All/01 - Coco [Explicit]_f5adcb36-e99c-4cf5-b36e-56b62e4efd12.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - Coffee (Give Me Something) [Explicit]_a91e1914-a379-476b-b735-30663654eb56.mp3")
song1("../../../sorted_mp3s/All/01 - Coffee (Give Me Something) [Explicit]_a91e1914-a379-476b-b735-30663654eb56.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Cold Heart (PNAU Remix)_0c221631-bedc-4376-b3b1-ffc10cc4bc20.mp3")
song1("../../../sorted_mp3s/All/01 - Cold Heart (PNAU Remix)_0c221631-bedc-4376-b3b1-ffc10cc4bc20.mp3").playlists = ['All', 'Deep_ChillHouse', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Cold Skin_4d0e46bd-3047-44ec-9559-bfaa25ce8162.mp3")
song1("../../../sorted_mp3s/All/01 - Cold Skin_4d0e46bd-3047-44ec-9559-bfaa25ce8162.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Coming Home (feat. Anabel Englund)_d2ee17fc-b27b-4d9a-91e9-34f872b58dcc.mp3")
song1("../../../sorted_mp3s/All/01 - Coming Home (feat. Anabel Englund)_d2ee17fc-b27b-4d9a-91e9-34f872b58dcc.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Concrete Jungle [Explicit]_3e54de01-33af-45c6-a1f7-fb8c32192a13.mp3")
song1("../../../sorted_mp3s/All/01 - Concrete Jungle [Explicit]_3e54de01-33af-45c6-a1f7-fb8c32192a13.mp3").playlists = ['All', 'Tech_BassHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Contact_753c53df-e762-4b43-a3ee-db2a91585afa.mp3")
song1("../../../sorted_mp3s/All/01 - Contact_753c53df-e762-4b43-a3ee-db2a91585afa.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Control_11e01e73-3285-40de-8d60-9075af6ea92f.mp3")
song1("../../../sorted_mp3s/All/01 - Control_11e01e73-3285-40de-8d60-9075af6ea92f.mp3").playlists = ['All', 'Trap_Midtempo']
load_song("../../../sorted_mp3s/All/01 - Cortex_55fcd396-96d1-4218-8773-65e716c135cb.mp3")
song1("../../../sorted_mp3s/All/01 - Cortex_55fcd396-96d1-4218-8773-65e716c135cb.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Cotton Eye Joe_c69b2591-d968-4b40-9648-74be4b1b6b4d.mp3")
song1("../../../sorted_mp3s/All/01 - Cotton Eye Joe_c69b2591-d968-4b40-9648-74be4b1b6b4d.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Criminals_ca083d90-c3d0-46e4-97bb-a0cceed2d18d.mp3")
song1("../../../sorted_mp3s/All/01 - Criminals_ca083d90-c3d0-46e4-97bb-a0cceed2d18d.mp3").playlists = ['All', 'Trap_Midtempo']
load_song("../../../sorted_mp3s/All/01 - DÁKITI [Explicit]_ce3b2a23-3ba4-48ca-b4a6-73bc31346fa9.mp3")
song1("../../../sorted_mp3s/All/01 - DÁKITI [Explicit]_ce3b2a23-3ba4-48ca-b4a6-73bc31346fa9.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - Daya_685e39ca-c86a-4fe3-af5f-dc6e580750ef.mp3")
song1("../../../sorted_mp3s/All/01 - Daya_685e39ca-c86a-4fe3-af5f-dc6e580750ef.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Deeper_b82b4a88-072f-4d04-82b3-946337f07209.mp3")
song1("../../../sorted_mp3s/All/01 - Deeper_b82b4a88-072f-4d04-82b3-946337f07209.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Divinity [feat. Amy Millan]_089597db-be21-4eda-9dad-5ba172bd28e9.mp3")
song1("../../../sorted_mp3s/All/01 - Divinity [feat. Amy Millan]_089597db-be21-4eda-9dad-5ba172bd28e9.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Do It To It [feat. Cherish]_9d390109-2988-4e18-8d2e-c7b28b7769c4.mp3")
song1("../../../sorted_mp3s/All/01 - Do It To It [feat. Cherish]_9d390109-2988-4e18-8d2e-c7b28b7769c4.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/01 - Doja [Explicit]_e813b335-dc54-4e56-aace-15d15fb70358.mp3")
song1("../../../sorted_mp3s/All/01 - Doja [Explicit]_e813b335-dc54-4e56-aace-15d15fb70358.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - Don't Forget My Love_e546d057-7aea-4eb5-b8b8-544e9ca46eb4.mp3")
song1("../../../sorted_mp3s/All/01 - Don't Forget My Love_e546d057-7aea-4eb5-b8b8-544e9ca46eb4.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Don't Leave Me Alone (feat. Anne-Marie) [EDX's Indian Summer Remix]_307b3169-7e40-4ce0-ac3f-147a96625cb2.mp3")
song1("../../../sorted_mp3s/All/01 - Don't Leave Me Alone (feat. Anne-Marie) [EDX's Indian Summer Remix]_307b3169-7e40-4ce0-ac3f-147a96625cb2.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Don’t Leave [feat. Ellie Goulding]_357aff5e-3045-401e-968d-4a7d26f0018c.mp3")
song1("../../../sorted_mp3s/All/01 - Don’t Leave [feat. Ellie Goulding]_357aff5e-3045-401e-968d-4a7d26f0018c.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Down [feat. Lil Wayne]_fa932aab-2061-4d8a-adc2-312736104d18.mp3")
song1("../../../sorted_mp3s/All/01 - Down [feat. Lil Wayne]_fa932aab-2061-4d8a-adc2-312736104d18.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Drinkee (Vintage Culture & John Summit Remix)_ed668efd-3d2b-463f-872a-0f9e5600c6f5.mp3")
song1("../../../sorted_mp3s/All/01 - Drinkee (Vintage Culture & John Summit Remix)_ed668efd-3d2b-463f-872a-0f9e5600c6f5.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Dynamite [Explicit]_926e2430-8b9e-4cea-bf7d-8d13619d1679.mp3")
song1("../../../sorted_mp3s/All/01 - Dynamite [Explicit]_926e2430-8b9e-4cea-bf7d-8d13619d1679.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - East Bridge_e2d9e622-a7be-4cc2-b781-540013dba809.mp3")
song1("../../../sorted_mp3s/All/01 - East Bridge_e2d9e622-a7be-4cc2-b781-540013dba809.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Ego Death (feat. Kanye West, FKA twigs & Skrillex)_58a67c5f-7965-40cc-8349-d044f8290bfd.mp3")
song1("../../../sorted_mp3s/All/01 - Ego Death (feat. Kanye West, FKA twigs & Skrillex)_58a67c5f-7965-40cc-8349-d044f8290bfd.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - Endorphins [feat. Alex Clare]_808cc635-8e01-4f1d-baf2-e2ae6387c9c0.mp3")
song1("../../../sorted_mp3s/All/01 - Endorphins [feat. Alex Clare]_808cc635-8e01-4f1d-baf2-e2ae6387c9c0.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Enigma_0da0a38e-b105-412c-b715-d31831f9dd68.mp3")
song1("../../../sorted_mp3s/All/01 - Enigma_0da0a38e-b105-412c-b715-d31831f9dd68.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Eyes In The Back Of My Head_027de117-54e3-47f8-8600-ab527fa83ef4.mp3")
song1("../../../sorted_mp3s/All/01 - Eyes In The Back Of My Head_027de117-54e3-47f8-8600-ab527fa83ef4.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - FOUNDATION_0f7b2b51-2a1f-4301-9455-1db0b61fdc16.mp3")
song1("../../../sorted_mp3s/All/01 - FOUNDATION_0f7b2b51-2a1f-4301-9455-1db0b61fdc16.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Faceshopping_4f937d78-74e8-488c-97b1-f3b4dcc3652a.mp3")
song1("../../../sorted_mp3s/All/01 - Faceshopping_4f937d78-74e8-488c-97b1-f3b4dcc3652a.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Fairy Tale_926c35ef-01ab-4cff-8222-867c5518ae8d.mp3")
song1("../../../sorted_mp3s/All/01 - Fairy Tale_926c35ef-01ab-4cff-8222-867c5518ae8d.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Falling Down_54a2efbe-ab83-4d3b-8bb1-2671294d269f.mp3")
song1("../../../sorted_mp3s/All/01 - Falling Down_54a2efbe-ab83-4d3b-8bb1-2671294d269f.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Falling_1c162e5c-6ad3-4238-b6e7-edd1efd58f8f.mp3")
song1("../../../sorted_mp3s/All/01 - Falling_1c162e5c-6ad3-4238-b6e7-edd1efd58f8f.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Falls (Golden Features Remix)_72cb027b-d599-4b58-b8bd-fb2c3f5cab72.mp3")
song1("../../../sorted_mp3s/All/01 - Falls (Golden Features Remix)_72cb027b-d599-4b58-b8bd-fb2c3f5cab72.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/01 - Filmic (Original Mix)_ccd6a99e-cfc4-4ea1-af0d-1bd775d29114.mp3")
song1("../../../sorted_mp3s/All/01 - Filmic (Original Mix)_ccd6a99e-cfc4-4ea1-af0d-1bd775d29114.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Forget It_e445590b-1348-4fef-bb0f-a336703c94f6.mp3")
song1("../../../sorted_mp3s/All/01 - Forget It_e445590b-1348-4fef-bb0f-a336703c94f6.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Friday (Dopamine Re-Edit)_534cf0ce-c401-4621-9c48-ba859e011f24.mp3")
song1("../../../sorted_mp3s/All/01 - Friday (Dopamine Re-Edit)_534cf0ce-c401-4621-9c48-ba859e011f24.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Gaspin 4 Air_b1455a4c-6506-4fd8-98d2-2ad87da06bb6.mp3")
song1("../../../sorted_mp3s/All/01 - Gaspin 4 Air_b1455a4c-6506-4fd8-98d2-2ad87da06bb6.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Gecko (Overdrive) [Radio Edit]_ea3df744-0fb0-40f6-98c4-3ca378c92304.mp3")
song1("../../../sorted_mp3s/All/01 - Gecko (Overdrive) [Radio Edit]_ea3df744-0fb0-40f6-98c4-3ca378c92304.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Glad You Came_69cbc27c-8faf-4f3b-87ca-da6e70825534.mp3")
song1("../../../sorted_mp3s/All/01 - Glad You Came_69cbc27c-8faf-4f3b-87ca-da6e70825534.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Good Feeling_e0823d18-6803-4168-b6be-44faf221168b.mp3")
song1("../../../sorted_mp3s/All/01 - Good Feeling_e0823d18-6803-4168-b6be-44faf221168b.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Harder (feat. Talay Riley)_23eed703-114a-426d-b4ee-a9c38a20168e.mp3")
song1("../../../sorted_mp3s/All/01 - Harder (feat. Talay Riley)_23eed703-114a-426d-b4ee-a9c38a20168e.mp3").playlists = ['All', 'Trance_ProgressiveHouse']
load_song("../../../sorted_mp3s/All/01 - Heart Break_b795a0cb-7d21-4034-9eb0-8cdfa2ab793b.mp3")
song1("../../../sorted_mp3s/All/01 - Heart Break_b795a0cb-7d21-4034-9eb0-8cdfa2ab793b.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Heartstrings_2be29bb5-b853-47c7-bdb2-52651bf1b4b3.mp3")
song1("../../../sorted_mp3s/All/01 - Heartstrings_2be29bb5-b853-47c7-bdb2-52651bf1b4b3.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Helix_dd11689b-9810-4b45-87bc-967c615ea7aa.mp3")
song1("../../../sorted_mp3s/All/01 - Helix_dd11689b-9810-4b45-87bc-967c615ea7aa.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Hold Your Colour (Noisia Remix) [Explicit]_44297704-9ef7-4954-9302-32b64311ed02.mp3")
song1("../../../sorted_mp3s/All/01 - Hold Your Colour (Noisia Remix) [Explicit]_44297704-9ef7-4954-9302-32b64311ed02.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Home_56574fdb-97c2-40cf-921d-ffd7c26391e5.mp3")
song1("../../../sorted_mp3s/All/01 - Home_56574fdb-97c2-40cf-921d-ffd7c26391e5.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/01 - Honest To Gød (feat. Charity)_5c0957a9-8f00-4063-a1c5-aa12e2080cc2.mp3")
song1("../../../sorted_mp3s/All/01 - Honest To Gød (feat. Charity)_5c0957a9-8f00-4063-a1c5-aa12e2080cc2.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Horizon_3cd80700-c392-41de-a06e-2668c8ddf495.mp3")
song1("../../../sorted_mp3s/All/01 - Horizon_3cd80700-c392-41de-a06e-2668c8ddf495.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - I Get You_3badefd9-2ebf-4c61-a3d6-a10d56f0ae3d.mp3")
song1("../../../sorted_mp3s/All/01 - I Get You_3badefd9-2ebf-4c61-a3d6-a10d56f0ae3d.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - I'm Not Alright (EDX's Dubai Skyline Remix)_fc20e4c6-5de0-45ef-878c-83c6dbafbd32.mp3")
song1("../../../sorted_mp3s/All/01 - I'm Not Alright (EDX's Dubai Skyline Remix)_fc20e4c6-5de0-45ef-878c-83c6dbafbd32.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - I'm On One (Feat. Drake, Rick Ross & Lil Wayne) [Explicit]_30b662e4-de8a-4ce1-ab0c-0ca66ab82ac1.mp3")
song1("../../../sorted_mp3s/All/01 - I'm On One (Feat. Drake, Rick Ross & Lil Wayne) [Explicit]_30b662e4-de8a-4ce1-ab0c-0ca66ab82ac1.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - Inferno_7b498df9-cd15-4253-b4d4-c64c917534d6.mp3")
song1("../../../sorted_mp3s/All/01 - Inferno_7b498df9-cd15-4253-b4d4-c64c917534d6.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - JustYourSoul (Tchami Remix)_6b918fc2-a29e-4e9b-86e8-8975e0ffe5d9.mp3")
song1("../../../sorted_mp3s/All/01 - JustYourSoul (Tchami Remix)_6b918fc2-a29e-4e9b-86e8-8975e0ffe5d9.mp3").playlists = ['All', 'Tech_BassHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Kaleidoscope_52ec6c06-df04-4aa4-af97-98d1d550e47b.mp3")
song1("../../../sorted_mp3s/All/01 - Kaleidoscope_52ec6c06-df04-4aa4-af97-98d1d550e47b.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Keep Dancing_3f5e23f5-abbf-4d25-b0ac-ec8776954ce9.mp3")
song1("../../../sorted_mp3s/All/01 - Keep Dancing_3f5e23f5-abbf-4d25-b0ac-ec8776954ce9.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Koala (Radio Edit)_716b1589-297a-4b56-80fe-8755cf8caec0.mp3")
song1("../../../sorted_mp3s/All/01 - Koala (Radio Edit)_716b1589-297a-4b56-80fe-8755cf8caec0.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Kotaro_322e8f84-4ac7-4e0d-8ce4-b0ada97ae6f1.mp3")
song1("../../../sorted_mp3s/All/01 - Kotaro_322e8f84-4ac7-4e0d-8ce4-b0ada97ae6f1.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Lean [Explicit]_1b4eef42-f699-4581-a5b1-88e360f4b67d.mp3")
song1("../../../sorted_mp3s/All/01 - Lean [Explicit]_1b4eef42-f699-4581-a5b1-88e360f4b67d.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/01 - Leaving (AWAY Remix)_1c6ec60d-aae1-4160-b53d-39ab7ad9c8b3.mp3")
song1("../../../sorted_mp3s/All/01 - Leaving (AWAY Remix)_1c6ec60d-aae1-4160-b53d-39ab7ad9c8b3.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Lemniscate (The Place Between Sleeping and Awake)_ee307721-0eb4-49c3-b77a-e61792d8d7a7.mp3")
song1("../../../sorted_mp3s/All/01 - Lemniscate (The Place Between Sleeping and Awake)_ee307721-0eb4-49c3-b77a-e61792d8d7a7.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Lemonade [feat. NAV] [Explicit]_9e91353f-e7a8-44da-8067-c9972aa8d447.mp3")
song1("../../../sorted_mp3s/All/01 - Lemonade [feat. NAV] [Explicit]_9e91353f-e7a8-44da-8067-c9972aa8d447.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - Levitate (feat. Tylor Maurer)_51121db3-fe7f-465e-9fcd-10f6e591d697.mp3")
song1("../../../sorted_mp3s/All/01 - Levitate (feat. Tylor Maurer)_51121db3-fe7f-465e-9fcd-10f6e591d697.mp3").playlists = ['All', 'Tech_BassHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Lifting_7da069e2-b537-49d4-82ce-695c8578906b.mp3")
song1("../../../sorted_mp3s/All/01 - Lifting_7da069e2-b537-49d4-82ce-695c8578906b.mp3").playlists = ['All', 'Tech_BassHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Lights Out_547d23d4-8d7a-4aca-a5ea-31344cb8f4fd.mp3")
song1("../../../sorted_mp3s/All/01 - Lights Out_547d23d4-8d7a-4aca-a5ea-31344cb8f4fd.mp3").playlists = ['All', 'Trap_Midtempo']
load_song("../../../sorted_mp3s/All/01 - Like A G6_2e5e6935-c96f-4924-9292-c872da4fe2b0.mp3")
song1("../../../sorted_mp3s/All/01 - Like A G6_2e5e6935-c96f-4924-9292-c872da4fe2b0.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Look At Me! [Explicit]_f55b1c80-a72e-4dc8-938e-85588cc4773b.mp3")
song1("../../../sorted_mp3s/All/01 - Look At Me! [Explicit]_f55b1c80-a72e-4dc8-938e-85588cc4773b.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - Lose Control_e3f6466c-d302-444a-a06d-00be84a3b8f7.mp3")
song1("../../../sorted_mp3s/All/01 - Lose Control_e3f6466c-d302-444a-a06d-00be84a3b8f7.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Lost It_2074c8de-0300-45a1-b6e2-3b02a1342ea3.mp3")
song1("../../../sorted_mp3s/All/01 - Lost It_2074c8de-0300-45a1-b6e2-3b02a1342ea3.mp3").playlists = ['All', 'Trap_Midtempo']
load_song("../../../sorted_mp3s/All/01 - Love Tonight (Vintage Culture & Kiko Franco Remix)_d4bad93a-3f5a-4560-86df-c94ff8c71f6f.mp3")
song1("../../../sorted_mp3s/All/01 - Love Tonight (Vintage Culture & Kiko Franco Remix)_d4bad93a-3f5a-4560-86df-c94ff8c71f6f.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Lune_1dff33d7-94f1-4a68-aabd-8d1ec872c82c.mp3")
song1("../../../sorted_mp3s/All/01 - Lune_1dff33d7-94f1-4a68-aabd-8d1ec872c82c.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Lust [Explicit]_205b7b90-74a4-4d5f-87eb-82fbb1096b1e.mp3")
song1("../../../sorted_mp3s/All/01 - Lust [Explicit]_205b7b90-74a4-4d5f-87eb-82fbb1096b1e.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Mantra (Mat Zo Remix)_b4237d0b-7192-476e-803f-126440666832.mp3")
song1("../../../sorted_mp3s/All/01 - Mantra (Mat Zo Remix)_b4237d0b-7192-476e-803f-126440666832.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Heads Will Roll (A-Trak Remix)_c00692ba-c21d-4963-8a33-9ff9b7b0c907.mp3")
song1("../../../sorted_mp3s/All/01 - Heads Will Roll (A-Trak Remix)_c00692ba-c21d-4963-8a33-9ff9b7b0c907.mp3").playlists = ['All', 'Deep_ChillHouse', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Melt Session #1 [feat. Robert Glasper] [Explicit]_75bf7f95-3e9b-48ce-8211-423d7aa422dd.mp3")
song1("../../../sorted_mp3s/All/01 - Melt Session #1 [feat. Robert Glasper] [Explicit]_75bf7f95-3e9b-48ce-8211-423d7aa422dd.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Missing (feat. Mingue) [Extended Mix]_9f2f2d1a-0ad5-45b1-a4ee-9c9e715b39bc.mp3")
song1("../../../sorted_mp3s/All/01 - Missing (feat. Mingue) [Extended Mix]_9f2f2d1a-0ad5-45b1-a4ee-9c9e715b39bc.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Mood [Explicit]_52241111-5897-4e2c-8a1f-b6767f7504ba.mp3")
song1("../../../sorted_mp3s/All/01 - Mood [Explicit]_52241111-5897-4e2c-8a1f-b6767f7504ba.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - Move All Night_bed7e7b0-802d-4604-8844-aa6284c48a3b.mp3")
song1("../../../sorted_mp3s/All/01 - Move All Night_bed7e7b0-802d-4604-8844-aa6284c48a3b.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - My Way_c0846ead-cc19-4357-9657-90eecce47c52.mp3")
song1("../../../sorted_mp3s/All/01 - My Way_c0846ead-cc19-4357-9657-90eecce47c52.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Never Enough_abb7059a-464b-4479-bc2b-b62cf1b24c95.mp3")
song1("../../../sorted_mp3s/All/01 - Never Enough_abb7059a-464b-4479-bc2b-b62cf1b24c95.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Never Know [Explicit]_40af245b-af42-469e-b060-cedc8b00cbed.mp3")
song1("../../../sorted_mp3s/All/01 - Never Know [Explicit]_40af245b-af42-469e-b060-cedc8b00cbed.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Next to Me_4aa30b28-6a80-47ff-9578-63da67b5c2d2.mp3")
song1("../../../sorted_mp3s/All/01 - Next to Me_4aa30b28-6a80-47ff-9578-63da67b5c2d2.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Nightlight_176bc0f8-c959-406e-928c-b8bbfbb79f20.mp3")
song1("../../../sorted_mp3s/All/01 - Nightlight_176bc0f8-c959-406e-928c-b8bbfbb79f20.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Nightwalk_a9b8714f-401f-41ad-8d8b-0e0e686a4c77.mp3")
song1("../../../sorted_mp3s/All/01 - Nightwalk_a9b8714f-401f-41ad-8d8b-0e0e686a4c77.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - On A Mountain (Flume Remix)_d14ed395-3398-4bf5-9d9c-c45af8fbde8c.mp3")
song1("../../../sorted_mp3s/All/01 - On A Mountain (Flume Remix)_d14ed395-3398-4bf5-9d9c-c45af8fbde8c.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Ona Ona_e6b1280e-e9c0-466e-a2a1-f2c6454c9bbc.mp3")
song1("../../../sorted_mp3s/All/01 - Ona Ona_e6b1280e-e9c0-466e-a2a1-f2c6454c9bbc.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Only For A Moment_85985ebd-b689-4c95-87f2-e288eb228ac5.mp3")
song1("../../../sorted_mp3s/All/01 - Only For A Moment_85985ebd-b689-4c95-87f2-e288eb228ac5.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Only The Gods (feat. Anabel Englund)_b1899c01-6d82-489a-8f9d-ded99f40885f.mp3")
song1("../../../sorted_mp3s/All/01 - Only The Gods (feat. Anabel Englund)_b1899c01-6d82-489a-8f9d-ded99f40885f.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - PILL BREAKER [feat. Machine Gun Kelly & blackbear] [Explicit]_a75c2065-7eeb-4d5b-b295-bdbff70d30dd.mp3")
song1("../../../sorted_mp3s/All/01 - PILL BREAKER [feat. Machine Gun Kelly & blackbear] [Explicit]_a75c2065-7eeb-4d5b-b295-bdbff70d30dd.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Palace [Explicit]_4f27317d-bdc6-4e81-a52e-d9c52c78f161.mp3")
song1("../../../sorted_mp3s/All/01 - Palace [Explicit]_4f27317d-bdc6-4e81-a52e-d9c52c78f161.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Pictures_9b65d483-9c44-430e-a0db-7bd62a377b89.mp3")
song1("../../../sorted_mp3s/All/01 - Pictures_9b65d483-9c44-430e-a0db-7bd62a377b89.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/01 - Potions_0caa3b1e-7e4c-4141-a3b4-f84f4759164c.mp3")
song1("../../../sorted_mp3s/All/01 - Potions_0caa3b1e-7e4c-4141-a3b4-f84f4759164c.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Pressure_003d883a-743b-4ff5-8870-d80aac976e92.mp3")
song1("../../../sorted_mp3s/All/01 - Pressure_003d883a-743b-4ff5-8870-d80aac976e92.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Pressure_f7ede3f2-389b-4ab8-af32-26e7d5e1d698.mp3")
song1("../../../sorted_mp3s/All/01 - Pressure_f7ede3f2-389b-4ab8-af32-26e7d5e1d698.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Prologue_6df42634-7816-48e8-92a4-67ba1abbe4b7.mp3")
song1("../../../sorted_mp3s/All/01 - Prologue_6df42634-7816-48e8-92a4-67ba1abbe4b7.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Pursuit Of Happiness (Steve Aoki Remix Feat. MGMT & Ratatat) [Explicit]_6c50b820-d223-428d-b2fc-8de399cfbcae.mp3")
song1("../../../sorted_mp3s/All/01 - Pursuit Of Happiness (Steve Aoki Remix Feat. MGMT & Ratatat) [Explicit]_6c50b820-d223-428d-b2fc-8de399cfbcae.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Quantum Immortality (AWAY Remix) (feat. Away)_8cf7a562-8c7c-4994-8533-172ea6da44de.mp3")
song1("../../../sorted_mp3s/All/01 - Quantum Immortality (AWAY Remix) (feat. Away)_8cf7a562-8c7c-4994-8533-172ea6da44de.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Rainforest_1300a5fb-d70e-4e5d-9bd4-4ce056dd6500.mp3")
song1("../../../sorted_mp3s/All/01 - Rainforest_1300a5fb-d70e-4e5d-9bd4-4ce056dd6500.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Realm (Upgrade Remix)_14da5eba-97f6-498b-a96e-0e3ac05e5476.mp3")
song1("../../../sorted_mp3s/All/01 - Realm (Upgrade Remix)_14da5eba-97f6-498b-a96e-0e3ac05e5476.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Red (Brothel Remix)_2d61b880-b4c5-4c77-8edf-44ef721a80e9.mp3")
song1("../../../sorted_mp3s/All/01 - Red (Brothel Remix)_2d61b880-b4c5-4c77-8edf-44ef721a80e9.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Reflex Angle (KOAN Sound Remix)_caf36ceb-daf0-4706-ae74-12e443e7173c.mp3")
song1("../../../sorted_mp3s/All/01 - Reflex Angle (KOAN Sound Remix)_caf36ceb-daf0-4706-ae74-12e443e7173c.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Rendezvous [Explicit]_7b67c381-b801-48a4-b639-7ab26a4c58c3.mp3")
song1("../../../sorted_mp3s/All/01 - Rendezvous [Explicit]_7b67c381-b801-48a4-b639-7ab26a4c58c3.mp3").playlists = ['All', 'Hits_Throwbacks', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Resolve_cc1077f8-3bd7-4ad1-82a3-2a7e56a5c958.mp3")
song1("../../../sorted_mp3s/All/01 - Resolve_cc1077f8-3bd7-4ad1-82a3-2a7e56a5c958.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Ripper_2c847bd2-f29e-441a-984e-6a292f558248.mp3")
song1("../../../sorted_mp3s/All/01 - Ripper_2c847bd2-f29e-441a-984e-6a292f558248.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Rising_8eea165f-b2e3-4a02-bd05-24ce60a562ac.mp3")
song1("../../../sorted_mp3s/All/01 - Rising_8eea165f-b2e3-4a02-bd05-24ce60a562ac.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Ritual_474ba40d-2a33-42b4-a08b-3a8675b2e2b2.mp3")
song1("../../../sorted_mp3s/All/01 - Ritual_474ba40d-2a33-42b4-a08b-3a8675b2e2b2.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - SBCNCSLY_d314f5ae-a911-41fd-83f5-3a3c27352688.mp3")
song1("../../../sorted_mp3s/All/01 - SBCNCSLY_d314f5ae-a911-41fd-83f5-3a3c27352688.mp3").playlists = ['All', 'Deep_ChillHouse', 'Trap_Midtempo']
load_song("../../../sorted_mp3s/All/01 - STAY [Explicit]_7c3cad4b-fa95-4e20-a0a7-0b81783b3001.mp3")
song1("../../../sorted_mp3s/All/01 - STAY [Explicit]_7c3cad4b-fa95-4e20-a0a7-0b81783b3001.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Saviour (feat. Sharlene Hector)_60933228-b302-4f6b-9a7f-b07a799ea9f2.mp3")
song1("../../../sorted_mp3s/All/01 - Saviour (feat. Sharlene Hector)_60933228-b302-4f6b-9a7f-b07a799ea9f2.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Say Nothing (Tchami Remix)_3c81a4fb-5647-43e9-8dcc-14098428f69e.mp3")
song1("../../../sorted_mp3s/All/01 - Say Nothing (Tchami Remix)_3c81a4fb-5647-43e9-8dcc-14098428f69e.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - September_cf8e5d7f-5dd4-47ba-ab6e-d305c772bce3.mp3")
song1("../../../sorted_mp3s/All/01 - September_cf8e5d7f-5dd4-47ba-ab6e-d305c772bce3.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - She Knows It (feat. Ayche Cee) [Explicit]_4429c648-5545-49a6-a397-758b909a664e.mp3")
song1("../../../sorted_mp3s/All/01 - She Knows It (feat. Ayche Cee) [Explicit]_4429c648-5545-49a6-a397-758b909a664e.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - She's Asleep (Vár Sofandi Remix)_558e5af4-5533-44f5-a68f-9a4f15720f6b.mp3")
song1("../../../sorted_mp3s/All/01 - She's Asleep (Vár Sofandi Remix)_558e5af4-5533-44f5-a68f-9a4f15720f6b.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Show Me_b51dd152-5360-48f8-8fe5-2b9e5264df62.mp3")
song1("../../../sorted_mp3s/All/01 - Show Me_b51dd152-5360-48f8-8fe5-2b9e5264df62.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Sirens (feat. Caroline Polachek)_dc1299a9-8e50-49d4-b184-66eb9294becd.mp3")
song1("../../../sorted_mp3s/All/01 - Sirens (feat. Caroline Polachek)_dc1299a9-8e50-49d4-b184-66eb9294becd.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Sleepwalker_6febc684-756d-4a36-bc3c-f36bd200225d.mp3")
song1("../../../sorted_mp3s/All/01 - Sleepwalker_6febc684-756d-4a36-bc3c-f36bd200225d.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Snow On Tha Bluff [Explicit]_7d8a384d-8535-4288-bb13-fa3ae8269d65.mp3")
song1("../../../sorted_mp3s/All/01 - Snow On Tha Bluff [Explicit]_7d8a384d-8535-4288-bb13-fa3ae8269d65.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - So Good (feat. bülow)_af059424-7d1f-49b3-be1f-f7b6f22d9d87.mp3")
song1("../../../sorted_mp3s/All/01 - So Good (feat. bülow)_af059424-7d1f-49b3-be1f-f7b6f22d9d87.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Somebody (feat. Bright Sparks) [Explicit]_7dc32d60-16b9-4c81-9c2a-c7e7865264f7.mp3")
song1("../../../sorted_mp3s/All/01 - Somebody (feat. Bright Sparks) [Explicit]_7dc32d60-16b9-4c81-9c2a-c7e7865264f7.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Stargazing_67056cd6-491e-4b09-ab45-1462527fc822.mp3")
song1("../../../sorted_mp3s/All/01 - Stargazing_67056cd6-491e-4b09-ab45-1462527fc822.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Stay (feat. Dalilah) (Tchami Remix)_112dc79f-9a39-4ed0-9efd-873127092589.mp3")
song1("../../../sorted_mp3s/All/01 - Stay (feat. Dalilah) (Tchami Remix)_112dc79f-9a39-4ed0-9efd-873127092589.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Stay_bb4b0a73-fce0-4b93-861c-ddc9eefba5f0.mp3")
song1("../../../sorted_mp3s/All/01 - Stay_bb4b0a73-fce0-4b93-861c-ddc9eefba5f0.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Sun In Your Eyes (Spencer Brown Remix)_8352ed31-ed3b-4369-a03a-c124b460777b.mp3")
song1("../../../sorted_mp3s/All/01 - Sun In Your Eyes (Spencer Brown Remix)_8352ed31-ed3b-4369-a03a-c124b460777b.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Supersonic (My Existence)_1625c7f4-d5bc-4077-adf9-b45cef914416.mp3")
song1("../../../sorted_mp3s/All/01 - Supersonic (My Existence)_1625c7f4-d5bc-4077-adf9-b45cef914416.mp3").playlists = ['All', 'Trap_Midtempo']
load_song("../../../sorted_mp3s/All/01 - Swimming Pools (Drank) [Explicit]_239f4201-b0a8-41a8-b9d7-1f142fbee4f7.mp3")
song1("../../../sorted_mp3s/All/01 - Swimming Pools (Drank) [Explicit]_239f4201-b0a8-41a8-b9d7-1f142fbee4f7.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - THINGS I CANNOT TELL YOU TO YOUR FACE_996d24a6-1fc6-4edc-86ec-ae6e14d2f1e8.mp3")
song1("../../../sorted_mp3s/All/01 - THINGS I CANNOT TELL YOU TO YOUR FACE_996d24a6-1fc6-4edc-86ec-ae6e14d2f1e8.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Temper_3100c22e-881e-413e-a8b0-b895080bfc89.mp3")
song1("../../../sorted_mp3s/All/01 - Temper_3100c22e-881e-413e-a8b0-b895080bfc89.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - The Best Part of Life_fa16dddf-4fcb-4fd1-9be7-3e9ea25eab3b.mp3")
song1("../../../sorted_mp3s/All/01 - The Best Part of Life_fa16dddf-4fcb-4fd1-9be7-3e9ea25eab3b.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - The Business_757aad09-5e4e-4d7b-ba80-cf3db8f59576.mp3")
song1("../../../sorted_mp3s/All/01 - The Business_757aad09-5e4e-4d7b-ba80-cf3db8f59576.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - The Fall_a397ff81-3cc1-4830-b640-34dca8446110.mp3")
song1("../../../sorted_mp3s/All/01 - The Fall_a397ff81-3cc1-4830-b640-34dca8446110.mp3").playlists = ['All', 'Trance_ProgressiveHouse']
load_song("../../../sorted_mp3s/All/01 - The Feelings_41efa262-4387-4c77-ba66-3d87867071ca.mp3")
song1("../../../sorted_mp3s/All/01 - The Feelings_41efa262-4387-4c77-ba66-3d87867071ca.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - The Middle_bd6bc154-683e-4856-854a-9865bf4846f4.mp3")
song1("../../../sorted_mp3s/All/01 - The Middle_bd6bc154-683e-4856-854a-9865bf4846f4.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - This City (Extended Mix)_4f8a7b1b-9a30-4ec8-a602-88a83a341d84.mp3")
song1("../../../sorted_mp3s/All/01 - This City (Extended Mix)_4f8a7b1b-9a30-4ec8-a602-88a83a341d84.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - This Is What You Came For (Extended Mix)_d3e64d4d-ce72-49aa-a7ba-eb2e7843f10c.mp3")
song1("../../../sorted_mp3s/All/01 - This Is What You Came For (Extended Mix)_d3e64d4d-ce72-49aa-a7ba-eb2e7843f10c.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Time, Real & Imaginary_4370deac-7ddc-4e1b-8693-479e708dbb9a.mp3")
song1("../../../sorted_mp3s/All/01 - Time, Real & Imaginary_4370deac-7ddc-4e1b-8693-479e708dbb9a.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Too Close_2c44a8e4-1d96-4356-a752-3b0bc92766e4.mp3")
song1("../../../sorted_mp3s/All/01 - Too Close_2c44a8e4-1d96-4356-a752-3b0bc92766e4.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Top Down_ea106329-bb35-4671-9bf2-fd311e40483c.mp3")
song1("../../../sorted_mp3s/All/01 - Top Down_ea106329-bb35-4671-9bf2-fd311e40483c.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Transit_a6cfd42b-a2a1-448c-ba7e-20d7e0a5dca3.mp3")
song1("../../../sorted_mp3s/All/01 - Transit_a6cfd42b-a2a1-448c-ba7e-20d7e0a5dca3.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Tri-State_b05c7bc7-1a59-41d4-ada8-93981cc17132.mp3")
song1("../../../sorted_mp3s/All/01 - Tri-State_b05c7bc7-1a59-41d4-ada8-93981cc17132.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Turn off the Lights (feat. Alexis Roberts)_e8673202-70fc-4dc4-bbe9-ae7c410dff68.mp3")
song1("../../../sorted_mp3s/All/01 - Turn off the Lights (feat. Alexis Roberts)_e8673202-70fc-4dc4-bbe9-ae7c410dff68.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Tyler Herro [Explicit]_026a3c12-95d1-4340-921c-9907596ec1ac.mp3")
song1("../../../sorted_mp3s/All/01 - Tyler Herro [Explicit]_026a3c12-95d1-4340-921c-9907596ec1ac.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - U_304052f5-068a-47ba-86ec-8c2efefadccf.mp3")
song1("../../../sorted_mp3s/All/01 - U_304052f5-068a-47ba-86ec-8c2efefadccf.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Ultimate [Explicit]_46ef0dcf-d140-4edf-844a-c0314c810568.mp3")
song1("../../../sorted_mp3s/All/01 - Ultimate [Explicit]_46ef0dcf-d140-4edf-844a-c0314c810568.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - Underwater (feat. Sonu Nigam) [Extended Mix]_6159e242-4ec2-4ee4-8d6d-af75af2a02db.mp3")
song1("../../../sorted_mp3s/All/01 - Underwater (feat. Sonu Nigam) [Extended Mix]_6159e242-4ec2-4ee4-8d6d-af75af2a02db.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - United In Grief [Explicit]_e94af39d-668e-4a5f-81e2-2c4d442edcc6.mp3")
song1("../../../sorted_mp3s/All/01 - United In Grief [Explicit]_e94af39d-668e-4a5f-81e2-2c4d442edcc6.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Venture_65747488-a7a7-4722-9f3e-7cde74dc7927.mp3")
song1("../../../sorted_mp3s/All/01 - Venture_65747488-a7a7-4722-9f3e-7cde74dc7927.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - Virus (How About Now) [Radio Edit]_fe16463b-5b6c-449e-9fd4-4a73a6512934.mp3")
song1("../../../sorted_mp3s/All/01 - Virus (How About Now) [Radio Edit]_fe16463b-5b6c-449e-9fd4-4a73a6512934.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - WHATS POPPIN [Explicit]_d91e8db5-13aa-4836-9bfc-86ad22ebd429.mp3")
song1("../../../sorted_mp3s/All/01 - WHATS POPPIN [Explicit]_d91e8db5-13aa-4836-9bfc-86ad22ebd429.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - Waiting for You_d2b2413f-7eee-4e9d-8aed-e29d28edcd84.mp3")
song1("../../../sorted_mp3s/All/01 - Waiting for You_d2b2413f-7eee-4e9d-8aed-e29d28edcd84.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Walking By_dd27dc74-4b6f-4257-8dca-c543885d3cf6.mp3")
song1("../../../sorted_mp3s/All/01 - Walking By_dd27dc74-4b6f-4257-8dca-c543885d3cf6.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Water (feat. ZOHARA)_5bfec198-6109-4950-9c91-dcc87e8a3db7.mp3")
song1("../../../sorted_mp3s/All/01 - Water (feat. ZOHARA)_5bfec198-6109-4950-9c91-dcc87e8a3db7.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/01 - Whatcha Say_0245b9c4-779e-4e24-9da0-295e2848ead0.mp3")
song1("../../../sorted_mp3s/All/01 - Whatcha Say_0245b9c4-779e-4e24-9da0-295e2848ead0.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - What’s Next [Explicit]_211b499c-cf7c-4453-8e2e-98f1b140cd1e.mp3")
song1("../../../sorted_mp3s/All/01 - What’s Next [Explicit]_211b499c-cf7c-4453-8e2e-98f1b140cd1e.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - Whistle_b6a0492b-3f23-4d09-a4bc-b4e9f14abad4.mp3")
song1("../../../sorted_mp3s/All/01 - Whistle_b6a0492b-3f23-4d09-a4bc-b4e9f14abad4.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/01 - Without Me (ILLENIUM Remix) [Explicit]_66ad210e-cc28-4989-934a-14e535daafc5.mp3")
song1("../../../sorted_mp3s/All/01 - Without Me (ILLENIUM Remix) [Explicit]_66ad210e-cc28-4989-934a-14e535daafc5.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - World Away_42315093-3f0d-4889-bd6d-05831b81ee09.mp3")
song1("../../../sorted_mp3s/All/01 - World Away_42315093-3f0d-4889-bd6d-05831b81ee09.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - You Should Run_9aa27bff-953d-4b33-9e3b-647a22d943c7.mp3")
song1("../../../sorted_mp3s/All/01 - You Should Run_9aa27bff-953d-4b33-9e3b-647a22d943c7.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/01 - ZUU [Explicit]_8532a4b9-6bce-4008-a3f3-92f4ae6cec3f.mp3")
song1("../../../sorted_mp3s/All/01 - ZUU [Explicit]_8532a4b9-6bce-4008-a3f3-92f4ae6cec3f.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/01 - ‎amends_707f8f80-97db-494b-b832-50e9d17a2d20.mp3")
song1("../../../sorted_mp3s/All/01 - ‎amends_707f8f80-97db-494b-b832-50e9d17a2d20.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - After Life (San Holo Remix) [feat. Stacy Barthe]_00da5d00-ba34-4574-bd79-283db9bd44fc.mp3")
song1("../../../sorted_mp3s/All/02 - After Life (San Holo Remix) [feat. Stacy Barthe]_00da5d00-ba34-4574-bd79-283db9bd44fc.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Alchemy (Original Mix)_5bfa3a65-e657-41bb-99bf-4b3b2c60f182.mp3")
song1("../../../sorted_mp3s/All/02 - Alchemy (Original Mix)_5bfa3a65-e657-41bb-99bf-4b3b2c60f182.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Alive (feat. Poppy Baskcomb)_5c93e78f-79bb-4bc3-998e-c08d8526f9bb.mp3")
song1("../../../sorted_mp3s/All/02 - Alive (feat. Poppy Baskcomb)_5c93e78f-79bb-4bc3-998e-c08d8526f9bb.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Anomaly_9239c892-6425-4c4a-9b7a-1ee0af831fab.mp3")
song1("../../../sorted_mp3s/All/02 - Anomaly_9239c892-6425-4c4a-9b7a-1ee0af831fab.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Another Angel (Extended Mix)_47ea32c0-cd37-4ded-a300-f363bef276d8.mp3")
song1("../../../sorted_mp3s/All/02 - Another Angel (Extended Mix)_47ea32c0-cd37-4ded-a300-f363bef276d8.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Answers (Extended Mix)_904bee73-14db-4412-a9b0-44712f9abd45.mp3")
song1("../../../sorted_mp3s/All/02 - Answers (Extended Mix)_904bee73-14db-4412-a9b0-44712f9abd45.mp3").playlists = ['All', 'FutureBass_Chillstep']
load_song("../../../sorted_mp3s/All/02 - Athena_47e84e01-7c7c-417c-aa67-d39304cba4e3.mp3")
song1("../../../sorted_mp3s/All/02 - Athena_47e84e01-7c7c-417c-aa67-d39304cba4e3.mp3").playlists = ['All', 'Trap_Midtempo']
load_song("../../../sorted_mp3s/All/02 - Be Somebody [Explicit]_2b78bc78-83a0-4e00-9fa3-29b433cb1598.mp3")
song1("../../../sorted_mp3s/All/02 - Be Somebody [Explicit]_2b78bc78-83a0-4e00-9fa3-29b433cb1598.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Better On My Own (feat. Anabel Englund)_b93291ec-4051-46b9-bc36-96f67f92c2d4.mp3")
song1("../../../sorted_mp3s/All/02 - Better On My Own (feat. Anabel Englund)_b93291ec-4051-46b9-bc36-96f67f92c2d4.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/02 - Boundless_69fade09-633f-4a45-9b31-efcb8383b130.mp3")
song1("../../../sorted_mp3s/All/02 - Boundless_69fade09-633f-4a45-9b31-efcb8383b130.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Break Your Heart [feat. Ludacris]_0f797234-e522-4567-a679-c1848aefc647.mp3")
song1("../../../sorted_mp3s/All/02 - Break Your Heart [feat. Ludacris]_0f797234-e522-4567-a679-c1848aefc647.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/02 - Breathin' (Extended Vocal Mix)_04c4ee13-c029-4d2d-a19d-bb6d4523e2c6.mp3")
song1("../../../sorted_mp3s/All/02 - Breathin' (Extended Vocal Mix)_04c4ee13-c029-4d2d-a19d-bb6d4523e2c6.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/02 - Came For The Low_17a9d37f-2afe-418a-bfc3-bc08b42d9cfb.mp3")
song1("../../../sorted_mp3s/All/02 - Came For The Low_17a9d37f-2afe-418a-bfc3-bc08b42d9cfb.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/02 - Canal St. [Explicit]_c9e7458b-69e8-4873-8f15-26f38e10d277.mp3")
song1("../../../sorted_mp3s/All/02 - Canal St. [Explicit]_c9e7458b-69e8-4873-8f15-26f38e10d277.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - DNA. [Explicit]_05f53aa6-2050-472b-af8f-45fb8009cf81.mp3")
song1("../../../sorted_mp3s/All/02 - DNA. [Explicit]_05f53aa6-2050-472b-af8f-45fb8009cf81.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Dynasty_be8593c4-ed3b-402d-bf10-a09efd78280d.mp3")
song1("../../../sorted_mp3s/All/02 - Dynasty_be8593c4-ed3b-402d-bf10-a09efd78280d.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Ecdysis_69e1553d-742b-48a0-b756-98ebe1e13123.mp3")
song1("../../../sorted_mp3s/All/02 - Ecdysis_69e1553d-742b-48a0-b756-98ebe1e13123.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Face Of My City (feat. Lil Baby) [Explicit]_1d9c331f-44cc-4130-b64c-1fa0c8f363b5.mp3")
song1("../../../sorted_mp3s/All/02 - Face Of My City (feat. Lil Baby) [Explicit]_1d9c331f-44cc-4130-b64c-1fa0c8f363b5.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Family_cf5cd50d-24d6-4c5f-b9e3-239bf9688fb0.mp3")
song1("../../../sorted_mp3s/All/02 - Family_cf5cd50d-24d6-4c5f-b9e3-239bf9688fb0.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/02 - Father Ocean (Ben Böhmer Remix)_ae0dd3f4-b164-42db-9c39-d38aa55b8ee3.mp3")
song1("../../../sorted_mp3s/All/02 - Father Ocean (Ben Böhmer Remix)_ae0dd3f4-b164-42db-9c39-d38aa55b8ee3.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Ghost Voices_e360995f-f6b5-45a0-b3cb-aac863a02488.mp3")
song1("../../../sorted_mp3s/All/02 - Ghost Voices_e360995f-f6b5-45a0-b3cb-aac863a02488.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Godspell_ff65edca-8887-4bc3-9115-706c637cc189.mp3")
song1("../../../sorted_mp3s/All/02 - Godspell_ff65edca-8887-4bc3-9115-706c637cc189.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - HEART ATTACK_6863e614-d6de-4fc1-842b-7a59123ccbdb.mp3")
song1("../../../sorted_mp3s/All/02 - HEART ATTACK_6863e614-d6de-4fc1-842b-7a59123ccbdb.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Here For You_9e155e32-d054-4990-9d5c-7028cc1e9dac.mp3")
song1("../../../sorted_mp3s/All/02 - Here For You_9e155e32-d054-4990-9d5c-7028cc1e9dac.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - High Rise_c86bd918-989d-4a5e-ba8d-640f5861a53c.mp3")
song1("../../../sorted_mp3s/All/02 - High Rise_c86bd918-989d-4a5e-ba8d-640f5861a53c.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Higher Love (Extended Mix)_c8f2e296-e36c-4758-9869-8ad1172f42f9.mp3")
song1("../../../sorted_mp3s/All/02 - Higher Love (Extended Mix)_c8f2e296-e36c-4758-9869-8ad1172f42f9.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Hypnotized (Extended Mix)_a4220bfc-a069-4a87-8a65-87519afc6e54.mp3")
song1("../../../sorted_mp3s/All/02 - Hypnotized (Extended Mix)_a4220bfc-a069-4a87-8a65-87519afc6e54.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - I'M DAT N____ [Explicit]_c8cbc09c-f66b-4979-ac2f-e4fc60199e83.mp3")
song1("../../../sorted_mp3s/All/02 - I'M DAT N____ [Explicit]_c8cbc09c-f66b-4979-ac2f-e4fc60199e83.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Indian Summer (Extended Mix)_aa300a07-99e4-41b7-8236-12e7fc6df644.mp3")
song1("../../../sorted_mp3s/All/02 - Indian Summer (Extended Mix)_aa300a07-99e4-41b7-8236-12e7fc6df644.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/02 - J2_a3e0c8a4-2526-4d2d-9325-8ea62dc91f1f.mp3")
song1("../../../sorted_mp3s/All/02 - J2_a3e0c8a4-2526-4d2d-9325-8ea62dc91f1f.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Jocelyn Flores [Explicit]_b82377cd-116b-4ff3-af6e-9ad428f09282.mp3")
song1("../../../sorted_mp3s/All/02 - Jocelyn Flores [Explicit]_b82377cd-116b-4ff3-af6e-9ad428f09282.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - La Danza (Extended Mix)_c213aa72-ac59-482d-8fbe-94f92a799648.mp3")
song1("../../../sorted_mp3s/All/02 - La Danza (Extended Mix)_c213aa72-ac59-482d-8fbe-94f92a799648.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/02 - Last Friday Night (T.G.I.F.)_1c59c250-d260-4bc0-9d15-0ee6d9e657dc.mp3")
song1("../../../sorted_mp3s/All/02 - Last Friday Night (T.G.I.F.)_1c59c250-d260-4bc0-9d15-0ee6d9e657dc.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/02 - Lonely Together [feat. Rita Ora]_34a21640-f176-4468-b67b-9b6bd885529d.mp3")
song1("../../../sorted_mp3s/All/02 - Lonely Together [feat. Rita Ora]_34a21640-f176-4468-b67b-9b6bd885529d.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/02 - Long Way From Home (Extended Mix)_6fa48e43-42f1-4381-896f-334924e9d79b.mp3")
song1("../../../sorted_mp3s/All/02 - Long Way From Home (Extended Mix)_6fa48e43-42f1-4381-896f-334924e9d79b.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Make It Happen_56423449-3107-4579-ad0f-90173104e610.mp3")
song1("../../../sorted_mp3s/All/02 - Make It Happen_56423449-3107-4579-ad0f-90173104e610.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Midnight City_ec98b6fa-b5da-4332-8b2b-3bb871a495c8.mp3")
song1("../../../sorted_mp3s/All/02 - Midnight City_ec98b6fa-b5da-4332-8b2b-3bb871a495c8.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/02 - Midnight_138f56cc-adf6-4754-9bed-f7c1367a03f8.mp3")
song1("../../../sorted_mp3s/All/02 - Midnight_138f56cc-adf6-4754-9bed-f7c1367a03f8.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Money In The Grave [feat. Rick Ross] [Explicit]_85cdbaa1-35b5-4c3c-9eca-faf743ceb235.mp3")
song1("../../../sorted_mp3s/All/02 - Money In The Grave [feat. Rick Ross] [Explicit]_85cdbaa1-35b5-4c3c-9eca-faf743ceb235.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/02 - Mr. Brightside_00731bbe-9195-4868-943d-a9f6c15cb45b.mp3")
song1("../../../sorted_mp3s/All/02 - Mr. Brightside_00731bbe-9195-4868-943d-a9f6c15cb45b.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/02 - Nightjar (feat. SHELLS) [Extended Mix]_becf7039-2cec-4bef-b64b-849897c9cab1.mp3")
song1("../../../sorted_mp3s/All/02 - Nightjar (feat. SHELLS) [Extended Mix]_becf7039-2cec-4bef-b64b-849897c9cab1.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/02 - No Captain (feat. POLIÇA)_bdf93f5f-7fcc-4b58-89da-7e8ab6f86d4a.mp3")
song1("../../../sorted_mp3s/All/02 - No Captain (feat. POLIÇA)_bdf93f5f-7fcc-4b58-89da-7e8ab6f86d4a.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - No One (feat. Thelma Plum)_878ef70d-8682-4bc7-b0e1-57393db3d353.mp3")
song1("../../../sorted_mp3s/All/02 - No One (feat. Thelma Plum)_878ef70d-8682-4bc7-b0e1-57393db3d353.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/02 - Northern Soul (Spencer Brown Remix)_08edc0e8-4fe9-4877-b380-c14c9144128b.mp3")
song1("../../../sorted_mp3s/All/02 - Northern Soul (Spencer Brown Remix)_08edc0e8-4fe9-4877-b380-c14c9144128b.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - PLANET'S MAD_9fcb2667-3013-4402-8d9e-23d6dd00c931.mp3")
song1("../../../sorted_mp3s/All/02 - PLANET'S MAD_9fcb2667-3013-4402-8d9e-23d6dd00c931.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Payphone [feat. Wiz Khalifa] [Explicit]_a57b643e-e31c-4d07-b1a1-b069526e6ddc.mp3")
song1("../../../sorted_mp3s/All/02 - Payphone [feat. Wiz Khalifa] [Explicit]_a57b643e-e31c-4d07-b1a1-b069526e6ddc.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/02 - Places_50e0b359-060e-42fc-8928-8e2705675011.mp3")
song1("../../../sorted_mp3s/All/02 - Places_50e0b359-060e-42fc-8928-8e2705675011.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/02 - Promesses (Extended Mix)_14ac7592-a9dc-42df-b350-b98f168efc0d.mp3")
song1("../../../sorted_mp3s/All/02 - Promesses (Extended Mix)_14ac7592-a9dc-42df-b350-b98f168efc0d.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Proud_716fdeeb-f360-40ff-8202-00f10965e32f.mp3")
song1("../../../sorted_mp3s/All/02 - Proud_716fdeeb-f360-40ff-8202-00f10965e32f.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - RICKY [Explicit]_ffb381b1-b0e5-4baf-9c4c-ed7ad142cbcd.mp3")
song1("../../../sorted_mp3s/All/02 - RICKY [Explicit]_ffb381b1-b0e5-4baf-9c4c-ed7ad142cbcd.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/02 - Red Shift_3a96309c-cb41-4b9d-aaf0-f53024149838.mp3")
song1("../../../sorted_mp3s/All/02 - Red Shift_3a96309c-cb41-4b9d-aaf0-f53024149838.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Road_28217c5d-0ae6-4d3a-a440-532de5983255.mp3")
song1("../../../sorted_mp3s/All/02 - Road_28217c5d-0ae6-4d3a-a440-532de5983255.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Rules [Explicit]_dd82416f-92b5-4aec-8e29-20ef695da225.mp3")
song1("../../../sorted_mp3s/All/02 - Rules [Explicit]_dd82416f-92b5-4aec-8e29-20ef695da225.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Runaway (feat. Reo Cragun) [Explicit]_c066668c-7fbc-4d80-8240-5f4765fb320e.mp3")
song1("../../../sorted_mp3s/All/02 - Runaway (feat. Reo Cragun) [Explicit]_c066668c-7fbc-4d80-8240-5f4765fb320e.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Safe & Sound (Extended Mix)_678a202c-5577-4d63-9d54-e68edbaa5d82.mp3")
song1("../../../sorted_mp3s/All/02 - Safe & Sound (Extended Mix)_678a202c-5577-4d63-9d54-e68edbaa5d82.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Save Me (feat. MKLA) [Extended Mix]_87823a1e-4f9a-4de4-9267-34f71070a41c.mp3")
song1("../../../sorted_mp3s/All/02 - Save Me (feat. MKLA) [Extended Mix]_87823a1e-4f9a-4de4-9267-34f71070a41c.mp3").playlists = ['All', 'Tech_BassHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Sentient_d1dd2617-87ea-4204-a9da-0311b0abe92d.mp3")
song1("../../../sorted_mp3s/All/02 - Sentient_d1dd2617-87ea-4204-a9da-0311b0abe92d.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Shrine_b16ec4a2-b6ca-4a1a-9d23-c3435bbfc833.mp3")
song1("../../../sorted_mp3s/All/02 - Shrine_b16ec4a2-b6ca-4a1a-9d23-c3435bbfc833.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Stereo Love (Original)_d28569c9-b0fe-4c63-92c1-31bef546cdab.mp3")
song1("../../../sorted_mp3s/All/02 - Stereo Love (Original)_d28569c9-b0fe-4c63-92c1-31bef546cdab.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/02 - Still Want U [Explicit]_4f0d2d6a-b244-4735-8f4e-e8596ac016b7.mp3")
song1("../../../sorted_mp3s/All/02 - Still Want U [Explicit]_4f0d2d6a-b244-4735-8f4e-e8596ac016b7.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Stole the Show_4d9f7a3a-dc4a-4e02-a6ed-c946ee6dccd0.mp3")
song1("../../../sorted_mp3s/All/02 - Stole the Show_4d9f7a3a-dc4a-4e02-a6ed-c946ee6dccd0.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Take A Step Back [feat. XXXTENTACION] [Explicit]_d31c785b-b09e-405d-a34b-bf54a890e92a.mp3")
song1("../../../sorted_mp3s/All/02 - Take A Step Back [feat. XXXTENTACION] [Explicit]_d31c785b-b09e-405d-a34b-bf54a890e92a.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/02 - Take_it_Back_v2 [Explicit]_2a2fc321-bd35-405e-9105-3582e16086cf.mp3")
song1("../../../sorted_mp3s/All/02 - Take_it_Back_v2 [Explicit]_2a2fc321-bd35-405e-9105-3582e16086cf.mp3").playlists = ['All', 'Hits_Throwbacks', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Takeaway (Sondr Remix)_350e7728-0c21-4253-a781-b9e0a3822929.mp3")
song1("../../../sorted_mp3s/All/02 - Takeaway (Sondr Remix)_350e7728-0c21-4253-a781-b9e0a3822929.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/02 - Terrified_477579c4-54ba-4457-b208-c10b8d353a23.mp3")
song1("../../../sorted_mp3s/All/02 - Terrified_477579c4-54ba-4457-b208-c10b8d353a23.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - The Box [Explicit]_edd1edbf-216f-4e44-9876-74bdb6364c79.mp3")
song1("../../../sorted_mp3s/All/02 - The Box [Explicit]_edd1edbf-216f-4e44-9876-74bdb6364c79.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/02 - The End [feat. HALIENE]_09857b1a-1f33-4959-8f93-21eee0578482.mp3")
song1("../../../sorted_mp3s/All/02 - The End [feat. HALIENE]_09857b1a-1f33-4959-8f93-21eee0578482.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - The Nights_5a42de94-3b3a-4b01-9f28-02d874acac73.mp3")
song1("../../../sorted_mp3s/All/02 - The Nights_5a42de94-3b3a-4b01-9f28-02d874acac73.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/02 - The Only Way Is Up_8b6dc1d0-4f50-4019-b967-9e72ffc81655.mp3")
song1("../../../sorted_mp3s/All/02 - The Only Way Is Up_8b6dc1d0-4f50-4019-b967-9e72ffc81655.mp3").playlists = ['All']
load_song("../../../sorted_mp3s/All/02 - Wants and Needs [feat. Lil Baby] [Explicit]_d516b2a4-4f97-4812-b17b-2d158a1ab508.mp3")
song1("../../../sorted_mp3s/All/02 - Wants and Needs [feat. Lil Baby] [Explicit]_d516b2a4-4f97-4812-b17b-2d158a1ab508.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/02 - We're All We Need_04efca69-de1d-4a5e-a520-85cefa949b57.mp3")
song1("../../../sorted_mp3s/All/02 - We're All We Need_04efca69-de1d-4a5e-a520-85cefa949b57.mp3").playlists = ['All', 'Trance_ProgressiveHouse']
load_song("../../../sorted_mp3s/All/02 - Wild Ones (feat. Sia)_02489b83-6f76-44f8-8090-115e5ff0bab4.mp3")
song1("../../../sorted_mp3s/All/02 - Wild Ones (feat. Sia)_02489b83-6f76-44f8-8090-115e5ff0bab4.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/02 - Wild_b7190d99-dbaa-43a6-b4ef-f72320c5a186.mp3")
song1("../../../sorted_mp3s/All/02 - Wild_b7190d99-dbaa-43a6-b4ef-f72320c5a186.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/02 - Worlds Apart (Seven Lions 1999 Extended Mix)_866d45d1-6bb2-4889-9388-4dc212660b22.mp3")
song1("../../../sorted_mp3s/All/02 - Worlds Apart (Seven Lions 1999 Extended Mix)_866d45d1-6bb2-4889-9388-4dc212660b22.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - 21C_Delta [Explicit]_d223fcdd-5e24-44a2-aec7-fdaf5ac58f88.mp3")
song1("../../../sorted_mp3s/All/03 - 21C_Delta [Explicit]_d223fcdd-5e24-44a2-aec7-fdaf5ac58f88.mp3").playlists = ['All', 'Hits_Throwbacks', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - AETHER_a6701fcd-582d-42be-8141-73755004592c.mp3")
song1("../../../sorted_mp3s/All/03 - AETHER_a6701fcd-582d-42be-8141-73755004592c.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - American Boy [Explicit]_aa8764f5-0f28-49af-a126-142b0f4c388f.mp3")
song1("../../../sorted_mp3s/All/03 - American Boy [Explicit]_aa8764f5-0f28-49af-a126-142b0f4c388f.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/03 - Atlas_b5b72ac0-5d3c-47bf-9b3e-3b5354e3552c.mp3")
song1("../../../sorted_mp3s/All/03 - Atlas_b5b72ac0-5d3c-47bf-9b3e-3b5354e3552c.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - BLINE_3aa8a79c-61d8-412b-b7f7-cf4b75bf8068.mp3")
song1("../../../sorted_mp3s/All/03 - BLINE_3aa8a79c-61d8-412b-b7f7-cf4b75bf8068.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Backseat Freestyle [Explicit]_cee4ee23-53ea-447a-865b-f965adfb3755.mp3")
song1("../../../sorted_mp3s/All/03 - Backseat Freestyle [Explicit]_cee4ee23-53ea-447a-865b-f965adfb3755.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Bass [Explicit]_c138d3b7-dcab-4267-a766-5f390969bc9a.mp3")
song1("../../../sorted_mp3s/All/03 - Bass [Explicit]_c138d3b7-dcab-4267-a766-5f390969bc9a.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Beaches_ea55f89b-df75-4076-9603-e7325f0e4383.mp3")
song1("../../../sorted_mp3s/All/03 - Beaches_ea55f89b-df75-4076-9603-e7325f0e4383.mp3").playlists = ['All', 'FutureBass_Chillstep']
load_song("../../../sorted_mp3s/All/03 - Blame Myself (Moore Kismet Remix)_9d0b2c2b-36c2-48ca-afd3-347651f007dd.mp3")
song1("../../../sorted_mp3s/All/03 - Blame Myself (Moore Kismet Remix)_9d0b2c2b-36c2-48ca-afd3-347651f007dd.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Braids_b8e5dd84-e5fb-497f-96cf-d03b846de8e6.mp3")
song1("../../../sorted_mp3s/All/03 - Braids_b8e5dd84-e5fb-497f-96cf-d03b846de8e6.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Bubble_39412ec0-57ca-4f95-81f3-905bccc39906.mp3")
song1("../../../sorted_mp3s/All/03 - Bubble_39412ec0-57ca-4f95-81f3-905bccc39906.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Chorus of Disapproval_4c8a85c6-4b4a-4903-97f3-2767b33308fe.mp3")
song1("../../../sorted_mp3s/All/03 - Chorus of Disapproval_4c8a85c6-4b4a-4903-97f3-2767b33308fe.mp3").playlists = ['All', 'Drum&Bass']
load_song("../../../sorted_mp3s/All/03 - Closer_4bf93896-7eb3-4586-95e8-41c5e482b6dc.mp3")
song1("../../../sorted_mp3s/All/03 - Closer_4bf93896-7eb3-4586-95e8-41c5e482b6dc.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/03 - Collider_3a91a736-6595-4964-b845-de74dc1aec2c.mp3")
song1("../../../sorted_mp3s/All/03 - Collider_3a91a736-6595-4964-b845-de74dc1aec2c.mp3").playlists = ['All', 'Tech_BassHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Distance (feat. Geoffroy) (KOAN Sound Remix)_316b1490-0ddd-4c62-8256-2d668325fb4c.mp3")
song1("../../../sorted_mp3s/All/03 - Distance (feat. Geoffroy) (KOAN Sound Remix)_316b1490-0ddd-4c62-8256-2d668325fb4c.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Feel This Moment_4c1f0644-b53c-4211-9459-6d20583cdff7.mp3")
song1("../../../sorted_mp3s/All/03 - Feel This Moment_4c1f0644-b53c-4211-9459-6d20583cdff7.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/03 - Fine Whine [Explicit]_a3b81bbb-0bba-45f5-9116-807025fb4abd.mp3")
song1("../../../sorted_mp3s/All/03 - Fine Whine [Explicit]_a3b81bbb-0bba-45f5-9116-807025fb4abd.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - For The Night [feat. Lil Baby & DaBaby] [Explicit]_7cc34eda-70a3-48d5-b0af-8ffa9fd84698.mp3")
song1("../../../sorted_mp3s/All/03 - For The Night [feat. Lil Baby & DaBaby] [Explicit]_7cc34eda-70a3-48d5-b0af-8ffa9fd84698.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/03 - Ghostbox_ad5cf293-69a8-44cf-aaed-cc4481765fa0.mp3")
song1("../../../sorted_mp3s/All/03 - Ghostbox_ad5cf293-69a8-44cf-aaed-cc4481765fa0.mp3").playlists = ['All', 'FutureBass_Chillstep']
load_song("../../../sorted_mp3s/All/03 - Hall of Fame_e8c987fd-02e8-451d-900a-15cdbcb5fa18.mp3")
song1("../../../sorted_mp3s/All/03 - Hall of Fame_e8c987fd-02e8-451d-900a-15cdbcb5fa18.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/03 - Heart Tones_710d3146-953f-4d02-9203-fbfc612f3eba.mp3")
song1("../../../sorted_mp3s/All/03 - Heart Tones_710d3146-953f-4d02-9203-fbfc612f3eba.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Heartless_a2e5514c-2278-4245-8c88-65c64946a5e4.mp3")
song1("../../../sorted_mp3s/All/03 - Heartless_a2e5514c-2278-4245-8c88-65c64946a5e4.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/03 - High Beams [Explicit]_c152f818-4e45-47ca-8fce-90724f9ebe19.mp3")
song1("../../../sorted_mp3s/All/03 - High Beams [Explicit]_c152f818-4e45-47ca-8fce-90724f9ebe19.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - KEEP IT BURNIN [Explicit]_9fb83eb8-2563-4b46-af9b-71af3e8aa9e2.mp3")
song1("../../../sorted_mp3s/All/03 - KEEP IT BURNIN [Explicit]_9fb83eb8-2563-4b46-af9b-71af3e8aa9e2.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Killed By The City (Mojjo Remix)_dc2c9ebd-64c7-47f6-ac48-41888bea9922.mp3")
song1("../../../sorted_mp3s/All/03 - Killed By The City (Mojjo Remix)_dc2c9ebd-64c7-47f6-ac48-41888bea9922.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/03 - Lose Myself [feat. Lynn Gunn]_604cabd9-141f-45ab-9190-5dc6817acd68.mp3")
song1("../../../sorted_mp3s/All/03 - Lose Myself [feat. Lynn Gunn]_604cabd9-141f-45ab-9190-5dc6817acd68.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Lovin U_24100d59-8d3e-40ec-9d54-7acafde0a237.mp3")
song1("../../../sorted_mp3s/All/03 - Lovin U_24100d59-8d3e-40ec-9d54-7acafde0a237.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Moonlight [Explicit]_697ea771-f24e-400a-a35a-a60e5584fbb2.mp3")
song1("../../../sorted_mp3s/All/03 - Moonlight [Explicit]_697ea771-f24e-400a-a35a-a60e5584fbb2.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Nepenthe_cb76ab15-5eca-472e-87c9-48daaa6eca59.mp3")
song1("../../../sorted_mp3s/All/03 - Nepenthe_cb76ab15-5eca-472e-87c9-48daaa6eca59.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Ni__as In Paris [Explicit]_9c1f75cf-a384-4afd-9e5b-a48c01e62b21.mp3")
song1("../../../sorted_mp3s/All/03 - Ni__as In Paris [Explicit]_9c1f75cf-a384-4afd-9e5b-a48c01e62b21.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/03 - PMW (All I Really Need) [Explicit]_e97e4630-0d00-4a51-b4f7-4a45ea36a88c.mp3")
song1("../../../sorted_mp3s/All/03 - PMW (All I Really Need) [Explicit]_e97e4630-0d00-4a51-b4f7-4a45ea36a88c.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - PRBLMS [Explicit]_b8edd0f6-4b0e-4835-a8b1-60967633de2f.mp3")
song1("../../../sorted_mp3s/All/03 - PRBLMS [Explicit]_b8edd0f6-4b0e-4835-a8b1-60967633de2f.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Pain_8f2d7d79-4ac0-403c-9918-f87943c5645b.mp3")
song1("../../../sorted_mp3s/All/03 - Pain_8f2d7d79-4ac0-403c-9918-f87943c5645b.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - See You Go [feat. Courtney Paige Nelson]_a07f3dd8-4b79-4e46-ac9f-b5120213fccd.mp3")
song1("../../../sorted_mp3s/All/03 - See You Go [feat. Courtney Paige Nelson]_a07f3dd8-4b79-4e46-ac9f-b5120213fccd.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Show Me Love (EDX Remix _ Radio Edit) [feat. Kimberly Anne]_c66b58c8-bc43-4ec3-b6a0-a32a9d38f3e8.mp3")
song1("../../../sorted_mp3s/All/03 - Show Me Love (EDX Remix _ Radio Edit) [feat. Kimberly Anne]_c66b58c8-bc43-4ec3-b6a0-a32a9d38f3e8.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/03 - Show Them_7ae87155-c5f9-4d17-9c8e-b8584118a7fa.mp3")
song1("../../../sorted_mp3s/All/03 - Show Them_7ae87155-c5f9-4d17-9c8e-b8584118a7fa.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Stacy's Mom_d4ec623d-04f7-4e27-ab98-084f0afad96b.mp3")
song1("../../../sorted_mp3s/All/03 - Stacy's Mom_d4ec623d-04f7-4e27-ab98-084f0afad96b.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/03 - Stereo Love (Extended Version)_e8dd3c19-2728-4d09-a2a5-0d117102e80f.mp3")
song1("../../../sorted_mp3s/All/03 - Stereo Love (Extended Version)_e8dd3c19-2728-4d09-a2a5-0d117102e80f.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/03 - Stronger [Explicit]_61df4268-264f-4b11-a19d-0106cb9d41a7.mp3")
song1("../../../sorted_mp3s/All/03 - Stronger [Explicit]_61df4268-264f-4b11-a19d-0106cb9d41a7.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/03 - Sun & Moon (Original Mix)_45e94ec4-9a6f-4995-847a-4179b6324ac1.mp3")
song1("../../../sorted_mp3s/All/03 - Sun & Moon (Original Mix)_45e94ec4-9a6f-4995-847a-4179b6324ac1.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Survivor’s Guilt (feat. G Herbo) [Explicit]_9b8c252a-e962-46c7-9763-02ec75ed9c15.mp3")
song1("../../../sorted_mp3s/All/03 - Survivor’s Guilt (feat. G Herbo) [Explicit]_9b8c252a-e962-46c7-9763-02ec75ed9c15.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Your Eyes_9683c093-72ed-4987-8755-c2eeebbb1e46.mp3")
song1("../../../sorted_mp3s/All/03 - Your Eyes_9683c093-72ed-4987-8755-c2eeebbb1e46.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/03 - Zhudio54 [Explicit]_4e657273-157a-4c85-b4ff-d2ebdcd310cb.mp3")
song1("../../../sorted_mp3s/All/03 - Zhudio54 [Explicit]_4e657273-157a-4c85-b4ff-d2ebdcd310cb.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/03 - a.i.ngel (Become God)_55902378-a178-4983-aa86-9af145ac1562.mp3")
song1("../../../sorted_mp3s/All/03 - a.i.ngel (Become God)_55902378-a178-4983-aa86-9af145ac1562.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Airplanes [Feat. Hayley Williams Of Paramore] (Explicit Album Version) [Explicit]_9de279d7-ffe5-4b98-95db-006bffad6de8.mp3")
song1("../../../sorted_mp3s/All/04 - Airplanes [Feat. Hayley Williams Of Paramore] (Explicit Album Version) [Explicit]_9de279d7-ffe5-4b98-95db-006bffad6de8.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/04 - Bad and Boujee (feat. Lil Uzi Vert) [Explicit]_5f163b65-c091-4323-98f5-5d7c53f6247e.mp3")
song1("../../../sorted_mp3s/All/04 - Bad and Boujee (feat. Lil Uzi Vert) [Explicit]_5f163b65-c091-4323-98f5-5d7c53f6247e.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/04 - Blue Dream_ec2793b2-8e4f-4465-a722-828b23b091a0.mp3")
song1("../../../sorted_mp3s/All/04 - Blue Dream_ec2793b2-8e4f-4465-a722-828b23b091a0.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/04 - Blue [22]_6fbe9387-6be0-4ce0-aacd-338a6cacfaad.mp3")
song1("../../../sorted_mp3s/All/04 - Blue [22]_6fbe9387-6be0-4ce0-aacd-338a6cacfaad.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Brightest Lights (feat. POLIÇA)_2fb04c76-75bf-430d-9987-6086afe78114.mp3")
song1("../../../sorted_mp3s/All/04 - Brightest Lights (feat. POLIÇA)_2fb04c76-75bf-430d-9987-6086afe78114.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Buenos Aires_d8503997-07d4-4b96-a5b5-c5c41701680e.mp3")
song1("../../../sorted_mp3s/All/04 - Buenos Aires_d8503997-07d4-4b96-a5b5-c5c41701680e.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/04 - December [feat. Davey Havok]_486b8ec8-7e3c-4f21-a505-3a12a2e85197.mp3")
song1("../../../sorted_mp3s/All/04 - December [feat. Davey Havok]_486b8ec8-7e3c-4f21-a505-3a12a2e85197.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Desert Woman_211326e9-a7da-4baf-a296-7879287acede.mp3")
song1("../../../sorted_mp3s/All/04 - Desert Woman_211326e9-a7da-4baf-a296-7879287acede.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - ELEMENT. [Explicit]_e9eb9637-31cd-4d05-a5da-672c724b1632.mp3")
song1("../../../sorted_mp3s/All/04 - ELEMENT. [Explicit]_e9eb9637-31cd-4d05-a5da-672c724b1632.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Emoboy303 (SIDE)_c16f25a1-be57-45e4-98b4-c6e1cb2d1b09.mp3")
song1("../../../sorted_mp3s/All/04 - Emoboy303 (SIDE)_c16f25a1-be57-45e4-98b4-c6e1cb2d1b09.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Endlessly_dd6c3437-e46f-4114-9c03-1bfb7c939201.mp3")
song1("../../../sorted_mp3s/All/04 - Endlessly_dd6c3437-e46f-4114-9c03-1bfb7c939201.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Focus_981758a1-df3b-4238-92a6-0da91b1a5dc9.mp3")
song1("../../../sorted_mp3s/All/04 - Focus_981758a1-df3b-4238-92a6-0da91b1a5dc9.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Free [Explicit]_76d0c1ef-a330-4284-9d67-e40d220d1199.mp3")
song1("../../../sorted_mp3s/All/04 - Free [Explicit]_76d0c1ef-a330-4284-9d67-e40d220d1199.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Fukk Sleep [Explicit]_994afbf1-4202-4ed3-b2d5-1d8fdcfcab16.mp3")
song1("../../../sorted_mp3s/All/04 - Fukk Sleep [Explicit]_994afbf1-4202-4ed3-b2d5-1d8fdcfcab16.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/04 - Gold Digger [feat. Jamie Foxx]_c79d7f62-afa6-4e4b-a881-e42608244067.mp3")
song1("../../../sorted_mp3s/All/04 - Gold Digger [feat. Jamie Foxx]_c79d7f62-afa6-4e4b-a881-e42608244067.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/04 - I Don't Fuck With You [feat. E-40] [Explicit]_e9b8591c-2ef8-4829-b516-b7d152b1fae9.mp3")
song1("../../../sorted_mp3s/All/04 - I Don't Fuck With You [feat. E-40] [Explicit]_e9b8591c-2ef8-4829-b516-b7d152b1fae9.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/04 - I Miss You More Than You Think [feat. Lunamatic] [Explicit]_462fff80-5525-4ae5-891c-fcf9f65536c3.mp3")
song1("../../../sorted_mp3s/All/04 - I Miss You More Than You Think [feat. Lunamatic] [Explicit]_462fff80-5525-4ae5-891c-fcf9f65536c3.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - I'm Fallin'_b62096d7-5685-408e-a809-45b886300a0c.mp3")
song1("../../../sorted_mp3s/All/04 - I'm Fallin'_b62096d7-5685-408e-a809-45b886300a0c.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - If You Want It_01e66605-6efc-4f22-8636-ac9002df4a59.mp3")
song1("../../../sorted_mp3s/All/04 - If You Want It_01e66605-6efc-4f22-8636-ac9002df4a59.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Jewel_225b55f6-0e01-4c46-bacb-86727e672cea.mp3")
song1("../../../sorted_mp3s/All/04 - Jewel_225b55f6-0e01-4c46-bacb-86727e672cea.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - L$D [Explicit]_4c62cbbc-5de8-4cfc-9a1e-73ff871874c4.mp3")
song1("../../../sorted_mp3s/All/04 - L$D [Explicit]_4c62cbbc-5de8-4cfc-9a1e-73ff871874c4.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - LVL [Explicit]_7d938ac7-7872-4ffe-8fe5-d694135ffd65.mp3")
song1("../../../sorted_mp3s/All/04 - LVL [Explicit]_7d938ac7-7872-4ffe-8fe5-d694135ffd65.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Limbo_a717375f-cbdd-45a5-9a82-eaa24ea91ec9.mp3")
song1("../../../sorted_mp3s/All/04 - Limbo_a717375f-cbdd-45a5-9a82-eaa24ea91ec9.mp3").playlists = ['All', 'FutureBass_Chillstep']
load_song("../../../sorted_mp3s/All/04 - Magnolia_670313ce-6ff9-47f1-b4ae-ab5430c5d8a8.mp3")
song1("../../../sorted_mp3s/All/04 - Magnolia_670313ce-6ff9-47f1-b4ae-ab5430c5d8a8.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Run This Town [feat. Rihanna & Kanye West] [Explicit]_4e79951b-5215-43b1-9af4-c3cad864991a.mp3")
song1("../../../sorted_mp3s/All/04 - Run This Town [feat. Rihanna & Kanye West] [Explicit]_4e79951b-5215-43b1-9af4-c3cad864991a.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/04 - SAD! [Explicit]_9957672a-9b05-4aab-83af-36ff03d99e87.mp3")
song1("../../../sorted_mp3s/All/04 - SAD! [Explicit]_9957672a-9b05-4aab-83af-36ff03d99e87.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - STEECEY_38b3ec7a-48f7-4c3c-9bae-df62b73693f4.mp3")
song1("../../../sorted_mp3s/All/04 - STEECEY_38b3ec7a-48f7-4c3c-9bae-df62b73693f4.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Stereo Hearts (Feat. Adam Levine)_fe3f709c-fff8-46fc-83b5-09f28fd7a1be.mp3")
song1("../../../sorted_mp3s/All/04 - Stereo Hearts (Feat. Adam Levine)_fe3f709c-fff8-46fc-83b5-09f28fd7a1be.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/04 - Strangers [feat. Tove Lo]_058d4bd5-fb3c-4693-8a62-06e31fc1d639.mp3")
song1("../../../sorted_mp3s/All/04 - Strangers [feat. Tove Lo]_058d4bd5-fb3c-4693-8a62-06e31fc1d639.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Sun Won't Rise_52f63786-1572-40ab-b3f1-a33fc5394bc5.mp3")
song1("../../../sorted_mp3s/All/04 - Sun Won't Rise_52f63786-1572-40ab-b3f1-a33fc5394bc5.mp3").playlists = ['All', 'FutureBass_Chillstep']
load_song("../../../sorted_mp3s/All/04 - Superfriends_ea7249a0-03a4-47ef-808e-8a05b3e9cf75.mp3")
song1("../../../sorted_mp3s/All/04 - Superfriends_ea7249a0-03a4-47ef-808e-8a05b3e9cf75.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Swervin (feat. 6ix9ine) [Explicit]_baf6dd20-eb06-460e-ad08-3f5c08e45394.mp3")
song1("../../../sorted_mp3s/All/04 - Swervin (feat. 6ix9ine) [Explicit]_baf6dd20-eb06-460e-ad08-3f5c08e45394.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/04 - The Art of Peer Pressure [Explicit]_373b423a-e6bc-4e6a-bc43-a0ee4f700c01.mp3")
song1("../../../sorted_mp3s/All/04 - The Art of Peer Pressure [Explicit]_373b423a-e6bc-4e6a-bc43-a0ee4f700c01.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Vibrant_40467a81-bbb9-498a-84f6-cd3f1af03a91.mp3")
song1("../../../sorted_mp3s/All/04 - Vibrant_40467a81-bbb9-498a-84f6-cd3f1af03a91.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Vigilantes_99bfb461-dbd8-40d5-bdc5-8ef521091d52.mp3")
song1("../../../sorted_mp3s/All/04 - Vigilantes_99bfb461-dbd8-40d5-bdc5-8ef521091d52.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Wassup [Explicit]_ff944562-abb0-47ed-a3dd-d14add59951c.mp3")
song1("../../../sorted_mp3s/All/04 - Wassup [Explicit]_ff944562-abb0-47ed-a3dd-d14add59951c.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - Will I Ever Find Love_7a9883d7-d6fe-4ee6-9384-605c83e12979.mp3")
song1("../../../sorted_mp3s/All/04 - Will I Ever Find Love_7a9883d7-d6fe-4ee6-9384-605c83e12979.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/04 - You Were Right_d7801f91-44bc-4a72-b436-7157bc569493.mp3")
song1("../../../sorted_mp3s/All/04 - You Were Right_d7801f91-44bc-4a72-b436-7157bc569493.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/05 - Adieu_4ed02be0-41bc-4294-8448-278a3b32c03f.mp3")
song1("../../../sorted_mp3s/All/05 - Adieu_4ed02be0-41bc-4294-8448-278a3b32c03f.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - Alive_0cf73583-52d0-465b-8405-8f7db31dcdf2.mp3")
song1("../../../sorted_mp3s/All/05 - Alive_0cf73583-52d0-465b-8405-8f7db31dcdf2.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - Black Room Boy (Original Mix)_9af15a72-db42-467c-9fb8-bb9068c84dde.mp3")
song1("../../../sorted_mp3s/All/05 - Black Room Boy (Original Mix)_9af15a72-db42-467c-9fb8-bb9068c84dde.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - Cage_d0b7d504-5592-41ca-b56e-0deb3dcb2aac.mp3")
song1("../../../sorted_mp3s/All/05 - Cage_d0b7d504-5592-41ca-b56e-0deb3dcb2aac.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - Can't Sleep_ed561926-4fe8-4419-b38f-3c5e2bb6ca47.mp3")
song1("../../../sorted_mp3s/All/05 - Can't Sleep_ed561926-4fe8-4419-b38f-3c5e2bb6ca47.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - Do You Don't You_83285083-eee3-40f8-9c26-ebe46efc8edc.mp3")
song1("../../../sorted_mp3s/All/05 - Do You Don't You_83285083-eee3-40f8-9c26-ebe46efc8edc.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/05 - Don't Let Me Down_2cddc586-0839-4371-9071-0996534dfbe7.mp3")
song1("../../../sorted_mp3s/All/05 - Don't Let Me Down_2cddc586-0839-4371-9071-0996534dfbe7.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/05 - Empire State Of Mind [feat. Alicia Keys] [Explicit]_a84b6d38-6e68-410f-88ca-f81a16ec0dc5.mp3")
song1("../../../sorted_mp3s/All/05 - Empire State Of Mind [feat. Alicia Keys] [Explicit]_a84b6d38-6e68-410f-88ca-f81a16ec0dc5.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/05 - Excuse Me [Explicit]_cda42b74-c213-42c0-93bb-07885f750495.mp3")
song1("../../../sorted_mp3s/All/05 - Excuse Me [Explicit]_cda42b74-c213-42c0-93bb-07885f750495.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - Falling For You_d44862d4-235e-4d05-9440-5bce871641bb.mp3")
song1("../../../sorted_mp3s/All/05 - Falling For You_d44862d4-235e-4d05-9440-5bce871641bb.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - Firestone_ef370dd4-e4af-4b93-8b81-90d89523e612.mp3")
song1("../../../sorted_mp3s/All/05 - Firestone_ef370dd4-e4af-4b93-8b81-90d89523e612.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/05 - Hell [Explicit]_7505b864-f475-42da-be1c-e47463ce6e96.mp3")
song1("../../../sorted_mp3s/All/05 - Hell [Explicit]_7505b864-f475-42da-be1c-e47463ce6e96.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - Hmm_5bebe31b-0a8e-4da4-bfd5-3f42d6d6e5f5.mp3")
song1("../../../sorted_mp3s/All/05 - Hmm_5bebe31b-0a8e-4da4-bfd5-3f42d6d6e5f5.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - How Does It Feel [feat. Channel Tres] [Explicit]_6d1865d6-cd94-4ed0-a675-c9ab6b13b999.mp3")
song1("../../../sorted_mp3s/All/05 - How Does It Feel [feat. Channel Tres] [Explicit]_6d1865d6-cd94-4ed0-a675-c9ab6b13b999.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/05 - LOW RIDE_43750173-6cc9-4643-a7df-a6cfd9cfaed7.mp3")
song1("../../../sorted_mp3s/All/05 - LOW RIDE_43750173-6cc9-4643-a7df-a6cfd9cfaed7.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - Low (feat. T-Pain)_9a969933-fa29-4b4f-9c3b-055ed2a6a346.mp3")
song1("../../../sorted_mp3s/All/05 - Low (feat. T-Pain)_9a969933-fa29-4b4f-9c3b-055ed2a6a346.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/05 - PUFFIN ON ZOOTIEZ [Explicit]_50c76200-f0a9-49e8-8610-ca81fdc8ac48.mp3")
song1("../../../sorted_mp3s/All/05 - PUFFIN ON ZOOTIEZ [Explicit]_50c76200-f0a9-49e8-8610-ca81fdc8ac48.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - Praise The Lord (Da Shine) [Explicit]_bc2115c2-a8c8-40e5-beb1-e75aca0b2597.mp3")
song1("../../../sorted_mp3s/All/05 - Praise The Lord (Da Shine) [Explicit]_bc2115c2-a8c8-40e5-beb1-e75aca0b2597.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/05 - Praise_65415713-b9fd-4dc8-820f-5c541f19b53e.mp3")
song1("../../../sorted_mp3s/All/05 - Praise_65415713-b9fd-4dc8-820f-5c541f19b53e.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/05 - Reflex [Explicit]_082ab9c9-eee8-4a14-9068-bd4d6cf10c82.mp3")
song1("../../../sorted_mp3s/All/05 - Reflex [Explicit]_082ab9c9-eee8-4a14-9068-bd4d6cf10c82.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - Rumor [feat. WYN]_149bd3c1-1d4c-42bf-b910-329102e13e67.mp3")
song1("../../../sorted_mp3s/All/05 - Rumor [feat. WYN]_149bd3c1-1d4c-42bf-b910-329102e13e67.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - The Last [Explicit]_8c1f08ef-f9c4-41c0-b1b5-42571c589b96.mp3")
song1("../../../sorted_mp3s/All/05 - The Last [Explicit]_8c1f08ef-f9c4-41c0-b1b5-42571c589b96.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - To Ü (feat. AlunaGeorge)_ee7f73c2-ce19-4fd7-8982-0323baeb5b9e.mp3")
song1("../../../sorted_mp3s/All/05 - To Ü (feat. AlunaGeorge)_ee7f73c2-ce19-4fd7-8982-0323baeb5b9e.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/05 - With You_6fc48b61-7f8e-4b26-92f1-b3ace74f4d8e.mp3")
song1("../../../sorted_mp3s/All/05 - With You_6fc48b61-7f8e-4b26-92f1-b3ace74f4d8e.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/05 - Without You (Feat. Usher)_7e486626-6fb1-4c7d-a931-d0680cdcfc38.mp3")
song1("../../../sorted_mp3s/All/05 - Without You (Feat. Usher)_7e486626-6fb1-4c7d-a931-d0680cdcfc38.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/05 - World To Me (Rootkit Remix)_d9111496-9a4c-473c-849e-fbc4ccdce725.mp3")
song1("../../../sorted_mp3s/All/05 - World To Me (Rootkit Remix)_d9111496-9a4c-473c-849e-fbc4ccdce725.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/05 - _1000 [miles]_400b449d-b0f9-4b13-8289-8434fb216a41.mp3")
song1("../../../sorted_mp3s/All/05 - _1000 [miles]_400b449d-b0f9-4b13-8289-8434fb216a41.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - 743⁺Aether_✧ ˳ ⁎ ¹¹¹} ⁺ . ˳ [Explicit]_73468689-3007-4bb3-bbb9-f381405b7180.mp3")
song1("../../../sorted_mp3s/All/06 - 743⁺Aether_✧ ˳ ⁎ ¹¹¹} ⁺ . ˳ [Explicit]_73468689-3007-4bb3-bbb9-f381405b7180.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - Alive (Reprise)_80630562-da6d-4eab-bc77-f324b27af68a.mp3")
song1("../../../sorted_mp3s/All/06 - Alive (Reprise)_80630562-da6d-4eab-bc77-f324b27af68a.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - Burn_9e0d5679-b417-4015-8c74-9f30d786b503.mp3")
song1("../../../sorted_mp3s/All/06 - Burn_9e0d5679-b417-4015-8c74-9f30d786b503.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - Come Get Her [Explicit]_4f42ebfe-6b08-41cc-a531-fb5636a4f727.mp3")
song1("../../../sorted_mp3s/All/06 - Come Get Her [Explicit]_4f42ebfe-6b08-41cc-a531-fb5636a4f727.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/06 - Dark Horse [feat. Juicy J]_abd8632a-00dd-4c25-987a-4492149a64cb.mp3")
song1("../../../sorted_mp3s/All/06 - Dark Horse [feat. Juicy J]_abd8632a-00dd-4c25-987a-4492149a64cb.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/06 - Doses & Mimosas [Explicit]_b16e0b35-0b3a-4aa6-98c9-7ac3340ec1e8.mp3")
song1("../../../sorted_mp3s/All/06 - Doses & Mimosas [Explicit]_b16e0b35-0b3a-4aa6-98c9-7ac3340ec1e8.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/06 - For Billy_50edd5ad-24a2-4e6f-ad53-a0065aa906c6.mp3")
song1("../../../sorted_mp3s/All/06 - For Billy_50edd5ad-24a2-4e6f-ad53-a0065aa906c6.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - Good Life [Explicit]_a21bc10b-c515-4237-8d73-972046006c12.mp3")
song1("../../../sorted_mp3s/All/06 - Good Life [Explicit]_a21bc10b-c515-4237-8d73-972046006c12.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/06 - LaLaLa_b03667cb-d471-4a40-accf-ba0a7d7b937b.mp3")
song1("../../../sorted_mp3s/All/06 - LaLaLa_b03667cb-d471-4a40-accf-ba0a7d7b937b.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - MTFU [Explicit]_ad44b5d3-a479-4d3d-b12c-a997cf90f7f5.mp3")
song1("../../../sorted_mp3s/All/06 - MTFU [Explicit]_ad44b5d3-a479-4d3d-b12c-a997cf90f7f5.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - Mental [feat. Saul Williams & Bridget Perez] [Explicit]_4950e42d-285e-4fa2-9197-12ac923e5298.mp3")
song1("../../../sorted_mp3s/All/06 - Mental [feat. Saul Williams & Bridget Perez] [Explicit]_4950e42d-285e-4fa2-9197-12ac923e5298.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - Pretty Little Fears [feat. J. Cole] [Explicit]_74c506d0-bf80-443e-aaeb-3024a0bb2458.mp3")
song1("../../../sorted_mp3s/All/06 - Pretty Little Fears [feat. J. Cole] [Explicit]_74c506d0-bf80-443e-aaeb-3024a0bb2458.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - Remedy (feat. TS Graye)_bd8a349e-c667-4a13-9b07-1cd6510a204c.mp3")
song1("../../../sorted_mp3s/All/06 - Remedy (feat. TS Graye)_bd8a349e-c667-4a13-9b07-1cd6510a204c.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - Stay With Me_0f1a7745-83d5-4c6e-976b-13c67f308f16.mp3")
song1("../../../sorted_mp3s/All/06 - Stay With Me_0f1a7745-83d5-4c6e-976b-13c67f308f16.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - Stir Me Up_d4be97ad-feb3-4b3b-8687-03bcda0a7c51.mp3")
song1("../../../sorted_mp3s/All/06 - Stir Me Up_d4be97ad-feb3-4b3b-8687-03bcda0a7c51.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - The Show Goes On [Explicit]_c50e4bde-f0d3-4653-a26a-90ef144b9b90.mp3")
song1("../../../sorted_mp3s/All/06 - The Show Goes On [Explicit]_c50e4bde-f0d3-4653-a26a-90ef144b9b90.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/06 - U & Me_dbe47fda-c799-438b-bc46-4dcc6c3f10de.mp3")
song1("../../../sorted_mp3s/All/06 - U & Me_dbe47fda-c799-438b-bc46-4dcc6c3f10de.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - Viridian Dream_a1619b14-d0b6-41fd-b4a2-640bc607e553.mp3")
song1("../../../sorted_mp3s/All/06 - Viridian Dream_a1619b14-d0b6-41fd-b4a2-640bc607e553.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - Voodoo_55c44146-9b8b-4507-9ca3-4ac0e8f98a1d.mp3")
song1("../../../sorted_mp3s/All/06 - Voodoo_55c44146-9b8b-4507-9ca3-4ac0e8f98a1d.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/06 - rockstar [feat. 21 Savage] [Explicit]_1a7510af-481a-4dc5-b61a-ade4f6cd3044.mp3")
song1("../../../sorted_mp3s/All/06 - rockstar [feat. 21 Savage] [Explicit]_1a7510af-481a-4dc5-b61a-ade4f6cd3044.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - All On Me_6fe640db-b8c9-49b0-9faf-68b283a02ffa.mp3")
song1("../../../sorted_mp3s/All/07 - All On Me_6fe640db-b8c9-49b0-9faf-68b283a02ffa.mp3").playlists = ['All', 'Tech_BassHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - Arc Second_f9ac2fb1-bb81-432d-9b36-b44772073155.mp3")
song1("../../../sorted_mp3s/All/07 - Arc Second_f9ac2fb1-bb81-432d-9b36-b44772073155.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - Artificial Skin_f244af4a-1ccf-48e6-ab21-f919851496eb.mp3")
song1("../../../sorted_mp3s/All/07 - Artificial Skin_f244af4a-1ccf-48e6-ab21-f919851496eb.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - Ass Back Home (Feat. Neon Hitch) [Explicit]_7ab7d094-cd1f-4a66-bdee-af703796f002.mp3")
song1("../../../sorted_mp3s/All/07 - Ass Back Home (Feat. Neon Hitch) [Explicit]_7ab7d094-cd1f-4a66-bdee-af703796f002.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/07 - Be Like You (feat. Broods) [Whethan Remix]_9a8dd8e0-e79a-48d8-8adc-944f6414f647.mp3")
song1("../../../sorted_mp3s/All/07 - Be Like You (feat. Broods) [Whethan Remix]_9a8dd8e0-e79a-48d8-8adc-944f6414f647.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/07 - Day 'N' Nite (Nightmare)_be323a3e-15f0-4fb0-898a-6fa5142f3205.mp3")
song1("../../../sorted_mp3s/All/07 - Day 'N' Nite (Nightmare)_be323a3e-15f0-4fb0-898a-6fa5142f3205.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/07 - FRIDAY_ae124ff0-cb83-4cec-a499-9e2fa4094e56.mp3")
song1("../../../sorted_mp3s/All/07 - FRIDAY_ae124ff0-cb83-4cec-a499-9e2fa4094e56.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - F__kin' Problems [Explicit]_5aef6a7e-f739-4017-9f49-7b9905c264e7.mp3")
song1("../../../sorted_mp3s/All/07 - F__kin' Problems [Explicit]_5aef6a7e-f739-4017-9f49-7b9905c264e7.mp3").playlists = ['All', 'Hits_Throwbacks', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - I'll Be Fine (Zes Remix)_2fd88520-aa6d-4a5e-a1a7-de118ea8fd8a.mp3")
song1("../../../sorted_mp3s/All/07 - I'll Be Fine (Zes Remix)_2fd88520-aa6d-4a5e-a1a7-de118ea8fd8a.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - Is It Cold In The Water_ (Flume & Eprom Remix)_ca924d98-8cfd-4bf2-a755-74d76482fd90.mp3")
song1("../../../sorted_mp3s/All/07 - Is It Cold In The Water_ (Flume & Eprom Remix)_ca924d98-8cfd-4bf2-a755-74d76482fd90.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - Lord Pretty Flacko Jodye 2 (LPFJ2) [Explicit]_81648aa3-6692-41ca-b289-48ac91d4b47b.mp3")
song1("../../../sorted_mp3s/All/07 - Lord Pretty Flacko Jodye 2 (LPFJ2) [Explicit]_81648aa3-6692-41ca-b289-48ac91d4b47b.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - Mantra_13daf691-9bd7-41d0-9460-6d0f130cc220.mp3")
song1("../../../sorted_mp3s/All/07 - Mantra_13daf691-9bd7-41d0-9460-6d0f130cc220.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - On My Knees_2d93db5e-0024-4f12-bd0e-3a36c2426aa7.mp3")
song1("../../../sorted_mp3s/All/07 - On My Knees_2d93db5e-0024-4f12-bd0e-3a36c2426aa7.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - Pretty Thoughts_97fcf19d-6b2e-4d0f-b4f2-4feb198ddedc.mp3")
song1("../../../sorted_mp3s/All/07 - Pretty Thoughts_97fcf19d-6b2e-4d0f-b4f2-4feb198ddedc.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - Running To The Sea (Seven Lions Remix) [feat. Susanne Sundfør]_095028e6-6d10-4ccd-a21d-2f27bd7fe6e1.mp3")
song1("../../../sorted_mp3s/All/07 - Running To The Sea (Seven Lions Remix) [feat. Susanne Sundfør]_095028e6-6d10-4ccd-a21d-2f27bd7fe6e1.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - Still (feat. 6LACK and Smino) [Explicit]_9424a44d-1def-407c-9777-1fd24e41d9b6.mp3")
song1("../../../sorted_mp3s/All/07 - Still (feat. 6LACK and Smino) [Explicit]_9424a44d-1def-407c-9777-1fd24e41d9b6.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - Sunset Lover (Zac Samuel Remix)_9f2e9ddd-a44f-44f3-b59a-a19cb9de0e8b.mp3")
song1("../../../sorted_mp3s/All/07 - Sunset Lover (Zac Samuel Remix)_9f2e9ddd-a44f-44f3-b59a-a19cb9de0e8b.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/07 - Underwater_e4648862-c5ea-4513-aa58-df3ae4b5b6d7.mp3")
song1("../../../sorted_mp3s/All/07 - Underwater_e4648862-c5ea-4513-aa58-df3ae4b5b6d7.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/07 - p r i d e . i s . t h e . d e v i l [Explicit]_30ffe7df-4f68-4f51-99cf-af9d0fead5a9.mp3")
song1("../../../sorted_mp3s/All/07 - p r i d e . i s . t h e . d e v i l [Explicit]_30ffe7df-4f68-4f51-99cf-af9d0fead5a9.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/08 - CONTACT_b3351107-36de-4ec8-bbaa-62f53a365d8a.mp3")
song1("../../../sorted_mp3s/All/08 - CONTACT_b3351107-36de-4ec8-bbaa-62f53a365d8a.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/08 - Close Your Eyes_332b1001-2d8b-4d06-82c9-12295fc54c44.mp3")
song1("../../../sorted_mp3s/All/08 - Close Your Eyes_332b1001-2d8b-4d06-82c9-12295fc54c44.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/08 - Feels [Explicit]_db93df8c-ed85-46d6-944d-cd51d1981eca.mp3")
song1("../../../sorted_mp3s/All/08 - Feels [Explicit]_db93df8c-ed85-46d6-944d-cd51d1981eca.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/08 - Hold On, We're Going Home [feat. Majid Jordan]_dce71412-955c-49c4-9c74-56946b634f3f.mp3")
song1("../../../sorted_mp3s/All/08 - Hold On, We're Going Home [feat. Majid Jordan]_dce71412-955c-49c4-9c74-56946b634f3f.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/08 - I Cry_f51e5f06-66d6-4eab-a5e8-d79d9eef8608.mp3")
song1("../../../sorted_mp3s/All/08 - I Cry_f51e5f06-66d6-4eab-a5e8-d79d9eef8608.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/08 - I Need Your Love_446b90f6-0801-4b09-92c1-e1540ebca7f2.mp3")
song1("../../../sorted_mp3s/All/08 - I Need Your Love_446b90f6-0801-4b09-92c1-e1540ebca7f2.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/08 - Living, Breathing_76bc9357-ec96-4268-83f0-8dc8e7bc85f7.mp3")
song1("../../../sorted_mp3s/All/08 - Living, Breathing_76bc9357-ec96-4268-83f0-8dc8e7bc85f7.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/08 - Miami_042b7d1a-87b1-4b1e-af93-5ab69a20040b.mp3")
song1("../../../sorted_mp3s/All/08 - Miami_042b7d1a-87b1-4b1e-af93-5ab69a20040b.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/08 - Pleasure Model (Synergy Remix)_3bda1f7b-f761-4c51-b1b2-d31ea8a41cd5.mp3")
song1("../../../sorted_mp3s/All/08 - Pleasure Model (Synergy Remix)_3bda1f7b-f761-4c51-b1b2-d31ea8a41cd5.mp3").playlists = ['All', 'Drum&Bass']
load_song("../../../sorted_mp3s/All/08 - Risky Business_039534db-55a3-4745-a7f3-6c312d968cb3.mp3")
song1("../../../sorted_mp3s/All/08 - Risky Business_039534db-55a3-4745-a7f3-6c312d968cb3.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/08 - Summer_3d9ad131-d2f3-4ab2-9e84-afd43d733933.mp3")
song1("../../../sorted_mp3s/All/08 - Summer_3d9ad131-d2f3-4ab2-9e84-afd43d733933.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/08 - The Last Goodbye (feat. Bettye LaVette)_a937e28f-2bd9-446a-bc2d-ce2a2aede64b.mp3")
song1("../../../sorted_mp3s/All/08 - The Last Goodbye (feat. Bettye LaVette)_a937e28f-2bd9-446a-bc2d-ce2a2aede64b.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/08 - Throw Sum Mo [feat. Nicki Minaj & Young Thug] [Explicit]_5c8c4eb1-6696-4c47-9288-b3a1c352612c.mp3")
song1("../../../sorted_mp3s/All/08 - Throw Sum Mo [feat. Nicki Minaj & Young Thug] [Explicit]_5c8c4eb1-6696-4c47-9288-b3a1c352612c.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/08 - Wasted [feat. Matthew Koma]_562377bc-50d5-4bcd-b09e-c97096d6130d.mp3")
song1("../../../sorted_mp3s/All/08 - Wasted [feat. Matthew Koma]_562377bc-50d5-4bcd-b09e-c97096d6130d.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/08 - Wildfire_7b359e99-cbdc-4f68-a383-b192700f54ea.mp3")
song1("../../../sorted_mp3s/All/08 - Wildfire_7b359e99-cbdc-4f68-a383-b192700f54ea.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/08 - You & Me (Flume Remix) [feat. Eliza Doolittle]_a9c2673e-5bbd-4007-a946-3a00cc86949f.mp3")
song1("../../../sorted_mp3s/All/08 - You & Me (Flume Remix) [feat. Eliza Doolittle]_a9c2673e-5bbd-4007-a946-3a00cc86949f.mp3").playlists = ['All', 'FutureBass_Chillstep']
load_song("../../../sorted_mp3s/All/08 - infinity (888) [feat. Joey Bada$$] [Explicit]_2b5755ef-fe2e-49a0-b9b7-03ff6a624b3b.mp3")
song1("../../../sorted_mp3s/All/08 - infinity (888) [feat. Joey Bada$$] [Explicit]_2b5755ef-fe2e-49a0-b9b7-03ff6a624b3b.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/09 - 3005 [Explicit]_1996540a-5045-4c95-a853-6142b32494c4.mp3")
song1("../../../sorted_mp3s/All/09 - 3005 [Explicit]_1996540a-5045-4c95-a853-6142b32494c4.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/09 - All I Got_0b6cb830-afe4-43ed-a0b9-f3b01d51592a.mp3")
song1("../../../sorted_mp3s/All/09 - All I Got_0b6cb830-afe4-43ed-a0b9-f3b01d51592a.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/09 - Blinding Lights_8020ae33-c816-4d70-9767-623c93e7af1e.mp3")
song1("../../../sorted_mp3s/All/09 - Blinding Lights_8020ae33-c816-4d70-9767-623c93e7af1e.mp3").playlists = ['All', 'Hits_Throwbacks', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/09 - Dead Limit_cfadfbcb-96c7-4fc6-a6e4-99d28fe3e0df.mp3")
song1("../../../sorted_mp3s/All/09 - Dead Limit_cfadfbcb-96c7-4fc6-a6e4-99d28fe3e0df.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/09 - Empire State Of Mind [feat. Alicia Keys]_b97fa16b-08f9-4097-9335-158e8992898b.mp3")
song1("../../../sorted_mp3s/All/09 - Empire State Of Mind [feat. Alicia Keys]_b97fa16b-08f9-4097-9335-158e8992898b.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/09 - Go Flex [Explicit]_e49bdc39-45da-4aec-bf6f-3b8ef020aa41.mp3")
song1("../../../sorted_mp3s/All/09 - Go Flex [Explicit]_e49bdc39-45da-4aec-bf6f-3b8ef020aa41.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/09 - IM GONE [Explicit]_1d331a6f-f532-4d6e-a734-ff713bcf4ead.mp3")
song1("../../../sorted_mp3s/All/09 - IM GONE [Explicit]_1d331a6f-f532-4d6e-a734-ff713bcf4ead.mp3").playlists = ['All', 'Tech_BassHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/09 - KEEP MOVING_d42465d0-b367-44bb-9e74-7368d5cbb6ba.mp3")
song1("../../../sorted_mp3s/All/09 - KEEP MOVING_d42465d0-b367-44bb-9e74-7368d5cbb6ba.mp3").playlists = ['All', 'Trap_Midtempo']
load_song("../../../sorted_mp3s/All/09 - Pressure_ad20a80f-8dfe-4638-adf1-de85a734d38e.mp3")
song1("../../../sorted_mp3s/All/09 - Pressure_ad20a80f-8dfe-4638-adf1-de85a734d38e.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/09 - Soldier (feat. Pivot Gang) [Explicit]_c3cbbac0-259a-48c1-badf-a6ceea722c6c.mp3")
song1("../../../sorted_mp3s/All/09 - Soldier (feat. Pivot Gang) [Explicit]_c3cbbac0-259a-48c1-badf-a6ceea722c6c.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/09 - Swimming Pools (Drank) (Extended Version) [Explicit]_7983b77e-06dd-40dc-aad4-480c1f2bb5fd.mp3")
song1("../../../sorted_mp3s/All/09 - Swimming Pools (Drank) (Extended Version) [Explicit]_7983b77e-06dd-40dc-aad4-480c1f2bb5fd.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/09 - To Me [Explicit]_e3887fe3-76fc-428c-bec0-a23cf521dda7.mp3")
song1("../../../sorted_mp3s/All/09 - To Me [Explicit]_e3887fe3-76fc-428c-bec0-a23cf521dda7.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/09 - Where Are Ü Now (with Justin Bieber)_80126e35-f6b9-404e-a343-7a3f0d474898.mp3")
song1("../../../sorted_mp3s/All/09 - Where Are Ü Now (with Justin Bieber)_80126e35-f6b9-404e-a343-7a3f0d474898.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/09 - X-Wing [Explicit]_918af6ce-dc29-4e41-9fd3-78fa59ccce51.mp3")
song1("../../../sorted_mp3s/All/09 - X-Wing [Explicit]_918af6ce-dc29-4e41-9fd3-78fa59ccce51.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/09 - goosebumps [Explicit]_385bd371-c822-4994-ae0e-e42c2be8f16d.mp3")
song1("../../../sorted_mp3s/All/09 - goosebumps [Explicit]_385bd371-c822-4994-ae0e-e42c2be8f16d.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/10 - Choosing For You (Holly Remix)_3be8c0e3-0bc6-4bd0-b97b-01c3de14f8cb.mp3")
song1("../../../sorted_mp3s/All/10 - Choosing For You (Holly Remix)_3be8c0e3-0bc6-4bd0-b97b-01c3de14f8cb.mp3").playlists = ['All', 'Trap_Midtempo']
load_song("../../../sorted_mp3s/All/10 - DAWN_758902fa-bc46-4890-8ae9-5dba0fdca793.mp3")
song1("../../../sorted_mp3s/All/10 - DAWN_758902fa-bc46-4890-8ae9-5dba0fdca793.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/10 - Desire (Single Edit)_a39cb135-8957-4dfe-b60e-7698c779013a.mp3")
song1("../../../sorted_mp3s/All/10 - Desire (Single Edit)_a39cb135-8957-4dfe-b60e-7698c779013a.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/10 - Devotion_4f08aae2-1c1c-4613-be20-c409fe06d314.mp3")
song1("../../../sorted_mp3s/All/10 - Devotion_4f08aae2-1c1c-4613-be20-c409fe06d314.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/10 - Drift_3f400647-e135-46d4-a862-2e9573410b49.mp3")
song1("../../../sorted_mp3s/All/10 - Drift_3f400647-e135-46d4-a862-2e9573410b49.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/10 - Era_494da4d4-3099-46e2-b51c-28008e93f79b.mp3")
song1("../../../sorted_mp3s/All/10 - Era_494da4d4-3099-46e2-b51c-28008e93f79b.mp3").playlists = ['All', 'Trap_Midtempo']
load_song("../../../sorted_mp3s/All/10 - Ex Calling [Explicit]_9894876b-1629-46f8-9380-6fea6b85a11a.mp3")
song1("../../../sorted_mp3s/All/10 - Ex Calling [Explicit]_9894876b-1629-46f8-9380-6fea6b85a11a.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/10 - Fashion Killa [Explicit]_dcb86cd2-6161-462d-b55d-ec70d6bb4633.mp3")
song1("../../../sorted_mp3s/All/10 - Fashion Killa [Explicit]_dcb86cd2-6161-462d-b55d-ec70d6bb4633.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/10 - Higher Love_689e2cb8-7c2a-43c3-b928-333f7186be7d.mp3")
song1("../../../sorted_mp3s/All/10 - Higher Love_689e2cb8-7c2a-43c3-b928-333f7186be7d.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/10 - If I Had A Dollar (feat. Benjamin Earl Turner) [Explicit]_7397b177-6faa-4538-8820-9963cb4c4b53.mp3")
song1("../../../sorted_mp3s/All/10 - If I Had A Dollar (feat. Benjamin Earl Turner) [Explicit]_7397b177-6faa-4538-8820-9963cb4c4b53.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/10 - Losing Patience_fe5ec62d-cf89-4a12-88f5-e42c7063723c.mp3")
song1("../../../sorted_mp3s/All/10 - Losing Patience_fe5ec62d-cf89-4a12-88f5-e42c7063723c.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/10 - No Type [Explicit]_638e5e20-1b37-49eb-9aa1-98a1b5552558.mp3")
song1("../../../sorted_mp3s/All/10 - No Type [Explicit]_638e5e20-1b37-49eb-9aa1-98a1b5552558.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/10 - RAIN [Explicit]_351895e4-83e5-4e76-acb4-0323b21a5afc.mp3")
song1("../../../sorted_mp3s/All/10 - RAIN [Explicit]_351895e4-83e5-4e76-acb4-0323b21a5afc.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/10 - Shellshock (Original)_b7e6c81c-d3c5-4b85-8ffc-d9b86556c468.mp3")
song1("../../../sorted_mp3s/All/10 - Shellshock (Original)_b7e6c81c-d3c5-4b85-8ffc-d9b86556c468.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/10 - Sweet Nothing_eed6f7ae-3f64-4303-a554-0669c389a9e8.mp3")
song1("../../../sorted_mp3s/All/10 - Sweet Nothing_eed6f7ae-3f64-4303-a554-0669c389a9e8.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/10 - Voices_4ac67f4f-1e05-48ad-9450-7e1b52528601.mp3")
song1("../../../sorted_mp3s/All/10 - Voices_4ac67f4f-1e05-48ad-9450-7e1b52528601.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/11 - Alone _ EA6 [Explicit]_e8f79d3f-29de-47d2-b51c-5a9531c776c9.mp3")
song1("../../../sorted_mp3s/All/11 - Alone _ EA6 [Explicit]_e8f79d3f-29de-47d2-b51c-5a9531c776c9.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/11 - Atoms (Said the Sky Remix)_df6d1c0b-6a0a-4cf8-b6f8-61bad929964d.mp3")
song1("../../../sorted_mp3s/All/11 - Atoms (Said the Sky Remix)_df6d1c0b-6a0a-4cf8-b6f8-61bad929964d.mp3").playlists = ['All', 'FutureBass_Chillstep']
load_song("../../../sorted_mp3s/All/11 - Drive (Edit)_24273181-5043-4169-b71c-8fc30101b7a8.mp3")
song1("../../../sorted_mp3s/All/11 - Drive (Edit)_24273181-5043-4169-b71c-8fc30101b7a8.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/11 - Fellow Feeling_0bbdd3b7-ffa9-4a22-834d-954300326421.mp3")
song1("../../../sorted_mp3s/All/11 - Fellow Feeling_0bbdd3b7-ffa9-4a22-834d-954300326421.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/11 - Forget About Me (Nite Version)_b906b447-c869-400c-b490-c987d72140df.mp3")
song1("../../../sorted_mp3s/All/11 - Forget About Me (Nite Version)_b906b447-c869-400c-b490-c987d72140df.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/11 - I'll Wait_0dfe03e0-34e4-44ab-8d1a-1e0c3590330c.mp3")
song1("../../../sorted_mp3s/All/11 - I'll Wait_0dfe03e0-34e4-44ab-8d1a-1e0c3590330c.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/11 - MUD_3fd93f4b-a187-41e9-a54a-c3340e507c88.mp3")
song1("../../../sorted_mp3s/All/11 - MUD_3fd93f4b-a187-41e9-a54a-c3340e507c88.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/11 - Quarantine Wifey (feat. JID) [Explicit]_40c62d8b-e2f4-4db9-854a-30faec65b9f5.mp3")
song1("../../../sorted_mp3s/All/11 - Quarantine Wifey (feat. JID) [Explicit]_40c62d8b-e2f4-4db9-854a-30faec65b9f5.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/11 - Scripture [Explicit]_b5c1e616-6671-4674-b21c-752333072375.mp3")
song1("../../../sorted_mp3s/All/11 - Scripture [Explicit]_b5c1e616-6671-4674-b21c-752333072375.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/11 - The Flood_11e87b97-1da3-4904-b386-79f462ff3f9e.mp3")
song1("../../../sorted_mp3s/All/11 - The Flood_11e87b97-1da3-4904-b386-79f462ff3f9e.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/11 - XXX. FT. U2. [Explicit]_30041044-6d52-4ac1-a5eb-d55d5a2d8a77.mp3")
song1("../../../sorted_mp3s/All/11 - XXX. FT. U2. [Explicit]_30041044-6d52-4ac1-a5eb-d55d5a2d8a77.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/12 - Alright_1ba70d75-a4b4-41b7-8aee-fcf36b627c70.mp3")
song1("../../../sorted_mp3s/All/12 - Alright_1ba70d75-a4b4-41b7-8aee-fcf36b627c70.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/12 - Are You With Me (Radio Edit)_b37c1af0-f9c4-48c9-b11d-b46db044fc55.mp3")
song1("../../../sorted_mp3s/All/12 - Are You With Me (Radio Edit)_b37c1af0-f9c4-48c9-b11d-b46db044fc55.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/12 - Higher_7d0c7f4e-90e1-48d0-a0d5-5b7f9d44b985.mp3")
song1("../../../sorted_mp3s/All/12 - Higher_7d0c7f4e-90e1-48d0-a0d5-5b7f9d44b985.mp3").playlists = ['All', 'Tech_BassHouse']
load_song("../../../sorted_mp3s/All/12 - I Wanna Know_1341ce27-daf4-4db3-a8da-98b1b2b10bc6.mp3")
song1("../../../sorted_mp3s/All/12 - I Wanna Know_1341ce27-daf4-4db3-a8da-98b1b2b10bc6.mp3").playlists = ['All', 'FutureBass_Chillstep']
load_song("../../../sorted_mp3s/All/12 - Leaf [Explicit]_c5c4a560-c8c8-45a8-bcfa-21c7bc0e50c1.mp3")
song1("../../../sorted_mp3s/All/12 - Leaf [Explicit]_c5c4a560-c8c8-45a8-bcfa-21c7bc0e50c1.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/12 - Never Gonna Forget_532629cb-2e71-4f52-9c93-f5a048cf7de3.mp3")
song1("../../../sorted_mp3s/All/12 - Never Gonna Forget_532629cb-2e71-4f52-9c93-f5a048cf7de3.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/12 - Nonchalant [Explicit]_b62caf51-bead-4d2e-a5c9-65f3e2489675.mp3")
song1("../../../sorted_mp3s/All/12 - Nonchalant [Explicit]_b62caf51-bead-4d2e-a5c9-65f3e2489675.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/12 - RIVER ROAD [Explicit]_849587d4-1a46-4365-bebd-4ce9d809d1f0.mp3")
song1("../../../sorted_mp3s/All/12 - RIVER ROAD [Explicit]_849587d4-1a46-4365-bebd-4ce9d809d1f0.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/12 - Sad Songs [Explicit]_71841914-3d36-441d-934e-ba5bdec97722.mp3")
song1("../../../sorted_mp3s/All/12 - Sad Songs [Explicit]_71841914-3d36-441d-934e-ba5bdec97722.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/12 - Some Nights (Extended) [Explicit]_1419f0c6-e8d2-4021-8d12-f30bad0e38b8.mp3")
song1("../../../sorted_mp3s/All/12 - Some Nights (Extended) [Explicit]_1419f0c6-e8d2-4021-8d12-f30bad0e38b8.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/12 - VOODOO [Explicit]_966af0e8-9942-49cf-87aa-86496572a0ba.mp3")
song1("../../../sorted_mp3s/All/12 - VOODOO [Explicit]_966af0e8-9942-49cf-87aa-86496572a0ba.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - After Hours_2d53df15-ea6d-4cf5-bf1f-4a4333a62b89.mp3")
song1("../../../sorted_mp3s/All/13 - After Hours_2d53df15-ea6d-4cf5-bf1f-4a4333a62b89.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - Ain't That Kind Of Friend_3b87f968-98de-41e4-bf79-2b6b1c508f05.mp3")
song1("../../../sorted_mp3s/All/13 - Ain't That Kind Of Friend_3b87f968-98de-41e4-bf79-2b6b1c508f05.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - Fade Away_fd85df0b-91a9-43ae-9709-752c12b8f3c2.mp3")
song1("../../../sorted_mp3s/All/13 - Fade Away_fd85df0b-91a9-43ae-9709-752c12b8f3c2.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - Freestyle [Explicit]_70419102-2f37-458a-904b-05b9ebbb436f.mp3")
song1("../../../sorted_mp3s/All/13 - Freestyle [Explicit]_70419102-2f37-458a-904b-05b9ebbb436f.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/13 - HOLY GHOST [Explicit]_f1101367-ef47-46e0-b315-8116085d77d2.mp3")
song1("../../../sorted_mp3s/All/13 - HOLY GHOST [Explicit]_f1101367-ef47-46e0-b315-8116085d77d2.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - High School Reunion [Explicit]_96baf95e-8c03-4927-b8bd-fbfa1ffa2b05.mp3")
song1("../../../sorted_mp3s/All/13 - High School Reunion [Explicit]_96baf95e-8c03-4927-b8bd-fbfa1ffa2b05.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - Jodye [Explicit]_47a18b52-ccf6-4dc1-a54b-84af8340488d.mp3")
song1("../../../sorted_mp3s/All/13 - Jodye [Explicit]_47a18b52-ccf6-4dc1-a54b-84af8340488d.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - Let You Go_f23a4992-e985-40ae-bb42-e05b064b04f0.mp3")
song1("../../../sorted_mp3s/All/13 - Let You Go_f23a4992-e985-40ae-bb42-e05b064b04f0.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - Let's Go (Radio Edit)_38e33549-da75-46e8-bbe9-3d37f3ec2fd1.mp3")
song1("../../../sorted_mp3s/All/13 - Let's Go (Radio Edit)_38e33549-da75-46e8-bbe9-3d37f3ec2fd1.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/13 - Poppin' Tags [Explicit]_34f38fb8-b426-4916-a72d-cd1f9d83db94.mp3")
song1("../../../sorted_mp3s/All/13 - Poppin' Tags [Explicit]_34f38fb8-b426-4916-a72d-cd1f9d83db94.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - Pray [feat. Kameron]_ff01cc0e-e561-4128-9154-035c3b945df1.mp3")
song1("../../../sorted_mp3s/All/13 - Pray [feat. Kameron]_ff01cc0e-e561-4128-9154-035c3b945df1.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - Seasons [Explicit]_a732953f-4045-4851-a757-63ee3da916b2.mp3")
song1("../../../sorted_mp3s/All/13 - Seasons [Explicit]_a732953f-4045-4851-a757-63ee3da916b2.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - Thing Called Love (Original Mix)_23b7492f-460c-4d8c-b399-bbaa7400a321.mp3")
song1("../../../sorted_mp3s/All/13 - Thing Called Love (Original Mix)_23b7492f-460c-4d8c-b399-bbaa7400a321.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/13 - Timber_81f0920a-56cd-4f02-92e4-173462aeebc6.mp3")
song1("../../../sorted_mp3s/All/13 - Timber_81f0920a-56cd-4f02-92e4-173462aeebc6.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/13 - Titanium (Feat. Sia)_2e6c54a6-70c2-4d9d-92d7-5b21056d7cba.mp3")
song1("../../../sorted_mp3s/All/13 - Titanium (Feat. Sia)_2e6c54a6-70c2-4d9d-92d7-5b21056d7cba.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/13 - Zatoichi [Explicit]_f7050fac-2742-4542-82fd-3e356fc2bf27.mp3")
song1("../../../sorted_mp3s/All/13 - Zatoichi [Explicit]_f7050fac-2742-4542-82fd-3e356fc2bf27.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/14 - Black Tux, White Collar [Explicit]_c03075c3-19f6-437e-9d90-e9b7ed0dfd42.mp3")
song1("../../../sorted_mp3s/All/14 - Black Tux, White Collar [Explicit]_c03075c3-19f6-437e-9d90-e9b7ed0dfd42.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/14 - Demons [Explicit]_7eba40b1-f111-457c-9753-30fb21e06731.mp3")
song1("../../../sorted_mp3s/All/14 - Demons [Explicit]_7eba40b1-f111-457c-9753-30fb21e06731.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/14 - Few Good Things (feat. Black Thought and Eryn Allen Kane) [Explicit]_84fa1f26-e14b-426f-b68e-70466a726429.mp3")
song1("../../../sorted_mp3s/All/14 - Few Good Things (feat. Black Thought and Eryn Allen Kane) [Explicit]_84fa1f26-e14b-426f-b68e-70466a726429.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/14 - Figaro [Explicit]_993ca32c-2de4-442c-9498-c33502540f8f.mp3")
song1("../../../sorted_mp3s/All/14 - Figaro [Explicit]_993ca32c-2de4-442c-9498-c33502540f8f.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/14 - Ghetto Symphony [Explicit]_17aa988c-1a74-453e-8004-7a6cf2e06e30.mp3")
song1("../../../sorted_mp3s/All/14 - Ghetto Symphony [Explicit]_17aa988c-1a74-453e-8004-7a6cf2e06e30.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/14 - Ghosts_60b580ee-734c-43f2-801a-0796b3b1f8a1.mp3")
song1("../../../sorted_mp3s/All/14 - Ghosts_60b580ee-734c-43f2-801a-0796b3b1f8a1.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/14 - Into Dust_d76c0966-5862-46f9-8683-c82ba9cc7cf5.mp3")
song1("../../../sorted_mp3s/All/14 - Into Dust_d76c0966-5862-46f9-8683-c82ba9cc7cf5.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/14 - One Way (Bonus) [feat. T-Pain] [Explicit]_df75cd89-f6ac-4ccb-ac4d-619586c81ab6.mp3")
song1("../../../sorted_mp3s/All/14 - One Way (Bonus) [feat. T-Pain] [Explicit]_df75cd89-f6ac-4ccb-ac4d-619586c81ab6.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/14 - Still With Me (Seven Lions Remix)_dfdcf0d3-63e0-4c9e-9920-3693eddabf75.mp3")
song1("../../../sorted_mp3s/All/14 - Still With Me (Seven Lions Remix)_dfdcf0d3-63e0-4c9e-9920-3693eddabf75.mp3").playlists = ['All', 'FutureBass_Chillstep', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/15 - Eternal (Original Mix)_0a4222b2-17b3-4b3e-ba3b-572ba530c4bf.mp3")
song1("../../../sorted_mp3s/All/15 - Eternal (Original Mix)_0a4222b2-17b3-4b3e-ba3b-572ba530c4bf.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/15 - Faith_1345a0de-9db1-4222-b1b6-8ed9e94fb67c.mp3")
song1("../../../sorted_mp3s/All/15 - Faith_1345a0de-9db1-4222-b1b6-8ed9e94fb67c.mp3").playlists = ['All', 'Deep_ChillHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/15 - Good4U [feat. Kota the Friend]_84278873-6843-4564-9bbb-3d6107fb6a52.mp3")
song1("../../../sorted_mp3s/All/15 - Good4U [feat. Kota the Friend]_84278873-6843-4564-9bbb-3d6107fb6a52.mp3").playlists = ['All', 'FutureBass_Chillstep']
load_song("../../../sorted_mp3s/All/15 - Gorgeous_79a5de69-5db4-48e9-872d-a6d685d2812e.mp3")
song1("../../../sorted_mp3s/All/15 - Gorgeous_79a5de69-5db4-48e9-872d-a6d685d2812e.mp3").playlists = ['All', 'Trap_Midtempo', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/15 - Hatred (feat. E11E) [Explicit]_d2bc566a-2e86-4ede-a772-a1e6698297a0.mp3")
song1("../../../sorted_mp3s/All/15 - Hatred (feat. E11E) [Explicit]_d2bc566a-2e86-4ede-a772-a1e6698297a0.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/15 - I Don't Deserve You (Seven Lions Radio Edit) [feat. Plumb]_35a324ca-7416-4ca8-acb7-495e9c2b0b3b.mp3")
song1("../../../sorted_mp3s/All/15 - I Don't Deserve You (Seven Lions Radio Edit) [feat. Plumb]_35a324ca-7416-4ca8-acb7-495e9c2b0b3b.mp3").playlists = ['All', 'Trance_ProgressiveHouse', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/15 - M'$ [Explicit]_b13c9d5f-e9e1-4a31-b4d1-7563bca98e89.mp3")
song1("../../../sorted_mp3s/All/15 - M'$ [Explicit]_b13c9d5f-e9e1-4a31-b4d1-7563bca98e89.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/15 - Muskox_44f7b9ee-67ed-43c4-8193-61f7b4cc66b0.mp3")
song1("../../../sorted_mp3s/All/15 - Muskox_44f7b9ee-67ed-43c4-8193-61f7b4cc66b0.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/15 - Sandman [Explicit]_942b8ae0-4b6d-4eb2-9c87-4e627c8f21ce.mp3")
song1("../../../sorted_mp3s/All/15 - Sandman [Explicit]_942b8ae0-4b6d-4eb2-9c87-4e627c8f21ce.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/15 - Young Forever [feat. Mr Hudson] [Explicit]_f2bdf537-b94a-463f-8f7d-f1b1c7b235bf.mp3")
song1("../../../sorted_mp3s/All/15 - Young Forever [feat. Mr Hudson] [Explicit]_f2bdf537-b94a-463f-8f7d-f1b1c7b235bf.mp3").playlists = ['All', 'Hits_Throwbacks']
load_song("../../../sorted_mp3s/All/16 - Desire_d0a655b3-fcd9-4960-9825-5a5f7225d445.mp3")
song1("../../../sorted_mp3s/All/16 - Desire_d0a655b3-fcd9-4960-9825-5a5f7225d445.mp3").playlists = ['All', 'Drum&Bass', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/16 - Dreams (Interlude) [Explicit]_16f21a62-c2ce-44e0-95cf-54fa6eb7de0a.mp3")
song1("../../../sorted_mp3s/All/16 - Dreams (Interlude) [Explicit]_16f21a62-c2ce-44e0-95cf-54fa6eb7de0a.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/16 - I Come Apart [Explicit]_7b4514a7-2b8a-453b-a2e3-94ca0726ada8.mp3")
song1("../../../sorted_mp3s/All/16 - I Come Apart [Explicit]_7b4514a7-2b8a-453b-a2e3-94ca0726ada8.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/16 - XO Tour Llif3 [Explicit]_f10b5389-45bc-4f21-bfc9-78d154f92473.mp3")
song1("../../../sorted_mp3s/All/16 - XO Tour Llif3 [Explicit]_f10b5389-45bc-4f21-bfc9-78d154f92473.mp3").playlists = ['All', 'Rap_R&B']
load_song("../../../sorted_mp3s/All/17 - Get Deaded (Moody Good Remix)_3566d8f5-b375-4d48-88d8-14dd33910026.mp3")
song1("../../../sorted_mp3s/All/17 - Get Deaded (Moody Good Remix)_3566d8f5-b375-4d48-88d8-14dd33910026.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/17 - Sunhammer_80d5bcdd-a932-4fc7-a285-5e51f1ccfde8.mp3")
song1("../../../sorted_mp3s/All/17 - Sunhammer_80d5bcdd-a932-4fc7-a285-5e51f1ccfde8.mp3").playlists = ['All', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/18 - F_ck Up Some Commas [Explicit]_41adf26f-dd87-4376-94bd-db0154876c95.mp3")
song1("../../../sorted_mp3s/All/18 - F_ck Up Some Commas [Explicit]_41adf26f-dd87-4376-94bd-db0154876c95.mp3").playlists = ['All', 'Rap_R&B', 'REDWAVE.']
load_song("../../../sorted_mp3s/All/24 - I'm Fine (feat. Cherry Lena) (IMANU Remix)_bf652e6c-3d97-4f0e-b8ac-3d86ce97b22b.mp3")
song1("../../../sorted_mp3s/All/24 - I'm Fine (feat. Cherry Lena) (IMANU Remix)_bf652e6c-3d97-4f0e-b8ac-3d86ce97b22b.mp3").playlists = ['All', 'Deep_ChillHouse']
load_song("../../../sorted_mp3s/All/30 - Hello [feat. A Boogie wit da Hoodie] [Explicit]_341d634e-8e8c-4695-b863-9bd20234fba9.mp3")
song1("../../../sorted_mp3s/All/30 - Hello [feat. A Boogie wit da Hoodie] [Explicit]_341d634e-8e8c-4695-b863-9bd20234fba9.mp3").playlists = ['All', 'Rap_R&B']
