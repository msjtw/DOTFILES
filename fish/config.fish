if [ -z "$WAYLAND_DISPLAY" ] && [ "$XDG_VTNR" -eq 1 ]
    exec niri --session
end

if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -Ux SSH_ASKPASS "/usr/lib/seahorse/ssh-askpass"

alias hx='helix'
alias vim='nvim'

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /home/msjtw/miniconda3/bin/conda
    eval /home/msjtw/miniconda3/bin/conda "shell.fish" "hook" $argv | source
else
    if test -f "/home/msjtw/miniconda3/etc/fish/conf.d/conda.fish"
        . "/home/msjtw/miniconda3/etc/fish/conf.d/conda.fish"
    else
        set -x PATH "/home/msjtw/miniconda3/bin" $PATH
    end
end
# # <<< conda initialize <<<

