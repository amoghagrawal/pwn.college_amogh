# linking files

Soft and Hard symbolic links using `ln`

## My solve
```
cd /
find usr -name flag
cat usr/share/emacs/26.3/lisp/obsolete/flag
```

## What I learned
Hard links are created using `ln oldlink newlink` and soft links are created using `ln -s oldlink newlink`. Soft links just transfer the user to the old file location and they cannot be accessed if the original is deleted. Hard links also copy the data ansd can be accessed after data deletion also.
