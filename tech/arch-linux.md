# Arch Linux

## Installation
- Use `Arch Linux` + `KDE` + `Brave Browser` + `Alacritty`.
- `Brave` cannot play sound. Try `floorp`

### Some necessary packages in Arch Linux
Check [pacman-arch-linux](pacman-arch-linux.md):

```bash
# Install yay from AUR
pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

# graphics
mesa
mesa-utils
libva-mesa-driver # for HP Elitebook G9

# Login management
sddm
sddm-kcm # For KDE

# Multimedia
ffmpeg
pipewire
pipewire-alsa
pipewire-audio
pipewire-pulse
pipewire-jack
wireplumber
gst-plugin-pipewire
pavucontrol

# Bluetooth
bluez-obex

# Programming
code
code-features
code-marketplace

# CLI Tools
starship

# Power management
auto-cpufreq # Install from source

# Widget KDE
# Thermal Monitor from olib

###################
# FOR HYPRLAND
###################

hyprland
alacritty
```

## Fix some issues
### Bluetooth issues
- Issue can't connect:
Uncomment the `Experimental = true` line in the configuration:
```
sudo vim /etc/bluetooth/main.conf
#Enables D-Bus experimental interfaces
# Possible values: true or false
Experimental = true

# Then restart the bluetooth.service:

sudo systemctl enable --now bluetooth.service
```

- Issue Microphone doesn't work:
After install all the necessary packages in [Arch Linux](arch-linux.md), it should change automatically from A2DP (SBC) to HSP/HFP (mSBC). If not, you should change it manually to use your microphone.


[install i3wm](i3wm-arch.md)