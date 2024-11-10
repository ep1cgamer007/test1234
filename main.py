from src.quote import get_random_stoic_quote
from src.unsplash import get_random_background
from src.draw import draw_quote_on_image

import os

if __name__ == "__main__":
  print("Starting Automation..")
  unsplash_api_key = os.environ['UNSPLASH_ACCESS_KEY']

  download_path = 'quote.jpg'

  # Get a random quote
  print("Fetching a random quote..")
  quote, author = get_random_stoic_quote()

  # Get a random background image from Unsplash and download it
  print("Fetching a random background image..")
  background_image_path = get_random_background(unsplash_api_key,
                                                download_path)

  if background_image_path:
    # Draw the quote on the background image and save it in the root directory
    print("Drawing the quote on the background image..")
    draw_quote_on_image(background_image_path, quote, author)


  print("Uploading to temp.sh...")
  os.system('curl -F "file=@quote_image.png" https://tmpfiles.org/api/v1/upload')
  print()
  print("Automation completed.")
