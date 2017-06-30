import os
import re


def search_directory(path, ext=None):
    directory_structure = dict()
    try:
        regex = re.compile(ext, re.IGNORECASE | re.DOTALL)
    except:
        # when compile regex pattern error, assign None
        regex = None

    for dirName, subdirList, fileList in os.walk(path, topdown=True):
        directory_structure[dirName] = list()
        for filename in fileList:
            if regex:
                matched = regex.match(filename)
                # if matched(=None) -> else:
                if matched:
                    directory_structure[dirName].append(os.path.join(dirName, filename))
            else:
                # if there is no regex pattern, ignore ext variables
                directory_structure[dirName].append(os.path.join(dirName, filename))
    return directory_structure


def get_file_list(path, ext=None):
    file_list = list()
    try:
        regex = re.compile(ext, re.IGNORECASE | re.DOTALL)
    except:
        regex = None

    for filename in os.listdir(path):
        if regex:
            matched = regex.match(filename)
            if matched:
                file_list.append(os.path.join(path, filename))
        else:
            file_list.append(os.path.join(path, filename))
    return file_list
