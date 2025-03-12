from rembg import remove
from PIL import Image

org="Pics/dhoni.jpg"
new="Pics/ndhoni.jpg"

img=Image.open(org)
mod=remove(img)
out=mod.convert("RGB")
out.save(new,"JPEG")

print("Successful")
