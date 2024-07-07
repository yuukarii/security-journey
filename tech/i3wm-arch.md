# Install I3wm on arch linux

[GitHub - Keyitdev/dotfiles: My personal build of dotfiles using i3.](https://github.com/Keyitdev/dotfiles/tree/v3)
Thấy cái này khá ngon lành.

Cài theo thôi nào.
Trước tiên gỡ hyprland đã -> DONE

```bash
git clone -b v3 --depth 1 https://www.github.com/keyitdev/dotfiles.git

# Install dependencies
yay -S --needed acpi alsa-utils base-devel curl git xorg xorg-xinit alacritty btop code dunst feh ffcast firefox i3-gaps i3lock-color i3-resurrect libnotify light mpc mpd ncmpcpp nemo neofetch pacman-contrib papirus-icon-theme picom polybar ranger rofi scrot slop xclip zathura zathura-pdf-mupdf zsh
# skip pulseaudio pulseaudio-alsa oh-my-zsh-git

mkdir -p "$HOME"/Pictures/wallpapers

cp -r ./config/* "$HOME"/.config
sudo cp -r ./scripts/* /usr/local/bin
sudo cp -r ./fonts/* /usr/share/fonts
cp -r ./wallpapers/* "$HOME"/Pictures/wallpapers

# Make Light executable, set zsh as default shell, update nvim extensions, refresh font cache.
sudo chmod +s /usr/bin/light
chsh -s /bin/zsh
sudo chsh -s /bin/zsh
fc-cache -fv

# Install gtk theme.
mkdir -p "$HOME"/.config/gtk-4.0
git clone https://github.com/Fausto-Korpsvart/Rose-Pine-GTK-Theme
sudo cp -r ./Rose-Pine-GTK-Theme/themes/RosePine-Main-BL  /usr/share/themes/RosePine-Main
sudo cp -r ./Rose-Pine-GTK-Theme/themes/RosePine-Main-BL/gtk-4.0/* "$HOME"/.config/gtk-4.0

# Install sddm and sddm flower theme.
yay -S --needed qt5-graphicaleffects qt5-quickcontrols2 qt5-svg sddm
sudo git clone https://github.com/keyitdev/sddm-flower-theme.git /usr/share/sddm/themes/sddm-flower-theme
sudo cp /usr/share/sddm/themes/sddm-flower-theme/Fonts/* /usr/share/fonts/
echo "[Theme]
Current=sddm-flower-theme" | sudo tee /etc/sddm.conf
```

Start i3 bằng command: `startx /usr/bin/i3`
First look:
![](Pasted%20image%2020240610082452.png)
Sẽ có nhiều thứ cần chỉnh sửa.
Lúc khác làm tiếp.


## Configure shared folder

The `open-vm-tools` have already installed on Arch.

Check this guide: https://wiki.archlinux.org/title/VMware/Install_Arch_Linux_as_a_guest in section 6.1.
Use systemd for auto-mounting.


## Install some stuffs
```bash
# Programming
code
code-features
code-marketplace


```

Configure zsh following [zsh-configuration](zsh-configuration.md).
Execute `alacritty migrate` to convert yml configuration to toml configuration.

My github repo: https://github.com/yuukarii/vm-dotfiles

## Config shared clipboard

install for Xorg configuration

**Note:** To use Xorg in a Virtual Machine, a minimum of 32MB VGA memory is needed.

Install the dependencies: [xf86-input-vmmouse](https://archlinux.org/packages/?name=xf86-input-vmmouse), [xf86-video-vmware](https://archlinux.org/packages/?name=xf86-video-vmware), and [mesa](https://archlinux.org/packages/?name=mesa).

For clipboard:
The drag-and-drop (copy/paste) feature requires both [open-vm-tools](https://archlinux.org/packages/?name=open-vm-tools) and [gtkmm3](https://archlinux.org/packages/?name=gtkmm3) packages to be installed.

```bash
cp /etc/X11/xinit/xinitrc ~/.xinitrc
```

Add `vmware-user &` to `~/.xinitrc`.


## Create a new Arch OS
Follow this instructions to create VM: [GitHub - kernkraft235/vmw17-arch-guest: Tips and Tweaks for creating a high performance Arch linux VM using VMware Workstation 17 on Windows 11](https://github.com/kernkraft235/vmw17-arch-guest?tab=readme-ov-file)

