#!/bin/bash
if [ -f conf/local.conf ]; then
    cat >> conf/local.conf << EOF
# oe default vars
YOCTO_CACHE="/home/savent/buildsys/yocto-cache"
SSTATE_DIR="${YOCTO_CACHE}/sstate"
DL_DIR="${YOCTO_CACHE}/dl"
EOF
else
    echo "Can't find `pwd`/conf/local.conf!"
fi
