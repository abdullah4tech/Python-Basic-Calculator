# import pyfiglet

# # Create a Figlet font object
# font = pyfiglet.Figlet()

# # Enter the text you want to convert to ASCII art
# text = "Calculator"

# # Use the `renderText` method to create ASCII art
# ascii_art = font.renderText(text)

# # Print the ASCII art to the console
# print(ascii_art)

import pyfiglet

# Create a Figlet font object with custom settings
font = pyfiglet.Figlet(font="nancyj-fancy", justify="left", width=200)

# Enter the text you want to convert to ASCII art
text = "Calculator"

# Use the `renderText` method to create ASCII art
ascii_art = font.renderText(text)

# Print the ASCII art to the console
print(ascii_art)
