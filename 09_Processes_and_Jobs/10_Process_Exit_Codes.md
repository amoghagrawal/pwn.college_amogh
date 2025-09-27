Process Exist Codes

Obtain an error code of the process `/challenge/get-code` and input that as an arguement to `challenge/submit-code`

## My solve
**Flag** `pwn.college{ErKRiOC8TcBZAVDK1tMuidMEKZv.QX5YDO1wCO2gjNzEzW}`
- On running `/challenge/get-code` we get an error that can be accessed using `?`
- On reading the variable using `echo $?` we get the code to be 242
- Submitting the code as an arugement to `/challenge/submit-code` gives us the flag

```
/challenge/get-code
echo $?
/challenge/submit-code 242
```

## What I learned
Erorrs of the recently run command are stored in a variable called `?` which shows 0 when the command as succeeded and 1 when it fails in most cases