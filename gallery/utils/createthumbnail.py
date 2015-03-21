__author__ = 'clint'

from PIL import Image, ImageOps
import os

ACCEPTED_EXTENSIONS = ('jpg','jpeg','png','gif')

def thumb_all(root):
    for i in os.listdir(root):
        if i.lower().endswith(ACCEPTED_EXTENSIONS):
            size = (128, 128)
            image = Image.open(os.path.join(root, i))
            thumb = ImageOps.fit(image, size, Image.ANTIALIAS)
            if not os.path.exists(os.path.join(root, '%s_thumb.jpg' % (i))):
                thumb.save(os.path.join(root, '%s_thumb.jpg' % (os.path.splitext(i)[0])))
                print "Created '%s'" % ('%s_thumb.jpg' % (os.path.splitext(i)[0]))

if __name__ == '__main__':
    thumb_all(r'../gallery/Colombia')