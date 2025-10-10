# DESCRIPTION
Decrypt `4:R256=Y3oRRoP0#~%Ro?A` to get the flag

# WRITEUP

- The challenge description says "the password to the next floor has been warped first by a factor of 47, then by a factor of 13"
- This hint leads us to think of using ROT47 and ROT13 to decode the cipher
- First I did ROT47 to get `ci#adel*b@##@!_ROT#@np` and then ROT13 to get `pv#nqry*o@##@!_EBG#@ac` which was incorrect
- Now reversing and doing ROT13 first to get `4:E256=L3bEEbC0#~%Eb?N` and then ROT47 to get the flag

> citadel{b3tt3r_ROTt3n}
