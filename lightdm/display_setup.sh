#!/bin/sh
xrandr --setprovideroutputsource modesetting NVIDIA-0
xrandr --auto
if xrandr | grep -q 'HDMI-1-1 connected' ; then
	xrandr --output HDMI-1-1 --mode 1920x1080 --right-of eDP-1-1 --primary --set "PRIME Synchronization" 1
	xrandr --output eDP-1-1
else
	xrandr --output eDP-1-1 --set "PRIME Synchronization" 1
fi
