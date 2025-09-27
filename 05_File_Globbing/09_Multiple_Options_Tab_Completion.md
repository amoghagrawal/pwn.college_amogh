# Multiple Options for Tab Completion

Using the tab key for autocompletion of the arugement and finding the correct file having the flag

## My solve
**Flag** `pwn.college{g4yBAN12WE1ot7uyor_RpVnsfR2.0lN0EzNxwCO2gjNzEzW}`
- Pressing tab on `cat /challenge/files/p` gives us `/challenge/files/pwn` first and then a list of possible files:
```
pwn                    pwn-the-planet         pwncollege-flag        pwncollege-flyswatter  
pwn-college            pwncollege-family      pwncollege-flamingo    pwncollege-hacking
```
- By trial and error, we find the right file which is `pwncollege-flag`

```
cat /challenge/files/pwncollege-flag 
```
