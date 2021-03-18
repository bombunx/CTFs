# Various Vernacular (340)

> This flag was intercepted. wmysau{foeim_Tfusoli}
> Unfortunately, it seems to be encrypted. Additional encrypted text was also found.
> Hkgxologflutleiaymt xgf Azutgkrftmtf ltmntf ERW wfr ELW wfmtk Rkweq.


# Solution

This was not a staightforward challenge as we were only able to solve the questions with the help of a hint.

From first glance, we deduced that it might be a substitution cipher but even using brute force method yields nothing. We tried rotational cipher and Viginere cipher but also got nothing. We sort of gave up around here and moved on to other challenges.

### Hint 1
> The plaintext may not necessarily be in English.

This was one of the hints that was provided after some time. Knowing this, we then tried to decode the tools in different languages. We bruteforce decoded in different languages and then put the output through Google Translate to see if it makes sense.

We decoded in German and got the following text as a result:


> Provisionsgeschalte von Abgeordneten setzen CDU und CSU unter Druck.

English:

> The CDU and CSU are under pressure from members of parliament.

```
Key: 
abcdefghijklmnopqrstuvwxyz     
azertduiocqyjfghbklmwxspvn  
```

Decoding the flag with the key gives us: 

> UTLXAG{NICHT_ENGXISH}

Perform some substitution manually to find the flag.


Flag: `utflag{nicht_english}`
