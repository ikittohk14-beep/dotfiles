#!/bin/sh

exec 3<> >(cat)
Xwayland -rootless -terminate -displayfd 3 &

read DISPLAY_NUM <&3
export DISPLAY=:$DISPLAY_NUM

echo "DISPLAY=$DISPLAY"

systemctl --user set-environment DISPLAY=$DISPLAY
systemctl --user import-environment DISPLAY WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
dbus-update-activation-environment --systemd DISPLAY WAYLAND_DISPLAY XDG_CURRENT_DESKTOP

exec driftwm
