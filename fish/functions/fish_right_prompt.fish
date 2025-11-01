function fish_right_prompt
        if not set -q CONDA_LEFT_PROMPT
                __conda_add_prompt
        end
        __fish_right_prompt_orig
end
