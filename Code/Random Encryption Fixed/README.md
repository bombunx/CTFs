# Random Encryption Fixed

>  We found the following file on a hacked terminal:

```
import random
flag = "flag{not_the_flag}"
seeds = []

for i in range(0,len(flag)):
    seeds.append(random.randint(0,10000))

res = []

for i in range(0, len(flag)):
    random.seed(seeds[i])
    rands = []
    for j in range(0,4):
        rands.append(random.randint(0,255))
    res.append(ord(flag[i]) ^ rands[i%4])
    del rands[i%4]
    print(str(rands))

print(res)
print(seeds)
```

> Output of a previous run:

```

[249, 182, 79]
.
.
. (trimmed for ease of reading)
[184, 161, 235, 97, 140, 111, 84, 182, 162, 135, 76, 10, 69, 246, 195, 152, 133, 88, 229, 104, 111, 22, 39]
[9925, 8861, 5738, 1649, 2696, 6926, 1839, 7825, 6434, 9699, 227, 7379, 9024, 817, 4022, 7129, 1096, 4149, 6147, 2966, 1027, 4350, 4272]
```

## Code

1.  Use the output of res (second last list) as the "flag", and create a loop to loop through the indexes.
2.  Create a empty list ```characterList``` to store all characters iteratively.
3.  Modify the line denoted as:
    ```
    res.append(ord(flag[i]) ^ rands[i%4])
    ```
    to
    ```
    characterList.append(chr(res[i] ^ rands[i%4]))
    ```
    > This works as the encryption used is using XOR (^) operator, which can be symmetrically decrypted using the same operator. This line finds the original ordinal value and finds the character for that ordinal.
4.  Join the characters in the list.
    ```
    ''.join(characterList)
    ```
    This finds the flag.