import platform

if platform.system() == "Darwin":
    font_size = 11
elif platform.system() == 'Linux':
    font_size = 11
else:
    font_size = 10

print("Font size:", font_size)
