#!/bin/bash



# Username variable stores the name of your directory within the Users directory
username="samjhopkins9"
# Filetype variable declares which kind of file will be copied
filetype="mp3"
# All folders whose names are stored in the three below variables are assumed to exist
download_folder="/Users/"$username"/Music/Amazon Music" # Folder which the program will search for files
unsorted_folder="/Users/"$username"/Music/new_"$filetype"s" # Folder which the program will copy files into from download folder
sorted_folder="/Users/"$username"/Music/sorted_"$filetype"s" # Folder which the program will organize songs into, expecting folders corresponding with each of the playlist names in the program to exist within the folder. Playlist names are contained in "songsorter.py".



# Function loops through all files and directories within a folder and moves files of the specified type to a new folder within the Music directory
function check_files {
    for path in *; do
        if [[ -d $path ]]; then
            # If an item within the folder is a directory, the function is called recursively within it so that all nested directories are checked
            cd "$path"
            check_files
            cd ..
        else
            # If the extension of the filename match with the filetype, moves it to an unorganized folder within the Music directory
            if [ "${path:(-3)}" = "$filetype" ]; then
                cp "$path" $unsorted_folder
                rm "$path"
            else
                arb="" # Arbitrary; exists because bash only allows "if-else" statements
            fi
        fi
    done
}


# Function checks if a python script called temp.py exists; if it does, it replaces it with an empty copy, and if it doesn't, it creates a new version.
function if_e_py {
    if [[ -e temp.py ]]; then
        rm temp.py
        touch temp.py
    else
        touch temp.py
    fi
}

# playlists variable contains the direct output of the whole array containing the playlists for a song file from the python scipt
playlists=""
# playlistsarr is a bash array containing the same items
playlistsarr=()
# Function loops through playlists string for a song, character by character, to separate the substrings into an array of playlist names
function parse_playlists {
    # String to load characters onto incrimentally for each playlist name in the list
    loadingstring=""
    for (( c=0; c<${#playlists}; c++ )); do
        # Skips opening brackets and quotes within lists; these do not need to be within the strings in the bash array
        if [ "${playlists:c:1}" == "[" ] || [ "${playlists:c:1}" == "'" ]]; then
            arb=""
        # On commas and closing brackets, where a full playlist name has been read in, it adds the string to the array, and resets it to empty
        elif [ "${playlists:c:1}" == "," ] || [ "${playlists:c:1}" == "]" ]; then
            playlistsarr+=( $loadingstring )
            loadingstring=""
        # On all other characters, it appends the current character to the characters already in the string
        else
            loadingstring=""$loadingstring""${playlists:c:1}""
        fi
    done
}

# basepython variable saves the contents of "songsorter.py" while still in project directory so that code is always copied into script, and can be accessed from any directory
basepython=$(<songsorter.py)
# Function creates a temporary python script, appends code to it with a filename as an input, runs it, then deletes the temporary files involved in the process.
function run_python {
    # Calls function creating a blank version of temp.py
    if_e_py
    # Appends contents of "songsorter.py" to temp.py, which contains the empty array and the "sort_songs" function
    echo "$basepython" >> temp.py
    # Appends code to tempy.py calling the "sort_song" function with a specified filename, asking the user which playlists they would like to add it to.
    echo "sort_song(\"$f\")" >> temp.py
    # Appends code which creates a file called "playlists.txt" and writes the whole array of playlists to it as a string.
    echo "with open(\"playlists.txt\", \"w\") as plists:" >> temp.py
    echo "      plists.write(str(playlists))" >> temp.py
    echo "      plists.close()" >> temp.py
    echo ""
    # Runs temporary python script after all above code is written into it
    python3 temp.py
    # Saves contents of playlists.txt to the playlists variable
    playlists=$(<playlists.txt)
    # Deletes temp.py and playlists.txt
    rm temp.py
    rm playlists.txt
}

# Function runs temp.py on a file to ask user for playlists, parses the contents of playlists.txt into a bash array, copies the file into the folder corresponding to each of the playlists by looping through the array in bash, then removes the file from its original directory.
function copy_file {
    run_python
    parse_playlists
    for p in "${playlistsarr[@]}"; do
        cp "$f" "~/Music/sorted_mp3s/"$p""
    done
    rm "$f"
}

# Function loops through all files within unorganized directory, checks if they are the appropriate filetype, and if so, runs the above code for copying the file into organized folders
function sort_files {
    for f in *
    do
        if [ "${f:(-3)}" = "$filetype" ]; then
            copy_file
        else
            arb=""
        fi
    done
}

# Runs function to find and copy all mp3s from the download folder into the new_"filetype"s folder within the Music directory.
cd "$download_folder"
check_files
# Runs function to copy all new files from unorganized folder into organized folders
cd "$unsorted_folder"
sort_files


