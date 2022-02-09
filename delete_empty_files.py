import os
import re
import filecmp



def delete_all_empy(input_folder: str):
    for root, dirs, files in os.walk(input_folder):
        for name in files:
            file_path = os.path.join(root, name)
            #print(file_path,'->',os.stat(file_path).st_size)
            if os.stat(file_path).st_size == 0:
                os.remove(file_path)
                print('Deleted',file_path)


TEST_PATH = '/media/nas/XX-Bordel/'

delete_all_empy(TEST_PATH)
