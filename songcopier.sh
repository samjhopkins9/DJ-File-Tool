#!/bin/bash

filetype="mp3"

function check_file(){
    if [ "${filename:(-3)}" = "$filetype" ]
    then
        cp "$filename" ~/new_"$filetype"s
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
        cat "../Documents/Programming/DJ Tools/songcatalogskeleton.py" >> temp.py
        if [ "${f:(-3)}" = "$filetype" ]
        then
            echo "load_song(\"$f\")" >> temp.py
            echo "sort_song(song1(\"$f\"))" >> temp.py
            echo "with open(\"playlists.txt\", \"w\") as plists:" >> temp.py
            echo "      pliststring = str(song1(\"$f\").playlists)" >> temp.py
            echo "      plists.write(pliststring)" >> temp.py
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
        echo "load_song(\"../../../sorted_mp3s/All/$f\")" >> "../Documents/Programming/DJ Tools/songcatalog.py"
        echo "song1(\"../../../sorted_mp3s/All/$f\").playlists = $playlists" >> "../Documents/Programming/DJ Tools/songcatalog.py"
        for i in "${playlistsarr[@]}"; do
            cp "$f" "../sorted_mp3s/"$i""
        done
        rm "$f"
    done
}

cd ../../..
cd Music
cd "Amazon Music"
check_files
cd ~/new_"$filetype"s
sort_files


