function fish_greeting -d "What's up, fish?"
    set_color $fish_color_autosuggestion


    echo " ____   ___  _   _ _ _____   ____             _      "
    echo "|  _ \\ / _ \\| \\ | ( )_   _| |  _ \\ __ _ _ __ (_) ___ "
    echo "| | | | | | |  \\| |/  | |   | |_) / _` | '_ \\| |/ __| "
    echo "| |_| | |_| | |\\  |   | |   |  __/ (_| | | | | | (__ "
    echo "|____/ \\___/|_| \\_|   |_|   |_|   \\__,_|_| |_|_|\\___| "


    echo "What's up, fish?"
    uname -nmsr

    command -q uptime
    and command uptime

    set_color normal
end
