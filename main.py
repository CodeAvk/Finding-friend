import glob
import imagehash
from PIL import Image

my_image_url="./boys/Tom.jpg"
my_hash=imagehash.average_hash(Image.open(my_image_url))


girls=glob.glob("./girls/*.jpg")
selected=girls[0]
accepted_diff=50

for girl in girls :
    girls_hash = imagehash.average_hash(Image.open(girl))
    diff=girls_hash-my_hash
    if diff < accepted_diff:
        selected=girl
        accepted_diff=diff

print(selected)

bf_image=Image.open(my_image_url)
gf_image=Image.open(selected)
couple_image=Image.new("RGB",(bf_image.width+gf_image.width,bf_image.height))
couple_image.paste(bf_image,(0,0))
couple_image.paste(gf_image,(bf_image.width,0))
couple_image.show()