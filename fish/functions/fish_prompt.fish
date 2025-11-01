function fish_prompt
        set -l last_status $status
        if set -q CONDA_LEFT_PROMPT
                __conda_add_prompt
        end
        return_last_status $last_status
        __fish_prompt_orig
end
