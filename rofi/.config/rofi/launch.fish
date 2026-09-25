#!/usr/bin/env fish

set current_time (date +"  %H:%M      %d.%m.%Y")

killall -q rofi
rofi -show drun -mesg "$current_time"
