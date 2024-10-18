#!/bin/sh
player_status=$(tailscale status --peers --json 2> /dev/null | grep ".ExitNodeStatus")
if [[ $? == 1 ]]; then
    echo " "
else 
    echo "󱗼"
fi
