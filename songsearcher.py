#!/usr/bin/python3
import csv
import webbrowser as web

# Opens "songs_to_search.csv",
with open("songs_to_search.csv") as file:
    # Loops through all lines in file
    for line in csv.reader(file):
    # Opens a web browser tab containing a link to an Amazon Search using the first cell in the row as the title of the song, and the second cell as the artist.
        web.open("https://www.amazon.com/s?k={a1}+{t1}&i=digital-music&crid=J8V6U287ZTGH&sprefix={a1}+{t1}%2Cdigital-music%2C83&ref=nb_sb_noss_1".format(t1=line[0], a1=line[1]))
    # Assumes that the only text contained within the .csv file is the titles of the songs in the first column and the artists in the second.
