# Tmux configuration

## Configuration file

`~/.tmux.conf`

Run this to apply new change inside a tmux session:
`tmux source-file ~/.tmux.conf`

## Center the window name in the status bar

```sh
set -g status-interval 5
set -g status-justify centre
```

## Index of window starts from 1

```sh
set -g base-index 1
```

```sh
set -g status-interval 5
set -g status-justify centre

set -g base-index 1
setw -g pane-base-index 1
set -g renumber-windows on

set -g mouse on
set-option -g history-limit 5000

setw -g mode-keys vi
```