# Debian/Ubuntu

## Key-takeaways
```bash
# install a package
apt install <package>

# Reinstall a package
apt reinstall <package>

# Reinstall a package and all dependencies
apt reinstall <package> $(apt-cache depends --recurse --installed <package> ||grep '[ ]')

# Removing a package
apt remove <package>

# Removing a package and all its configuration, data files
apt purge <package>

# Upgrade a package
apt upgrade <package>

# Keep system up-to-date
apt update
apt upgrade

# Search for packages
apt search <string>
apt search <string> | less

# Search only by name
dpkg-query -l '*<string>*'

# Or check in the following directories
/var/lib/apt/lists/*
/var/lib/dpkg/available
/var/lib/dpkg/status

# List installed packages
dpkg --list


```