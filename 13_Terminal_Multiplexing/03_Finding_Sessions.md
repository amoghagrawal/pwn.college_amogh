# Finding Sessions

Find the flag hidden in one of the detached screens

## My solve
**Flag** `pwn.college{INNnUa0khdofbP-V1TlpSITgzGD.01N4IDOxwCO2gjNzEzW}`
- In the challenge, 3 screens have been detached and one of them has the flag
- With `screen -ls` we find the PIDs of the 3 detached screens as **144, 147 and 150**
- Manually attaching each screen and then detaching when done we find 150 has the flag and 144, 147 are the wrong ones

```bash
screen -ls
screen -r 144
# press Ctrl+A following by d
screen -r 147
# press Ctrl+A following by d
screen -r 150
# press Ctrl+A following by d
```

## What I learned
We can check the PIDs and names of the detached screens with `screen -ls`