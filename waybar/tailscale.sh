#!/bin/sh
vpn=$(tailscale status --peers --json 2> /dev/null)
state=$(echo $vpn | jq -r .BackendState)
res=""
if [[ "$state" == "Running" ]]; then
    res="${res}󱗼"
fi

echo $res
