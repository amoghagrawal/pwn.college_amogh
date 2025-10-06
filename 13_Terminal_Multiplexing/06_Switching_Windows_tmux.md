# Switching Windows (tmux)

Finding the flag hidden on Window 0 of the tmux

## My solve
**Flag** `pwn.college{4tnYd4IKahN8EyaZIa3sN7_4LC2.0FM5IDOxwCO2gjNzEzW}`
- First we need to attach to the screen having the windows
- On typing `tmux ls` we find that there is only one tmux created
- We attach to with `tmux a` to find the instructions that the flag is on window 0
- We switch to window 0 with Ctrl+B 0

```bash
tmux ls
tmux a
# press Ctrl+B 0
```

## What I learned
We can create a window using **Ctrl+B c**, move between windows with **Ctrl+B n** and **Ctrl+B p**. Switch between windows 0-9 with **Ctrl+B 0** and so on. To see the window picker, we use **Ctrl+B w**