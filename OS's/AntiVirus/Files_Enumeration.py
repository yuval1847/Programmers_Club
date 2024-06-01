import os
import itertools

def IsThereSubDirectories(filesList: list):
    # The function gets a list of files.
    # The function returns True if there are sub-directories in the given list, otherwise false.
    for i in filesList:
        if os.path.isdir(i):
            return True
    return False

def ObjectsInDirectory(folderToScan: str):
    # The function gets a string which represents a directory's path.
    # The function returns a list of all the files and sub-directories in the given directory.
    try:
        if os.path.exists(folderToScan):

            # Creating a list of all the files and directories in the given path
            filesList = os.listdir(folderToScan)

            # Add the full path for each file and directory.
            for i in range(len(filesList)):
                filesList[i] = folderToScan + "/" + filesList[i]

            return filesList
        
        else:
            return "Directory doesn't exist"
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def SearchFilesInSubDirectories(filesList: list):
    # The function gets a list of files and folders.
    # The function returns the given list after replacing any sub-directory with a list of the files inside it.
    while IsThereSubDirectories(filesList):
        new_files_list = []
        for item in filesList:
            if os.path.isdir(item):
                new_files_list.extend(ObjectsInDirectory(item))
            else:
                new_files_list.append(item)
        filesList = new_files_list
    return filesList

def FilesEnumeration(folderToScan: str):
    # The function gets a string which represents a directory's path.
    # The function returns a list of all the files in the given directory (including the sub-directories' files).
    print("DETECTING FILES...")

    # Checking if the given path exists.
    if not os.path.exists(folderToScan):
        print("The given path doesn't exist!")
        return []

    # Creating a list of all the files and directories in the given path
    filesList = ObjectsInDirectory(folderToScan)
    
    # Filter the files in the sub-directories
    filesList = SearchFilesInSubDirectories(filesList)

    print("FINISHED DETECTING")
    return filesList