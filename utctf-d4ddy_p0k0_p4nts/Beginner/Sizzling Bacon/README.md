# Sizzling Bacon (100)

> My buddy Francis is really into Bacon. He loves it so much that he gave me this encoded bacon-themed flag (he said he was inspired by the sound of sizzling bacon).

```
sSsSSsSSssSSsSsSsSssSSSSSSSssS{SSSsSsSSSsSsSSSsSSsSSssssssSSSSSSSsSSSSSSSSsSSsssSSssSsSSSsSSsSSSSssssSSsssSSsSSsSSSs}
```


# Solution

From the name of the challenge, we deduced that this was probably a Bacon cipher (Baconion cipher)

Baconian cipher works by representing the plain text as 5-bit binary representation. The binary representation is then substituted with 2 different alphabets.
In this case, the binary representations are replaced with 's' and 'S'.

We know that the plaintext before the '{' is 'utflag', so by changing the 's' to 1 and 'S' to 0 would give us the binary represntation of the flag.
Convert the binaries to plaintext using ASCII table and the flag is obtained.

```
10100 10011 00101 01011 00000 00110 {00010 10001 01000 10010 01111 11000 00001 00000 00010 01110 01101 00010 01000 01111 00111 00100 10001}
```


Flag: `utflag{crispy_bacon_cipher}`
