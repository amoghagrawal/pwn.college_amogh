# Pondering Paths
`/` is the root of directory <br>
`~` is /home/hacker and this is where we start on pwn.college <br>
paths can be either absolute or relative <br>
`.` means the current directory <br>
`..` means to the previous directory <br>

## The Root
Understanding of the root directory `/`
### My solve
**Flag** `pwn.college{MtleBnWeHxP6fGDldNhe5g0Pgls.QX4cTO0wCO2gjNzEzW}`

```
/pwn
```
### What I learned
the pwn is a program inside the root directory

## Program and absolute paths
Understanding of absolute paths and running programs using them
### My solve
**Flag** `pwn.college{gT2SxUqfMywQ7YHnztDmiNQ_-UD.QX1QTN0wCO2gjNzEzW}`

```
/challenge/run
```
### What I learned
the run program has the flag which is in the challenge directory which is in the root directory

## Position thy self
Understanding of changing directories using `cd`
### My solve
**Flag** `pwn.college{kCeh4R_e4by8RpqGZ2Yp_d5Jl22.QX2QTN0wCO2gjNzEzW}`

```
/challenge/run
cd /usr/share/build-essential
/challenge/run
```
### What I learned
the command cd is used to navigate directories and stands for change directory

## Position elsewhere
Changing to another directory and running the program
### My solve
**Flag** `pwn.college{cVg2laPebKi_p4xNIxc6zL0ZHHK.QX3QTN0wCO2gjNzEzW}`

```
/challenge/run
cd /usr/share/build-essential
/challenge/run
```
### What I learned
we run `/challenge/run` to get the directory in which we need to run the flag, we change directories using `cd`

## Position yet elsewhere
Changing to a different directory and running the program
### My solve
**Flag** `pwn.college{sieAsi_2qL1eIvzcb7WP5vKJ0Qx.QX4QTN0wCO2gjNzEzW}`

```
/challenge/run
cd tmp
/challenge/run
```
### What I learned
changing directories lets us run programs from different locations

## implicit relative paths, from /
Using relative paths from the root directory `/`
### My solve
**Flag** `pwn.college{EMJmV4i2qt-uyviAVYbKB4vMK8-.QX5QTN0wCO2gjNzEzW}`

```
cd /
challenge/run
```
### What I learned
instead of running the program from `/challenge/run` which is an absolute path, we navigate to `/` and then use a relative path `challenge/run`

## explicit relative paths, from /
Using explicit relative paths with `.` from the root directory
### My solve
**Flag** `pwn.college{YsdkFsbux_5itXyOTZfhYNrQEvE.QXwUTN0wCO2gjNzEzW}`

```
cd /
./challenge/run
```
### What I learned
we can refer to the current directory using `.` in paths like `/challenge` and` /challenge/.` are same

## implicit relative path
Running a program in the current directory using `./`
### My solve
**Flag** `pwn.college{YsdkFsbux_5itXyOTZfhYNrQEvE.QXwUTN0wCO2gjNzEzW}`

```
cd /challenge
./run
```
### What I learned
linux doesnt execute programs in the current directory automatically to prevent accidental executation so run program in the challenge directory needs to executed using `./`

## home sweet home
`~` is the home/hacker directory 
### My solve
**Flag** `pwn.college{A3yQ_88AKw0ySDgoYQzrgJz0YyI.QXzMDO0wCO2gjNzEzW}`
- rewrites the flag from /challenge/run to ~/f directory

```
/challenge/run ~/f
```

### What I learned
in the dojo we start in the home directory which is `/home/hacker` and has our personal files and is denoted by `~` to save time