if [ -z "$WAYLAND_DISPLAY" ] && [ "$XDG_VTNR" -eq 1 ]
    exec sway
end

if status is-interactive
    # Commands to run in interactive sessions can go here
end


alias hx='helix'
alias vim='nvim'
