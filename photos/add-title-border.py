import argparse
from typing import Tuple
from PIL import Image, ImageDraw, ImageFont


def parse_command_line_arguments() -> Tuple[str, str, str, str]:
    parser = argparse.ArgumentParser(description='Image Title Border command line arguments')
    parser.add_argument('-i', '--input', help='input file')
    parser.add_argument('-t', '--title', help='title')
    parser.add_argument('-d', '--date', help='date')
    parser.add_argument('-o', '--output', help='output file')

    # Parse the command line arguments
    args = parser.parse_args()

    # Access the values
    input_file = args.input
    title = args.title
    date = args.date
    output_file = args.output

    # Perform your logic here using the input and output files
    print('Parsed the following:')
    print('Input file:', input_file)
    print('Title:', title)
    print('Date:', date)
    print('Output file:', output_file)
    return input_file, title, date, output_file


def validate_command_line_arguments(input_file: str, title: str, date: str, output_file: str) -> bool:
    if input_file.endswith("jpg") and output_file.endswith("jpg"):
        return True
    return False


def add_title_to_image(input_file: str, title: str, date: str, output_file:str):
    # Load the image
    img = Image.open(input_file)

    # Create a new image with a black rectangle at the top
    rect_height = int(img.height * 0.025)
    border_img = Image.new('RGB', (img.width, img.height+rect_height), color='black')
    border_img.paste(img, (0,rect_height))

    draw = ImageDraw.Draw(border_img)
    # font = ImageFont.truetype("path/to/font.ttf", size=20)
    font_size = int(rect_height * 0.7)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", font_size, encoding="unic")

    text_width, _ = draw.textsize(title, font)
    draw.text(((border_img.width - text_width) / 2, 10), title, 'white', font)

    # Define the text positions
    width, height = img.size
    name_position = (20, 10)  # Top left corner
    title_position = (width // 2, 10)  # Middle top
    date_position = (width - 20, 10)  # Top right corner

    # Write text1 at text1_position
    draw.text(name_position, "PHILIPP THEYSSEN", fill="white", font=font)

    # Write text2 at text2_position
    text_width, text_height = draw.textsize(title, font=font)
    text2_position = (title_position[0] - text_width // 2, title_position[1])
    draw.text(text2_position, title, fill="white", font=font)

    # Write text3 at text3_position
    text_width, text_height = draw.textsize(date, font=font)
    text3_position = (date_position[0] - text_width, date_position[1])
    draw.text(text3_position, date, fill="white", font=font)

    # Save the edited image as a new file
    border_img.save(output_file)


if __name__ == "__main__":
    input_file, title, date, output_file = parse_command_line_arguments()
    if not validate_command_line_arguments(input_file, title, date, output_file):
        print("Invalid command line arguments")
    add_title_to_image(input_file, title, date, output_file)
