# File Copier/Organizer/Searcher for DJs

    ## Description
     - This tool is meant to help DJs keep up with the organization of a large database of songs.
     - The organizer component loops through a folder of downloaded song files, checking all nested folders, and copies all files of a specified type into a single unorganized folder. Then, for each song, asks the user which folder(s) they would like it to, copies it into the specified folder(s), and deletes it from the unorganized folder.
     - The searcher component looks through a spreadsheet of songs, inputted by the user, and automatically opens an Amazon tab searching for each one.
    
    ## Predependencies
     - Python must be installed. If not, install here: https://www.python.org/downloads/macos/
    
    ## How to run
     1. Navigate to the directory of this project in your bash terminal.
     - Copier/Organizer
        1. Open songcopier.sh in a text editor. At the top of the file, there are a few variables open for your modification, with comments explaining which is which. Where directed, specify your username as it appears on your computer, the type of file you would like to copy, and your folders for new downloads, unorganized files, and organized files.
        2. Type **bash songcopier.sh**. If all specified folders exist, the script will run correctly.
     - Searcher
        1. Open "songs_to_search.csv" in Excel. Put the names of the songs you want to find in the first column, and the artists in the second. It does not have to be exact.
        2. Type **python3 songsearcher.py**. The program will open an Amazon tab containing a search for each song in the spreadsheet.

    ## Components
    _Comments explaining code are present in all listed components.
     ### songcopier.sh
        * Main shell script for copying songs; executes code extraced from songsorter.py as a part of execution.
     #### songsorter.py
        * Python script containing function prompting user for playlists to add each song to, saves output to .txt file
     ### songs_to_search.csv
        * Spreadsheet to fill in with names of songs and artists for searcher component.
     ### songsearcher.py
        * Python script which loops through songs_to_search.csv row-by-row and opens a browser tab containing an Amazon search for each one.
        
    ## License
     * GNU General Public License v3.0, Sam Hopkins, July 12, 2022. Updated Jan 16, 2023.
