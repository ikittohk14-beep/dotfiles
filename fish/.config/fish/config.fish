function ikifetch_comm
    ikifetch --gif ryo3.gif --kitty $argv
end

if status is-interactive; and test -t 1
    ikifetch_comm
end

alias fetch="ikifetch_comm"
alias agy="command agy --dangerously-skip-permissions"

function cava
    command cava $argv
    clear
    ikifetch_comm --static
end

function peaclock
    command peaclock $argv
    clear
    ikifetch_comm --static
end

fish_add_path /home/ikitto/.spicetify
fish_add_path /home/ikitto/.local/bin

function fish_prompt_update_colors --on-event fish_prompt

    set -g fish_color_autosuggestion 929092

    set -g fish_color_param c2c6d6

    set -g fish_color_operator 859aea
end

set -gx PATH "/home/ikitto/.local/bin" $PATH
