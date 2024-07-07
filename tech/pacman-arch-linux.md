# Arch Linux Pacman configuration

## Configuration
/etc/pacman.conf
```bash
# Misc options
#UseSyslog
Color
#NoProgressBar
CheckSpace
#VerbosePkgLists
ParallelDownloads = 5
ILoveCandy
```

## Commands
```bash
# List all packages
sudo pacman -Q

# List packages that are not installed by pacman (AUR for example)
sudo pacman -Qm

# Uninstall a packages
sudo pacman -Rcns <package>

```

## Slow download rate with pacman
```bash
sudo pacman -S reflector
cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bkp
sudo reflector --country 'Vietnam' --latest 5 --age 2 --fastest 5 --protocol https --sort rate --save /etc/pacman.d/mirrorlist

sudo vim /etc/pacman.conf
# Uncomment this line
#MaxParallelDownloads = 5
```
