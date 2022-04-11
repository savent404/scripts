setenv bootargs console=ttyS0,115200 earlyprintk=uart8250-32bit,0x28001000
ext4load scsi 5:1 0x90000000 /ft1500a-dsk-v2.dts
ext4load scsi 5:1 0x90100000 /uImage
eq close c0;eq close c1;eq close c4;eq close c5;pci enum;bootm 0x90100000 0x95000000:0x1000000 0x90000000


external

vmlinuz-0-rescue-db0a874aef34454f8c0c4d327f8afc7b
initramfs-0-rescue-db0a874aef34454f8c0c4d327f8afc7b.img
dtb-4.4.13-1.el7.aarch64/ft1500a-v2-dsk-v2.dtb
