import textwrap

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

def draw_quote_on_image(image_path,
                        quote,
                        author,
                        font_path="font.ttf",
                        contrast_factor=0.7,
                        font_size=145):
    # Open the existing image
    img = Image.open(image_path)

    # Calculate crop area to make the image square
    min_dimension = min(img.size)
    left = (img.width - min_dimension) // 2
    top = (img.height - min_dimension) // 2
    right = left + min_dimension
    bottom = top + min_dimension

    # Crop the image
    img = img.crop((left, top, right, bottom))

    # Darken the image
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(contrast_factor)

    draw = ImageDraw.Draw(img)

    # Set the font with anti-aliasing enabled
    font = ImageFont.truetype(font_path, size=font_size, layout_engine=ImageFont.LAYOUT_BASIC)

    # Create Paragraph From Quote Text
    para = textwrap.wrap(quote, width=30)

    # Calculate vertical position for the quote in the center
    vertical_pos = (img.size[1] - sum(draw.textsize(line, font=font)[1] for line in para)) // 2
    current_h, pad = vertical_pos, 10

    # Draw the text using PIL's text method
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((img.width - w) // 2, current_h), line, font=font, fill="white")
        current_h += h + pad

    # Draw Author with hyphen
    author_line = f"- {author}"
    w, h = draw.textsize(author_line, font=font)
    draw.text(((img.width - w) // 2, current_h), author_line, font=font, fill="white")

    # Save the image in the root directory
    img.save("quote_image.png")