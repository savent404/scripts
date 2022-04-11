#!/bin/bash

# |       uboot     |     dtb    |       kernel        |
# | 0----------2.5M | 2.5M----3M | 3M--------------15M |

# usage: flash-package.sh uboot dtb kernel
#  output to 'img'


uboot_size=`stat -c%s $1`
dtb_size=`stat -c%s $2`
kernel_size=`stat -c%s $3`

dtb_head=2621440
kernel_head=3145728
kernel_full=12582912

pad1=`expr $dtb_head - $uboot_size`
pad2=`expr $kernel_head - $dtb_head - $dtb_size`
pad3=`expr $kernel_full - $kernel_size`

dd if=/dev/zero of=./pad1 bs=1 count=$pad1
dd if=/dev/zero of=./pad2 bs=1 count=$pad2
dd if=/dev/zero of=./pad3 bs=1 count=$pad3

cat $1 pad1 $2 pad2 $3 pad3 > img

rm pad1 pad2 pad3
