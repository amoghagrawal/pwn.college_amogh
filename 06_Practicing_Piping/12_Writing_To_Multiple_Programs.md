# Writing to Multiple Programs

Writing the standard input of one command to two other commands directly without copying it using tee and process susbstition

## My solve
**Flag** `pwn.college{E2z9OGZeqmcm4lNeoAvnGg9pCOC.QXwgDN1wCO2gjNzEzW}`
- The challenge asks us to write the input of `/challenge/hack` to two more commands, `/challenge/the` and `/challenge/planet`
- It requires us to duplicate the data using `tee` and use process substition for input
- Process substition treats commands as files also when written like `>()`

```
/challenge/hack | tee >(/challenge/the) >(/challenge/planet)
```
