import glob

def findMdFiles(search_criteria: str ='./**/*.md')-> list:
    """Search all files with .md extensions in current path and sub paths.

    Args:
        search_criteria (str, optional): Search criteria. Defaults to './**/*.md'.

    Returns:
        list: path to files which fit the search
    """
    files = (glob.glob(search_criteria, recursive=True))
    return files

def exclude_files(files_list: list, files_to_exlude: list =[])-> list:
    """Revome froma a list some files by searching keyword. For example if you do not want include some ".md" file in the final pdf.

    Args:
        files_list (list): Liste with path and files names that are going to be merge in 1 md file.
        files_to_exlude (list, optional): keywork that will be search and delete from "files_list" list . Defaults to [].

    Returns:
        list: _description_
    """
    filtered_list = [file for file in files_list 
                        if not any(word in file for word in files_to_exlude)]
    return filtered_list

def createUniqueMdFile(file_list: list, my_file_name: str):
    """Will merge all ".md" files from input in only one ".md" file.

    Args:
        file_list (list): Liste with path and files names that are going to be merge in 1 md file.
        my_file_name (str): created new .md file name that contain all ".md" files merged.
    """
    with open(my_file_name, 'w', encoding='utf-8') as fout:
        for file_path in file_list:
            with open(file_path, 'r', encoding='utf-8') as fin:
                fout.write(fin.read())
                fout.write('\n')