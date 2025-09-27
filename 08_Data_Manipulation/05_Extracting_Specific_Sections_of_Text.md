# Extracting Specific Sections of Text

Using `cut` to display specific columns and obtaining the flag from it

## My solve
**Flag** `pwn.college{kJK9DLaXJqm9xeEYlUIKLtA4LKS.01NxEzNxwCO2gjNzEzW}`
- The challenge requires to only use the column 2 of the `challenge/run` output so we use the `cut command` to do that
- We delete the newlines from the cut output using `tr`

```
/challenge/run | cut -d " " -f 2 | tr -d "\n"
```

## What I learned
`cut` can be used to only show specific columns of an output where `-d` is the delimiter and `-f` is the column number