# Proxed (100)

```
Cool haxxorz only

Author: Jordan Bertasso
```
>[http://web2.utctf.live:5320/](http://proxed.duc.tf:30019)

# Solution
When connecting to the webpage, it will prompt that an untrusted IP is connecting to it.
Analyze the source code which would say that it checks the "X-Forwarded-For" header if it matches 31.33.33.7.
Send the modified request using curl or BurpSuite to the server and the flag would be revealed.

# Flag
```
DUCTF{17_533m5_w3_f0rg07_70_pr0x}
```
