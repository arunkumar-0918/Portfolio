from PIL import Image, ImageDraw

def crop_square_with_top_bias(img, top_bias_ratio=0.2):
    width, height = img.size
    square_size = min(width, height)
    
    # Calculate top-biased crop box
    left = (width - square_size) // 4
    top = int((height - square_size) * top_bias_ratio)
    top = max(top, 0)  # Ensure it's not negative
    bottom = top + square_size 
    return img.crop((left, top, left + square_size, bottom))

# Load image
img = Image.open("image/arun.jpg").convert("RGBA")

square_img = crop_square_with_top_bias(img, top_bias_ratio=0.05)  # Adjust 0.05–0.3 for more/less headroom

# Resize the cropped image slightly smaller
resize_factor = 0.9  # 90% of the original size (adjust to reduce more or less)
square_img = square_img.resize(
    (int(square_img.size[0] * resize_factor), int(square_img.size[1] * resize_factor)),
    Image.Resampling.LANCZOS
)

# Create mask
mask = Image.new('L', square_img.size, 0)
draw = ImageDraw.Draw(mask)

# Reduce the size of the circular mask to be slightly smaller than the square image
circle_margin = 10  # Adjust for a smaller circle
draw.ellipse(
    (circle_margin, circle_margin, square_img.size[0] - circle_margin, square_img.size[1] - circle_margin),
    fill=255
)

# Apply circular mask
square_img.putalpha(mask)

# Save or show the result
square_img.show()

