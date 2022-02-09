import os
import re
import filecmp


def check_duplicate(duplicated_file_path: str):
    dir_path, filename = os.path.split(duplicated_file_path)
    short_file_name = re.search('duplicate_time.struct_time\(.*\)_(.*\....)', filename, re.IGNORECASE)

    if short_file_name:
        short_name = short_file_name.group(1)
        original_path = os.path.join(dir_path, short_name)

        #rint('comparing', original_path, duplicated_file_path)
        return filecmp.cmp(original_path, duplicated_file_path)
    return False


def check_all_duplicate(input_folder: str):
    for root, dirs, files in os.walk(input_folder):
        for name in files:
            if str(name).startswith('duplicate_time'):
                file_path = os.path.join(root, name)
                if check_duplicate(file_path):
                    os.remove(file_path)
                    print('Delete',file_path)


TEST_PATH = '/media/nas/01-Photos/'

check_all_duplicate(TEST_PATH)
