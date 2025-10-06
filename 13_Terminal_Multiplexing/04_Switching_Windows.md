# Switching Windows

Find the flag hidden in one of the windows of the screen

## My solve
**Flag** `pwn.college{wO4n_hcu2pvwsaET7oIPqLeRKH7.0FO4IDOxwCO2gjNzEzW}`
- First we need to attach to the screen having the windows
- On typing `screen -ls` we find the screen **135.challenge_session   (Detached)** as the only active screen
- On attaching the screen we find the instructions that the flag is on window 0
- We switch to window 0 with Ctrl+A 0

```bash
screen -ls
screen -r 135
# opens window 1
# press Ctrl+A 0 for window 0
```

## What I learned
We can create a window using **Ctrl+A c**, move between windows with **Ctrl+A n** and **Ctrl+A p**. Switch between windows 0-9 with **Ctrl+A 0** and so on. To bring the selection of all the windows, we use **Ctrl+A "**