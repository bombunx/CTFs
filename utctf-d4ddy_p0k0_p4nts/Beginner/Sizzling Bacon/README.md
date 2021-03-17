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
101001001100101010110000000110{0001010001010001001001111110000000100000000100111001101000100100001111001110010010001}
```


Flag: `utflag{crispy_bacon_cipher}`
