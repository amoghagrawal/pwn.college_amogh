# Deleting Newlines

Using `tr -d \"n"` to delete the unwanted newlines to obtain the correct flag

## My solve
**Flag** `pwn.college{o21ViWVlCvX6yQoF7G1EaeBeCsq.0VNxEzNxwCO2gjNzEzW}`
- The flag has unwanted newlines that we have to remove using `tr -d "\n`

```
/challenge/run | tr -d "\n"
```

## What I learned
Newlines are shown by "\n" and we can delete from from the stdout using `tr -d "\n"`