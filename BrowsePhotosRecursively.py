import os
import time
from PIL import Image
from PIL.ExifTags import TAGS
import sys

ROOT_PATH = '/home/morvan/Images'
ROOT_PATH = '/media/nas/XX - Archives'
rootPath = os.path.abspath(ROOT_PATH)


for root, dirs, files in os.walk(rootPath):
    for name in files:

        if name.endswith((".jpg", ".png", "*.jpeg")):
            try:
                path_to_file=os.path.join(root,name)
                ti_m = os.path.getctime(path_to_file)
                m_ti = time.ctime(ti_m)
                t_obj = time.strptime(m_ti)

                T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)

                print('Image :', name,"in",root,"Date :", T_stamp)
                image = Image.open(path_to_file)

                exifdata = image.getexif()
                for tag_id in exifdata:
                    # get the tag name, instead of human unreadable tag id
                    tag = TAGS.get(tag_id, tag_id)
                    data = exifdata.get(tag_id)
                    # decode bytes
                    if isinstance(data, bytes):
                        data = data.decode()
                    print(f"{tag:25}: {data}")

            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
                print("Next entry.")
                print()


