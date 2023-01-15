#!/bin/bash
filetype="mp3"
basepython=$(<songsorter.py)

function check_file(){
    if [ "${filename:(-3)}" = "$filetype" ]
    then
        cp "$filename" ""
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
        if [ "${f:(-3)}" = "$filetype" ]
        then
            if [[ -e temp.py ]]; then
                rm temp.py
                touch temp.py
            else
                touch temp.py
            fi
            echo "$basepython" >> temp.py
            echo "sort_song(\"$f\")" >> temp.py
            echo "with open(\"playlists.txt\", \"w\") as plists:" >> temp.py
            echo "      plists.write(str(playlists))" >> temp.py
            echo "      plists.close()" >> temp.py
            echo ""
            python3 temp.py
            playlists=$(<playlists.txt)
            loadingstring=""
            for (( c=0; c<${#playlists}; c++ )); do
                if [ "${playlists:c:1}" == "[" ] || [ "${playlists:c:1}" == "'" ] ||  [ "${playlists:c:1}" == "," ]; then
                    arb=""
                elif [ "${playlists:(c-1):1}" == "," ] || [ "${playlists:c:1}" == "]" ]; then
                    loadingstring=""
                else
                    loadingstring=""$loadingstring""${playlists:c:1}""
                fi
            done
            for i in "${playlistsarr[@]}"; do
                cp "$f" "~/Music/sorted_mp3s/"$i""
            done
            rm "$f"
            if [[ -e temp.py ]]; then
                rm temp.py
                touch temp.py
            else
                touch temp.py
            fi
        else
            arb=""
        fi
    done
}

cd "~/Music/Amazon Music"
check_files
cd "~/Music/new_mp3s"
sort_files


