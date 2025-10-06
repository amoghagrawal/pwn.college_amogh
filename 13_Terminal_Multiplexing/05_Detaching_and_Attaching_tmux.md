# Detaching and Attaching (tmux)

Using `tmux` to create a screen and detach and reattach it to get the flag

## My solve
**Flag** `pwn.college{QD2BWS-umKPgn7S8iAscfp8SR0_.0VO4IDOxwCO2gjNzEzW}`
- The challenge requires us to create a screen using `tmux`
- We need to detach it with **Ctrl+B d** and type `/challenge/run`
- On reattching with `tmux attach` or `tmux a` we get the flag

```bash
tmux
# press Ctrl+B d for detaching
/challenge/run
tmux attach
```

## What I learned
Tmux is the modern alternative to screen. It has the commands `tmux ls`, and it can be detached using Ctrl+B d and reattached by `tmux a`