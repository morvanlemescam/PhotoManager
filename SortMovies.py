import os


def browse_folder(input_folder: str, output_folder: str):
    for root, dirs, files in os.walk(input_folder):
        for name in files:

            file_path = os.path.join(root, name)
            filename, file_extension = os.path.splitext(file_path)
            dir_path, filename = os.path.split(file_path)

            if file_extension.upper() in ['.ZIP']:
                target_path = os.path.join(output_folder, filename)
                print('file extension ', file_path, '>>', target_path, '->', file_extension)
                #print(output_folder,filename,'>>', target_path, '->', file_extension)
                os.rename(file_path,target_path)

            else:
                print(file_path)



input_path = '/media/nas/XX-Bordel/photos_restaurees'
output_path = '/media/nas/ZZ-ZIP_Archives'
browse_folder(input_path, output_path)
