import glob

def findMdFiles(search_criteria: str ='./**/*.md')-> list:
    files = (glob.glob(search_criteria, recursive=True))
    return files

def exclude_files(files_list: list, files_to_exlude: list =[])-> list:
    filtered_list = [file for file in files_list 
                        if not any(word in file for word in files_to_exlude)]
    return filtered_list

def createUniqueMdFile(file_list: list, my_file_name: str):
    with open(my_file_name, 'w', encoding='utf-8') as fout:
        for file_path in file_list:
            with open(file_path, 'r', encoding='utf-8') as fin:
                fout.write(fin.read())
                fout.write('\n')