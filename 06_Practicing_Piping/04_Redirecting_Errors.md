# Redirecting Errors

Learning about File Descriptor (FD) and using them to redirect the output and errors

## My solve
**Flag** `pwn.college{44op78AXi0z-XQN6CK_ElblOo7H.QX3YTN0wCO2gjNzEzW}`
- The challenge wants us to redirect the flag which is the output (FD1) to `myflag` and the error/instructions from FD2 to `instructions`

```
/challenge/run > myflag 2> instructions
cat myflag
```

## What I learned
File descriptors are channels in linux where FD0 is the stdin, FD1 is stdout and FD2 is stderr. We can specify the channel's output we want to write onto the file by specifying the number before `>` like `1>` will write the output onto the file
