# Challenge (50)
NzMgNzkgNmUgNzQgN2IgNzAgNjIgNjEgNzQgNjUgNmUgNjcgNjYgNWYgNmMgNjIgNjggNWYgNzQgNjIgNjcgNWYgN2EgNzIgN2Q=

# Solution
This is a base64 encoded string based on the "=" sign at the end of the string. ([Base64 Decoder](https://www.base64decode.org/))

Pass it into an online decoder will give you a hex result.
```
73 79 6e 74 7b 70 62 61 74 65 6e 67 66 5f 6c 62 68 5f 74 62 67 5f 7a 72 7d
```
Convert the hex results into ASCII.https://www.rapidtables.com/convert/number/hex-to-ascii.html
```
synt{pbatengf_lbh_tbg_zr}
```
Finally, use ROT13 to decode the string and you will get the flag. https://www.dcode.fr/rot-13-cipher
```
flag{congrats_you_got_me}
```

# Flag
flag{congrats_you_got_me}
