sudo qemu-system-arm \
    -kernel $1 \
    -dtb $2 \
    -s \
    -S \
    -initrd $3 \
    -M vexpress-a9 \
    -m 800 \
    -nographic \
    -append " root=/dev/mmcblk0 rw,i_version console=ttyAMA0,115200 earlycon=pl011 \
        ima_appraise=log ima_policy=tcb ima_policy=appraise_tcb rootflags=i_version" \
    -smp 2
    #-net tap,ifname=tap1,script=no,downscript=no  \
    # -sd $3 \
    # -net nic,vlan=0 \
