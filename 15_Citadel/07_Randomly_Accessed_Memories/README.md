# DESCRIPTION
Get the flag from the github repo https://github.com/evilcryptonite/daft-punk-archive

# WRITEUP

- The challenge has a verse hinting at using **git** to get the flag
```
clone it, pull it, reset it, stage it,
commit, push it, fork, rebase it,
merge it, branch it, tag it, log it,
add it, stash it, diff, untrack it.
```
- Using `git log` we get to see 3 commits in which secret chunks have been added
- By copying the object IDs and using them with `git show` we can see the additions made in the commit
- The additions happened to be Base64 encoded flags
- To get the flags we had to decode it from Base64

1. Chunk 1 (50474f316ba2ff644b546437a032971874f43ecf): `citadel{w3_4r3`
2. Chunk 2 (cc8b79a83c2ef5997c728d1037368042af85214f): `up_4ll_n1t3`
3. Chunk 3 (79af115d8b2cef0f3110f21f5475e1b5bea1a0af): `t0_g1t_lucky}`

> citadel{b3tt3r_ROTt3n}
