# Sync and Backup data

Nhu cầu của mình:
- Sync các file cần thiết giữa điện thoại và laptop (Windows/LinuxLinux)
- Backup dữ liệu vào hard disk.

## Linux
### Sync between smartphone and laptop
- Smartphone mình là android device.
- Laptop dùng Linux.
- Sử dụng `adb` để sync mà không cần cài thêm application chạy ngầm vì nhu cầu của mình là sync manually. `adb` cũng support wireless transfer.
- `adb` trên smartphone thấy đủ chức năng rồi.
- Trên Arch linux laptop thì install như sau (tham khảo [ADB on Arch Linux wiki](https://wiki.archlinux.org/title/Android_Debug_Bridge)): 
	- `pacman -Syu android-tools android-udev`
- Để sync file thì cần thêm 1 cái tool nữa là [better-adb-sync](https://github.com/jb2170/better-adb-sync)
- Lần đầu connect cần pair 2 thiết bị trước:
	- `adb devices`
	- `adb pair <ip>:<port>`
	- `adb connect <ip>:<port>`
- Sử dụng `better-adb-sync` để sync file:
```bash
adbsync --del --exclude tech-vault/.obsidian \
	--exclude life-vault/.obsidian push \
	/home/yuukarii/SharedData/1-pkm/ \
	/storage/emulated/0/SharingWithLaptop/PKM

adbsync pull \
	/storage/emulated/0/SharingWithLaptop/Keepass/dnomadvn.kdbx \
	/home/yuukarii/SharedData/7-sharing-with-phone/Keepass/dnomadvn.kdbx
```

Những media dir từ điện thoại cần sync qua laptop:
```
/storage/emulated/0/DCIM/Camera
/storage/emulated/0/Pictures/Screenshots
/storage/emulated/0/Pictures/Zalo
/storage/emulated/0/Pictures
/storage/emulated/0/Movies/Zalo
```

Script to automatically detect port on Android:
```bash
#!/usr/bin/bash

function sync_data () {
	echo "START SYNCING KEEPASS"
	adbsync pull \
		/storage/emulated/0/SharingWithLaptop/Keepass/dnomadvn.kdbx \
		/home/yuukarii/SharedData/7-sharing-with-phone/Keepass/dnomadvn.kdbx
	echo "START SYNCING OBSIDIAN"
	adbsync --del --exclude .obsidian \
		push \
		/home/yuukarii/SharedData/1-pkm/ /storage/emulated/0/SharingWithLaptop/PKM
	echo "START SYNCING IMAGES AND VIDEO"
	adbsync --del pull /storage/emulated/0/DCIM/Camera/ \
		/home/yuukarii/SharedData/3-media/3.1-pictures/3.1.3-camera/
	adbsync --del pull /storage/emulated/0/Pictures/ \
		/home/yuukarii/SharedData/3-media/3.1-pictures/3.1.5-pictures/
	adbsync --del pull /storage/emulated/0/Movies/ \
		/home/yuukarii/SharedData/3-media/3.1-pictures/3.1.4-movies/
}
adb get-state
if [ $? -eq 0 ]; then
	echo "DEVICE CONNECTED"
	sync_data

else
	echo DEVICE NOT CONNECTED
	IP_ADDRESS=$1
	PORT=$(nmap -p35000-65535 $IP_ADDRESS | grep open | cut -d '/' -f 1)
	if [[ -z "$PORT" ]]; then
		echo "CANNOT GRAB PORT"
	else
		adb connect $IP_ADDRESS:$PORT
		sync_data
	fi
fi
```
### Backup data from laptop to external hard disk
Trên Linux có thể dùng `rsync` command.

`rsync` is a utility for transferring and synchronizing files between a computer and a storage drive and across networked computers by comparing the modification times and sizes of files.

Command:
```bash
rsync -av --delete /path/to/backup /location/of/backup
rsync -av --delete /home/yuukarii/SharedData/ \
	/run/media/yuukarii/Sleepwalker/Data/
```

## Windows
Sync between laptop and external driver: use FreeFileSync app.
Sync between laptop and smartphone: finding the appropriate tool.