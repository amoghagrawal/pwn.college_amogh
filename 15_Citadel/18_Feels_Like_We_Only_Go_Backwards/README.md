# DESCRIPTION
Get the flag by reverse engineering the binary script

# WRITEUP

- My first thought was to check the file in HxD but it was a `.elf` which is a binary file only
- Next on running it, it was asking for 3 things - a song, a number and the flag
- Randomly guessing on level 1, we found big strings like "feel like we only go backwards" or "the less i know the better" work
- Tried finding numbers for level 2 but nothing worked
- Next, I opened the file in Ghidra and checked the strings corresponding to the levels
- The strings lead us to the functions and on decoding those functions we got the the flag

> citadel{f0r_0n3_m0r3_h0ur_1_c4n_r4g3}