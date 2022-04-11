if [ -z $rootfs_part ]; then
    rootfs_part=/dev/mmcblk0p3
fi

trail_mnt="/trail_mnt"
mkdir $trail_mnt
mount $rootfs_part $trail_mnt

# mount securityfs
if [ -z `df -h | grep securityfs` ]; then
    mount -t securityfs /sys/kernel/security securityfs
fi
if [ -f $trail_mnt/etc/keys/ima_extra_policy ]; then
    echo $trail_mnt/etc/keys/ima_extra_policy > /sys/kernel/security/ima/policy
else
    echo "warning: not fount /etc/keys/ima_extra_policy in rootfs"
fi

umount $trail_mnt
rm -rf $trail_mnt
