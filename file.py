import requests
import os
from datetime import datetime

def download_random_image():
  """Downloads a random image from Unsplash and saves it to desktop."""
  url = "https://source.unsplash.com/random"
  response = requests.get(url, stream=True)

  # Check for successful response
  if response.status_code == 200:
    # Get unique filename with timestamp
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{now}.jpg"  # Adjust extension based on image type

    # Create desktop path (modify if needed)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    filepath = os.path.join(desktop_path, filename)

    # Save image
    with open(filepath, 'wb') as f:
      for chunk in response.iter_content(1024):
        f.write(chunk)
      print(f"Image downloaded and saved to: {filepath}")
  else:
    print(f"Error downloading image: {response.status_code}")

# Run download function
download_random_image()
