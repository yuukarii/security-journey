# Android phone

## Uninstall an application
```bash
adb devices
adb shell
pm list packages
pm list packages | grep 'google'
pm uninstall -k --user 0 package-name

pm uninstall --user 0 com.android.vending
cmd package install-existing com.android.vending
```
Use this [website](https://play.google.com/store/games) to search the package-name for verifying.