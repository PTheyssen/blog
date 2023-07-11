# Tool for adding title to images

Simple python script that adds a black margin at the top of an jpg image. 
Additionaly an author, title and date is added as white text in the black margin.

## Usage 

add-title-border.py [-h] [-i INPUT] [-t TITLE] [-d DATE] [-o OUTPUT]

- INPUT: path to original jpg
- TITLE: string of title (will be in center)
- DATE: date of the picture
- OUTPUT: output name of the new image that will be created

## Example Usage:
```
p3 add-title-border.py -i BER-01-2023/DSC06626.jpg -t "HELLO WORLD" -d "JANUARY 2023" -o test.jpg
```
