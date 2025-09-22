# Comprehending Commands

## cat: not the pet, but the command!
Understanding the `cat` command to display file contents
### My solve
**Flag** `pwn.college{UmS9MZCYZxYjAKOo3zTVKC2RPql.QXxcTN0wCO2gjNzEzW}`

```
cat flag
```

### What I learned
The `cat` command prints the contents of a file

## catting absolute paths
Using `cat` with absolute file paths
### My solve
**Flag** `pwn.college{kAfbjyy8tNRLd9BqZCXPvx0Qtrd.QX5ETO0wCO2gjNzEzW}`

```
cat /flag
```

### What I learned
You can use absolute paths with `cat` to read files from anywhere in the directories

## more catting practice
Using `cat` to navigate to files without `cd`
### My solve
**Flag** `pwn.college{oA7qWLhUNcKKkV6FsJB2qUSBCMd.QXwITO0wCO2gjNzEzW}`

```
cat /usr/share/doc/flag
```

### What I learned
`cat` works with any readable file, and is useful for quickly viewing contents.

## grepping for a needle in a haystack
Using `grep` to search for text in files
### My solve
**Flag** `pwn.college{M99C2lhWBQvZIT0Q9wYtjtYk7vo.QX3EDO0wCO2gjNzEzW}`

```
grep pwn.college /challenge/data.txt
```

### What I learned
`grep` is used to find lines having a specific string in fils, in our case the flag contains `pwn.college` which is a common thing across all flags

## comparing files
Comparing the contents of two files using `diff`
### My solve
**Flag** ` pwn.college{wXCprUf9Oex_5XF2DLJOTzhR7BU.01MwMDOxwCO2gjNzEzW}`

```
diff /challenge/decoys_only.txt /challenge/decoys_and_real.txt
```
- the flag is on line 35 of the second file, after line 34 of the intial file (34a35)

## listing files
Listing files in a directory
### My solve
**Flag** `pwn.college{YyM5deFYh6unju3KY10MjguRWAV.QX4IDO0wCO2gjNzEzW}`
- Find the files inside the challenge directory
- Run the renamed run file

```
ls /challenge
/challenge/16635-renamed-run-20397
```

## touching files
Creating new files using `touch`
### My solve
**Flag** `pwn.college{0303dpG7ZS4lFWLBiXq0b1klUx7.QXwMDO0wCO2gjNzEzW}`

```
touch /tmp/pwn
touch /tmp/college
/challenge/run
```

## removing files
Deleting files using `rm`
### My solve
**Flag** `pwn.college{kzLCeJqwuOEfkUEF5dNMzdcQ9ck.QX2kDM1wCO2gjNzEzW}`

```
rm delete_me
/challenge/check
```

## moving files
Moving or renaming files using `mv`
### My solve
**Flag** `pwn.college{AXsuzlF8chjJSs31lcg5wFiwMVr.0VOxEzNxwCO2gjNzEzW}`

```
mv /flag /tmp/hack-the-planet
```

## hidden files
Navigating hidden files using `ls -a`
### My solve
**Flag** `pwn.college{otVAsF91RwqdhEbclzl_rN4hyzs.QXwUDO0wCO2gjNzEzW}`

```
ls \ -a
cd \
cat ./.flag-4694279015222
```

### What I learned
Files can be hidden from being shown by default if they start with a `.`

## An Epic Filesystem Quest
Find the flag hidden behind multiple directories
### My solve
**Flag** `pwn.college{Q_777Ry_5tcbYYdVlJJgUhdodLp.QX5IDO0wCO2gjNzEzW}`

```
cd /
ls
cat ALERT
cd /usr/local/lib/python3.8/dist-packages/jupyter_server/files/__pycache__
ls
cat CUE
cd /usr/lib/python3/dist-packages/zope/interface/common/tests/__pycache__
ls
cat TEASER
cd /usr/lib/python3/dist-packages/python3_openid-3.1.0.egg-info
ls
cat NUGGET
cd /usr/share/javascript/mathjax/unpacked/jax/output/SVG/fonts/TeX/Main/Bold
ls
cat EVIDENCE
cd /usr/share/glib-2.0/schemas
cat TRACE
cd /opt/linux/linux-5.4/tools/testing/selftests/powerpc/eeh
ls -a
cat .POINTER
cd /usr/local/lib/python3.8/dist-packages/jedi/third_party/django-stubs/django-stubs/contrib/contenttypes/management/commands
ls
cat SPOILER
cd /opt/tcpdump/.git/refs/heads
ls
cat MESSAGE-TRAPPED
```

## What I learned
Hints and the flag can be trapped in a serious of files and we need to find the clues leading up to the flag

## making directories
Making directories using `mkdir`
### My solve
**Flag** `pwn.college{YmZVlEk9xuIz7Eov7QX85jUhIZR.QXxMDO0wCO2gjNzEzW}`

```
cd /tmp
mkdir pwn
touch pwn/college
/challenge/run
```

## What I learned
We can create directories using `mkdir`


## finding files
Finding files using `find`
### My solve
**Flag** `pwn.college{cDmS98LM4-o8ylZHj7bEFlEUDuw.QXyMDO0wCO2gjNzEzW}`
- Tried finding the flag file in `/` but couldnt find anything
- Ran the find command in `challenge` but no result
- Ran the command in `usr` to get two possible flag files: `/usr/local/lib/python3.8/dist-packages/pwnlib/flag` and `usr/share/emacs/26.3/lisp/obsolete/flag`
- `/usr/local/lib/python3.8/dist-packages/pwnlib/flag` contains `flag.py` but permission is denied
- `usr/share/emacs/26.3/lisp/obsolete/flag` is the program containing the flag

```
cd /
find usr -name flag
cat usr/share/emacs/26.3/lisp/obsolete/flag
```

## What I learned
The `find` command takes the name and the location to find the file in, otherwise it shows all the files and uses the current location to find the files.


## linking files
Soft and Hard symbolic links using `ln`
### My solve

```
cd /
find usr -name flag
cat usr/share/emacs/26.3/lisp/obsolete/flag
```

## What I learned
Hard links are created using `ln oldlink newlink` and soft links are created using `ln -s oldlink newlink`. Soft links just transfer the user to the old file location and they cannot be accessed if the original is deleted. Hard links also copy the data ansd can be accessed after data deletion also.