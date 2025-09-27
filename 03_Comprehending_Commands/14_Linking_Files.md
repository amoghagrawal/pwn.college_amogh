# linking files

Soft and Hard symbolic links using `ln`

## My solve
**Flag** `pwn.college{ElB6diz_IHr1xYNQNOPgTULFmy0.QX5ETN1wCO2gjNzEzW}`

```
ln -s /flag /home/hacker/not-the-flag
/challenge/catflag
```

## What I learned
Hard links are created using `ln oldlink newlink` and soft links are created using `ln -s oldlink newlink`. Soft links just transfer the user to the old file location and they cannot be accessed if the original is deleted. Hard links also copy the data ansd can be accessed after data deletion also.
