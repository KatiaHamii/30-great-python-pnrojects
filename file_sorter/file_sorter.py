import  os
import shutil   #to move files around


def create_folder(path:str, extention:str) -> str:

    """Creates a folder that is named after the execution of the file passed in"""

    folder_name :str = extention[1:] #.png -> png
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def sort_files(source_path:str) :
    """Sorts files based on the given path"""

    for root_dir, sub_dir, filenames in os.walk(source_path):
        for  filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extention:str = os.path.splitext(filename)[1]  # if there is no extention -> return " "

            if extention:
                target_folder: str = create_folder(source_path, extention)
                target_path: str = os.path.join(target_folder, filename)
                shutil.move(file_path, target_path)


def remove_empty_folders(source_path:str):
    """Removes all empty folders"""

    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):  #True -> starts with root_dir, false -> starts with the last child
        for cur_dir in sub_dir:
            folder_path:str = os.path.join(root_dir, cur_dir)

            if not os.listdir(folder_path): # if it does not contain any elements inside
                os.rmdir(folder_path)


def main():
    user_input:str = input("Please provede a file path to sort: ")
    if os.path.exists(path=user_input):
        sort_files(user_input)
        remove_empty_folders(user_input)
        print("files sorted successfully")
    else:
        print("provide a valid file path")


if __name__ == "__main__":
    main()