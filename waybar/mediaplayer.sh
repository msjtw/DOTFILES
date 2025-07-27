#!/bin/sh
player_status=$(playerctl -p "spotify" status 2> /dev/null)
if [ "$player_status" = "Playing" ]; then
    echo "$(playerctl -p "spotify" metadata artist) - $(playerctl -p "spotify" metadata title)"
elif [ "$player_status" = "Paused" ]; then
    echo "paused"
fi

player_status=$(playerctl -p "spotify_player" status 2> /dev/null)
if [ "$player_status" = "Playing" ]; then
    echo "$(playerctl -p "spotify_player" metadata artist) - $(playerctl -p "spotify_player" metadata title)"
elif [ "$player_status" = "Paused" ]; then
    echo "paused"
fi
