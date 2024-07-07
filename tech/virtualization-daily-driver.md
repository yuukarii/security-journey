# Virtualization use for daily use

## Windows 11 in qemu/kvm
How to configure Windows 11 VM
- CPUs: 
	- Choose host-passthrough
	- Manually set CPU topology: 1 sockets (Windows cannot regconize many sockets) 8 cores 1 threads
- Display:
	- Choose Spice server
	- Listen type: None
	- Tick OpenGL
- Video: Virtio. tick 3D acceleration.

On Windows guest:
1. On the Windows 11 Guest, install this latest Spice-Guest-Tools from [https://www.spice-space.org/download/windows/spice-guest-tools/spice-guest-tools-latest.exe](https://www.spice-space.org/download/windows/spice-guest-tools/spice-guest-tools-latest.exe)
2. On the Windows 11 Guest, install this latest Virtio-Win-Guest-Tools from [https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/latest-virtio/virtio-win-guest-tools.exe](https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/latest-virtio/virtio-win-guest-tools.exe)

## VMWARE on WINDOWS 11 HOST
Run `msinfo32.exe` and check `Virtualization-based security`, it should be *Not enable*.
If not, do this: [Disable Hyper-V to run virtualization software - Windows Client | Microsoft Learn](https://learn.microsoft.com/en-us/troubleshoot/windows-client/application-management/virtualization-apps-not-work-with-hyper-v)

[i3wm-arch](i3wm-arch.md)

