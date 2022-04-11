#!/bin/bash
#
# usage: source ./proxy.sh http://localhost:8080
#

TMP_FILE='/tmp/tmp-proxy'

function setup_normal {
    cat << EOF > $TMP_FILE
export http_proxy="$1"
export https_proxy="$1"
export ftp_proxy="$1"
export ALL_PROXY="$1"
export all_proxy="$1"
EOF
    source $TMP_FILE
    rm $TMP_FILE
}


function setup_wget {
    if [ -z $1 ]; then
        rm ~/.wgetrc
    else
        cat << EOF > ~/.wgetrc
https_proxy = $1
http_proxy = $1
ftp_proxy = $1
use_proxy = on
EOF
    fi
}

function setup_git {
    if [ -z $1 ]; then
        git config --global --unset http.proxy
        git config --global --unset https.proxy
    else
        git config --global http.proxy $1
        git config --global https.proxy $1
    fi
}



if [ -z $1 ]; then
    echo "unexport"
else
    echo "setup proxy $1..."
fi
setup_normal $1
setup_git $1
setup_wget $1

