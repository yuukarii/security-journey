# Tmux configuration

## Configuration file

`~/.config/tmux/tmux.conf`

```
unbind C-Space
set -g prefix C-Space
bind C-Space send-prefix

set-option -g history-limit 10000
setw -g mode-keys vi
set -g mouse on

set -g base-index 1
setw -g pane-base-index 1
```