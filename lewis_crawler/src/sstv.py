"""SSTV Lib. Contains all the required methods for
    - Robotic Camera Actuation
    - SSTV Generation
    - SSTV Scheduling."""

from shutil import copyfile
from PIL import Image, ImageFont, ImageDraw
from pysstv import color
import os, errno

def take_photo():
    # This def is meant to take a photograph from the robot, 
    # it should include all steps and error checking to raise the mast
    # Take the photo, and put the mast down.

    # Copy in the test pattern png (if photo process errors out, this will be used instead)
    copyfile('lewis_crawler/templates/TEST_PATTERN.jpg', 'lewis_crawler/working/working.jpg')

    # Software to take the photo should be here
    copyfile('lewis_crawler/templates/TEST_PATTERN.jpg', 'lewis_crawler/working/working.jpg')

def prepare_martin1():
    raw_img = Image.open("lewis_crawler/working/working.jpg") # Open the current working image
    img = raw_img.resize((320, 256), Image.ANTIALIAS) # resize it for the Martin M1

    if False:
        TINT_COLOR = (255, 255, 255) # White text bg
        TEXT_COLOR = (0,0,0)
    else:
        TINT_COLOR = (0, 0, 0) # Black text bg
        TEXT_COLOR = (255,255,255)
    TRANSPARENCY = .25  # Degree of transparency, 0-100%
    OPACITY = int(255 * TRANSPARENCY)
    overlay = Image.new('RGBA', img.size, TINT_COLOR+(0,))

    draw = ImageDraw.Draw(overlay)
    font = ImageFont.truetype(r'lewis_crawler/templates/nasalization.ttf', 20)
    
    draw.rectangle(((0, 0), (90, 20)), fill=TINT_COLOR+(OPACITY,))
    draw.text((0, 0),"KW1FOX",TEXT_COLOR,font=font) # Draw KW1FOX in the top left

    img = img.convert("RGBA")
    img = Image.alpha_composite(img, overlay)
    img = img.convert("RGB")
    img.save('lewis_crawler/working/working.jpg') # Save the working image

    slowscan_message = color.MartinM1(img, 48000, 16) # Image, rate, bits
    return slowscan_message

def prepare_robot36():
    raw_img = Image.open("lewis_crawler/working/working.jpg") # Open the current working image
    img = raw_img.resize((320, 240), Image.ANTIALIAS) # resize it for robot36

    if False:
        TINT_COLOR = (255, 255, 255) # White text bg
        TEXT_COLOR = (0,0,0)
    else:
        TINT_COLOR = (0, 0, 0) # Black text bg
        TEXT_COLOR = (255,255,255)
    TRANSPARENCY = .25  # Degree of transparency, 0-100%
    OPACITY = int(255 * TRANSPARENCY)
    overlay = Image.new('RGBA', img.size, TINT_COLOR+(0,))

    draw = ImageDraw.Draw(overlay)
    bigfont = ImageFont.truetype(r'lewis_crawler/templates/nasalization.ttf', 20) 
    smallfont = ImageFont.truetype(r'lewis_crawler/templates/nasalization.ttf', 17) 
    
    draw.rectangle(((0, 0), (90, 20)), fill=TINT_COLOR+(OPACITY,))
    draw.text((0, 0),"KW1FOX",TEXT_COLOR,font=bigfont) # Draw KW1FOX in the top left

    draw.rectangle(((0, 40), (83, 80)), fill=TINT_COLOR+(OPACITY,))
    draw.text((0, 40),"day: 25.2",TEXT_COLOR,font=smallfont)
    draw.text((0, 60),"Volt: 13.8",TEXT_COLOR,font=smallfont)
    #draw.text((0, 80),"Miles: 1.02",TEXT_COLOR,font=smallfont)

    img = img.convert("RGBA")
    img = Image.alpha_composite(img, overlay)
    img = img.convert("RGB")
    img.save('lewis_crawler/working/working.jpg') # Save the working image
    slowscan_message = color.Robot36(img, 48000, 16) # Image, rate, bits
    return slowscan_message

if __name__ == "__main__":
    # Take photograph. 
    take_photo() # Saves a photograph to the working/working.jpg location

    # Draw neccicary text on photo
    slowscan = prepare_robot36() # Quick n dirty
    #slowscan = prepare_martin1() # Much slower, but cleaner picture


    try:
        os.makedirs('lewis_crawler/working')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    slowscan.write_wav('lewis_crawler/working/working.wav')

    #sstv('working/working.png', 'working/radio.wav', mode='Robot36')

def do_test():
    # Take photograph. 
    take_photo() # Saves a photograph to the working/working.jpg location

    # Draw neccicary text on photo
    slowscan = prepare_robot36() # Quick n dirty
    #slowscan = prepare_martin1() # Much slower, but cleaner picture


    try:
        os.makedirs('lewis_crawler/working')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    slowscan.write_wav('lewis_crawler/working/working.wav')

    #sstv('working/working.png', 'working/radio.wav', mode='Robot36')
