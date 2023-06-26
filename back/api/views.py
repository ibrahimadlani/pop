""" This is the views file for the app. """

from django.http import JsonResponse, HttpResponse
from PIL import Image, ImageDraw, ImageFont


# Create your views here.


def index(request):
    """This is the index view."""
    return JsonResponse({"message": "Hello, world!"})


def pop(request, input):
    """This is the pop view."""

    image = Image.open("assets/img/bg.png")

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the font properties
    font_size = 96
    font_color = (255, 255, 255)  # Red color, you can modify it as per your needs
    font_path = "font/MabryPro-Bold.ttf"  # Replace with the actual font file path
    font = ImageFont.truetype(
        font_path,
        font_size,
    )

    # Define the text content and position
    text = "We are"

    text_position = (
        100,
        80 + font_size,
    )  # Coordinates of the top-left corner of the text

    # Draw the text on the image
    draw.text((100, 80), text, font=font, fill=font_color)
    draw.text(text_position, input, font=font, fill=font_color)

    # Save the modified image
    image.save("assets/img/result.png")

    image_file = (
        "assets/img/result.png"  # Replace with the actual path to your image file
    )

    # Open the image file
    with open(image_file, "rb") as f:
        image_data = f.read()

    return HttpResponse(image_data, content_type="image/png")
