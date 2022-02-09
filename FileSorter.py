# Basic analyse
import filecmp
import os.path
import time
import uuid
from datetime import datetime

from PIL import Image


def scan_image_folder(input_folder: str, output_folder: str):
    for root, dirs, files in os.walk(input_folder):
        for name in files:
            file_path = os.path.join(root, name)
            # print("File %s :" % file_path)
            # print("> Last modified: %s" % time.ctime(os.path.getmtime(file_path)))
            # print("> Created: %s" % time.ctime(os.path.getctime(file_path)))
            try:
                img = Image.open(file_path)
                # print("> Format is %s" % img.format)
                treat_image(file_path, output_folder)
            except Exception as reason:

                print("> Not an image! ", reason)

        # for name in dirs:
        #    print("\n jumping to %s" % os.path.join(root, name))


def treat_image(image_path: str, output_folder: str):
    # print("Processing image %s ..." % image_path)

    modification_date: time = time.ctime(os.path.getmtime(image_path))
    date_of_modification = datetime.strptime(modification_date, "%a %b %d %H:%M:%S %Y")  # Convert string to date format
    day: str = date_of_modification.day
    month: str = date_of_modification.month
    year: str = date_of_modification.year
    try:
        root_dir = os.path.abspath(output_folder)
        target_folder = os.path.join(root_dir, str(year), str(month))
        # print('should create', target_folder)
        os.makedirs(target_folder, exist_ok=True)

        target_file = os.path.join(target_folder, os.path.basename(image_path))

        skip_file = False

        if os.path.exists(target_file):
            if filecmp.cmp(image_path, target_file):
                skip_file = True
                print('Info duplicated file will be skipped:' + target_file)

            else:
                unique_id = uuid.uuid4()
                new_file_mane = 'duplicate_' + str(unique_id) + '_' + os.path.basename(image_path)
                target_file = os.path.join(target_folder, new_file_mane)
                print('Warning different file - similar name :' + target_file)

        if not skip_file:
            print('Moving', image_path, 'to', target_file)
            os.rename(image_path, target_file)
        else :
            os.remove(image_path)



    except Exception as err:
        print('cannot create', target_folder, 'because', err)


# Main part

scanned_folder: str = '/media/nas/XX-Bordel/photos_restaurees'
collection_folder: str = '/media/nas/01-Photos'

scan_image_folder(scanned_folder, collection_folder)
