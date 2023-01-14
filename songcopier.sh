#!/bin/bash

filetype="mp3"

function check_file(){
    if [ "${filename:(-3)}" = "$filetype" ]
    then
        cp "$filename" "~/Library/Mobile\ Documents/com~apple~CloudDocs/ZBT DJ Song Pool/Unsorted"
        rm -r "$filename"
    else
        arb=""
    fi
}

function check_files(){
    for path in *; do
        filename="$path"
        check_file
        if [[ -d $path ]]
        then
            cd "$path"
            check_files
            cd ..
        else
            arb=""
        fi
    done
}

function sort_files(){
    for f in *
    do
        if [[ -e temp.py ]]; then
            rm temp.py
            touch temp.py
        else
            touch temp.py
        fi
        cat "~/Library/Mobile\ Documents/com~apple~CloudDocs/ZBT DJ Song Pool/DJ File Tool/songsorter.py" >> temp.py
        if [ "${f:(-3)}" = "$filetype" ]
        then
            echo "load_song(\"$f\")" >> temp.py
            echo "sort_song(song1(\"$f\"))" >> temp.py
            echo "with open(\"playlists.txt\", \"w\") as plists:" >> temp.py
            echo "      plists.write(str(playlists))" >> temp.py
            echo "      plists.close()" >> temp.py
            echo ""
        else
            arb=""
        fi
        python3 temp.py
        playlists=`cat playlists.txt`
        playlistsarr=()
        loadingstring=""
        for (( c=0; c<${#playlists}; c++ ))
        do
            if [ "${playlists:c:1}" == "[" ] || [ "${playlists:c:1}" == "'" ] ||  [ "${playlists:c:1}" == "," ]; then
                arb=""
            elif [ "${playlists:(c-1):1}" == "," ] || [ "${playlists:c:1}" == "]" ]; then
                playlistsarr+=( $loadingstring )
                loadingstring=""
            else
                loadingstring="$loadingstring"""${playlists:c:1}""
            fi
        done
        for i in "${playlistsarr[@]}"; do
            cp "$f" "~/Library/Mobile\ Documents/com~apple~CloudDocs/ZBT DJ Song Pool/"$i""
        done
        rm "$f"
    done
}

# Changes to downloads folder, copies all mp3s in all directories
cd ~/Downloads
check_files

# Changes to Amazon Music folder, copies all mp3s in all directories
cd ~/Music/"Amazon Music"
check_files

# Changes to ZBT DJ Song Pool folder within Shared directory in iCloud folder
cd "~/Library/Mobile\ Documents/com~apple~CloudDocs/Shared/ZBT DJ Song Pool/Unsorted"
sort_files


