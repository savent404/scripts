dmesg -n 4
insmod /test/*.ko
mount -t devtmpfs devtmpfs /dev
mdev -s

/usr/lib/qt/examples/gui/analogclock/analogclock
