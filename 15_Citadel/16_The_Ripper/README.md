# DESCRIPTION
Extract the passcode hidden in the files using the given wordlist

# WRITEUP

- This was to be solved by using JohnTheRipper which is a password cracking tool
- We already had the wordlist and the hash for the program
- Running it through JohnTheRipper gave us the password which was the flag
```
john --wordlist=wordlist.txt --rules hash.txt
```

> citadel{fake_flag_4_fake_pl4y3rs}