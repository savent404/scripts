#!/bin/bash

if [ $# -ne 2 ]; then
    echo "$0 usage: $0 kernel-dir arch"
fi

LNX=$(realpath $1)
ARCH=$2

echo "generating cscope list..."
find $LNX/arch/$ARCH -name "*.[chxSs]" -print > ./cscope.files
find $LNX \
    -path "$LNX/arch/*" -prune -o \
    -path "$LNX/tmp*" -prune -o \
    -path "$LNX/Documentation*" -prune -o \
    -path "$LNX/scripts*" -prune -o \
    -path "$LNX/tools*" -prune -o \
    -path "$LNX/.git*" -prune -o \
    -name "*.[chxsS]" -print >> ./cscope.files

echo "generating cscope tags..."
cscope -bqk
