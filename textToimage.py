import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer "}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print("Status Code:", response.status_code)  # Print status code for debugging
    print("Response Content:", response.content[:500])  # Print part of the response content for inspection
    return response.content


user_input = input("Enter a description of an image: ")

# Query the model for image generation
image_bytes = query({
    "inputs": user_input,
})

# Try opening the image
try:
    image = Image.open(io.BytesIO(image_bytes))
    image.show()  # This will open the image in the default image viewer
except IOError:
    print("Failed to open image. The response might not contain valid image data.")

