In the i3 config change "password" for your sudo password


Any programs you don't have installed you can delete that line or change your bindsym


Picom version is from ibhagwan @ https://github.com/ibhagwan/picom-ibhagwan-git


Animated background from https://github.com/sdaveas/i3-animated-background, but i don't use the gif converter, instead I download a video as a png sequence and put the pngs in the directory manually, allowing a much better image quality, also changed script from --bg-center to --bg-fill


packet-tracer installed with https://github.com/mpotane/void-packettracer you can merelly change the .deb package name in the script to packettracer.deb, rename you .deb packages to same name and it will install, I'm using version 8.2


rofi-themes from https://github.com/adi1090x/rofi


Conky color python script for wttr.in from 	url = https://gist.github.com/tronje/21c4c1ecf7a9afb133f1814336ac3d48


For Unimatrix 
  
  sudo curl -L https://raw.githubusercontent.com/will8211/unimatrix/master/unimatrix.py -o /usr/local/bin/unimatrix
  
  sudo chmod a+rx /usr/local/bin/unimatrix

for lxappearance:

  cursors: sudo xbps-install brezze-cursors

  theme: sudo xbps-install adwaita-plus

  icons: sudo xbps-install gnome-themes-extra
  
 -------------------------------------------

AMD nVidia configuration process for LENOVO IDEAPAD GAMING 3 15ACH6

I'm posting this here for future reference and for others to see, since nowadays we see more and more laptops come with Ryzens pared with nVidia GPUs, with switchable/shared graphics I want to share this, anyone is welcome to improve this post, I also take the opportunity to kindly ask that if anyone from void team sees this post to add a more complete section to the docs for future reference and new users!

PLEASE FORGIVE ME ANY MISTAKES, I'm just trying to help, I started using linux at around 9 months ago I'M STILL A NOOB, I'm just trying to help some noob like me that could be wasting 3 days of his life trying to find this info.

THIS WORKED FOR ME, ITS NOT GUARANTEED IT WILL WORK FOR YOU, if anyone with more experience wants to help "standardize" this process I would be most grateful.

IF AFTER A REBOOT YOUR PC GETS ALL BLACK DON'T PANIC, just press cntrl+alt+f4 and delete or rename via console /etc/lightdm/display_setup.sh. If you cant access tty with cntrl+alt+f4 enter recovery mode in grub and delete the file.

YOU SHOULD ALSO BACKUP your ../xorg.conf.d/ folder be it where it is, to achieve that just do:

sudo cp -R /usr/share/X11/xorg.conf.d/ /usr/share/X11/xorg.conf.d.bk/

or depending on where it is

sudo cp -R /etc/X11/xorg.conf.d/ /etc/X11/xorg.conf.d.bk/

--------------------------------------------------------------------------------

My laptop is a LENOVO IDEAPAD GAMING 3 15ACH6 with a Ryzen 5 5600H and an nVidia RTX 3050

So to put my nVidia rtx up and running and being the main gpu I followed the steps in this link: https://wiki.archlinux.org/title/NVIDIA_Optimus#Use_NVIDIA_graphics_only

EDIT: Don't install nouveau, if you did you can blacklist it editing/creating /etc/modprobe.d/blacklist.conf:

sudo vim /etc/modprobe.d/blacklist.conf

and the add the following line :

blacklist nouveau

I checked first nvtop to see which gpu was working, and there was the amd cpu showing activity and the nVidia gpu stood quiet.

Then I followed the bellow steps:

Follow the steps in the void manual: https://docs.voidlinux.org/config/graphical-session/graphics-drivers/index.html according to your hardware, from previous experience this steps also most likely work with intel cpus. I followed both for nVidia and amd.

then edit /etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf

if you don't have this folder and this file it will almost surely be in /usr/share/X11/xorg.conf.d/*, just edit the file there and then copy it to etc:

in my case i didn't have /etc/X11/xorg.conf.d/ so I proceeded like this:

EDIT: if you have a file named /etc/X11/xorg.conf back it up and delete it: (or just move it to another name as bellow)

sudo mv /etc/X11/xorg.conf /etc/X11/xorg.conf.bk

(i use vim you can use nano or touch and then edit it or make the file on the file manager)

sudo vim /usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf

and then delete everything and paste this:

Section "OutputClass"
    Identifier "intel"
    MatchDriver "i915"
    Driver "modesetting"
EndSection

Section "OutputClass"
    Identifier "nvidia"
    MatchDriver "nvidia-drm"
    Driver "nvidia"
    Option "AllowEmptyInitialConfiguration"
    Option "PrimaryGPU" "yes"
    ModulePath "/usr/lib/nvidia/xorg"
    ModulePath "/usr/lib/xorg/modules"
EndSection

and also at 10-amdgpu.conf: (create it if needed)

sudo vim /usr/share/X11/xorg.conf.d/10-amdgpu.conf

paste this:

Section "OutputClass"
        Identifier "AMDgpu"
        MatchDriver "amdgpu"
        Driver "modesetting"
EndSection

For intel CPUs I'm not exactly sure but, if you have a file started with 10-intel something, editing the driver line to Driver "modesetting" should be enough

then: (edit first and copy after so you don't need to edit twice)

sudo cp -R /usr/share/xorg..conf.d/ /etc/X11/

After if in your ~/.xinitrc, if you dont have it create it:

 sudo vim ~/.xinitrc

and add the following:

xrandr --setprovideroutputsource modesetting NVIDIA-0 
xrandr --auto

in my case I also added: (if you skip this nvidia will work standalone)

xrandr --output eDP-1-1 --set "PRIME Synchronization" 1

to activate synchronization between integrated and dedicated graphics.

Now it will depend on your display manager , in my case I use LightDM, if you use another check the 3 section on the provided link and proceed as suggested.

so for LightDm edit your go to your /etc/lightdm/ and create a file named display_setup.sh

sudo vim /etc/lightdm/display_setup.sh

at the start of the file add #!/bin/sh and the same as you put in .xinitrc, so:

xandr --setprovideroutputsource modesetting NVIDIA-0
xrandr --auto
xrandr --output eDP-1-1 --set "PRIME Synchronization" 1

I chmoded it but they didn't tell to:

sudo chmod +x /etc/lightdm/display_setup.sh

After in your lightdm.conf:

sudo vim /etc/lightdm/lightdm.conf

Find the seat session and at the following line:

 [Seat:*] 
#display-setup-script=

uncomment and add the path to display_setup.sh

 display-setup-script=/etc/lightdm/display_setup.sh

I also changed the line:

[LightDM]
#logind-check-graphical=false

to true:

logind-check-graphical=true

lastly reboot and then check with nvtop if your machine is using your nVidia gpu.

That's it, i worked for me at least, Hope it helps someone else, I'm open and hoping for any feedback or corrections, as this was mostly trial and error process with some previous experience from other trial and error processes, maybe some of these lines are just placebo, maybe something might even be wrong but not breaking the system.

Thanks for reading :)
