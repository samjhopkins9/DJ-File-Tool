#!/bin/bash

filetype="mp3"

function check_files {
    for path in *; do
        filename="$path"
        if [[ -d $path ]]
        then
            cd "$path"
            check_files
            cd ..
        else
            check_file
        fi
    done
}

function check_file {
    if [ "${filename:(-3)}" = "$filetype" ]
    then
        cp "$filename" "/Users/samjhopkins9/Music/new_mp3s"
        rm "$filename"
    else
        arb=""
    fi
}

function if_e_py {
    if [[ -e temp.py ]]; then
        rm temp.py
        touch temp.py
    else
        touch temp.py
    fi
}

playlists=""
playlistsarr=()
function parse_playlists {
    loadingstring=""
    for (( c=0; c<${#playlists}; c++ )); do
        if [ "${playlists:c:1}" == "[" ] || [ "${playlists:c:1}" == "'" ]]; then
            arb=""
        elif [ "${playlists:c:1}" == "," ] || [ "${playlists:c:1}" == "]" ]; then
            playlistsarr+=( $loadingstring )
            loadingstring=""
        else
            loadingstring=""$loadingstring""${playlists:c:1}""
        fi
    done
}

basepython=$(<songsorter.py)
function run_python {
    if_e_py
    echo "$basepython" >> temp.py
    echo "sort_song(\"$f\")" >> temp.py
    echo "with open(\"playlists.txt\", \"w\") as plists:" >> temp.py
    echo "      plists.write(str(playlists))" >> temp.py
    echo "      plists.close()" >> temp.py
    echo ""
    python3 temp.py
    playlists=$(<playlists.txt)
    rm temp.py
    parse_playlists
}

function copy_file {
    run_python
    for p in "${playlistsarr[@]}"; do
        cp "$f" "~/Music/sorted_mp3s/"$p""
    done
    rm "$f"
}

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

cd "/Users/samjhopkins9/Music/Amazon Music"
check_files
cd "/Users/samjhopkins9/Music/new_mp3s"
sort_files


