#!/usr/bin/python3

import csv
import webbrowser as web

with open("songs_to_search.csv") as file2:
    for line in csv.reader(file2):
        web.open("https://www.amazon.com/s?k={a1}+{t1}&i=digital-music&crid=J8V6U287ZTGH&sprefix={a1}+{t1}%2Cdigital-music%2C83&ref=nb_sb_noss_1".format(t1=line[0], a1=line[1]))
