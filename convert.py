from markdown_pdf import MarkdownPdf, Section
from gather_files import exclude_files, findMdFiles, createUniqueMdFile, getValueToExcludeFromEnvVar
from functions import debug, fileName

debug_level = debug()

#VARIABLES
file_name_without_extention=fileName()
md_file_name = file_name_without_extention + ".md"
pdf_file_name = file_name_without_extention + ".pdf"

if debug_level: 
    print("Unique .md file be created with name: " + md_file_name)
    print("Unique .pdf file be created with name: " + pdf_file_name)

all_my_md_files = findMdFiles()                                             #Search for all .md file
excluded_files=getValueToExcludeFromEnvVar()

if debug_level: 
    print("Next files will be exluded:"); 
    print(excluded_files)

my_md_files = exclude_files(files_list=all_my_md_files, values_to_exclude=excluded_files)                     #Exlude some file if needed

if debug_level: 
    print("Next files will be merged in one .md file:"); 
    print(my_md_files)

createUniqueMdFile(file_list=my_md_files, my_file_name=md_file_name)        #Create a unique .md file

pdf = MarkdownPdf(toc_level=False)
