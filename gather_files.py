import glob
import os


def findMdFiles(search_criteria: str = "./**/*.md") -> list:
    """Search all files with .md extensions in current path and sub paths.

    Args:
        search_criteria (str, optional): Search criteria. Defaults to './**/*.md'.

    Returns:
        list: path to files which fit the search
    """
    files = glob.glob(search_criteria, recursive=True)
    return files


def getValueToExcludeFromEnvVar() -> list:
    """Read values from TO_EXCLUDE env var, create a list with a split by "," identification.
    Example: export TO_EXCLUDE="README.md, REAMDE2.md"

    Returns:
        list: Contain all values read from TO_EXCLUDE env var.
    """

    value_to_exclude_from_env = os.getenv("TO_EXCLUDE")  # Get values from Env var

    if value_to_exclude_from_env:
        values_to_exclude = value_to_exclude_from_env.split(",")
    else:
        values_to_exclude = []

    return values_to_exclude


def exclude_files(files_list: list, values_to_exclude: list = []) -> list:
    """Remove items from a list by searching keywords.

    Args:
        files_list (list): Liste with all items.
        values_to_exclude (list, optional): keywork that will be compare with item names. Defaults to [].

    Returns:
        list: _description_
    """
    filtered_list = [
        file
        for file in files_list
        if not any(word in file for word in values_to_exclude)
    ]
    return filtered_list


def createUniqueMdFile(file_list: list, my_file_name: str):
    """Will merge all ".md" files from input in only one ".md" file.

    Args:
        file_list (list): Liste with path and files names that are going to be merge in 1 md file.
        my_file_name (str): created new .md file name that contain all ".md" files merged.
    """
    with open(my_file_name, "w", encoding="utf-8") as fout:
        for file_path in file_list:
            with open(file_path, encoding="utf-8") as fin:
                fout.write(fin.read())
                fout.write("\n")  # Add line break betweend each files.
