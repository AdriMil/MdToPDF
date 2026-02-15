from markdown_pdf import MarkdownPdf, Section

from functions import debug, fileName
from gather_files import (createUniqueMdFile, exclude_files, findMdFiles,
                          getValueToExcludeFromEnvVar)

debug_level = debug()

# VARIABLES
file_name_without_extention = fileName()
md_file_name = file_name_without_extention + ".md"
pdf_file_name = file_name_without_extention + ".pdf"

if debug_level:
    print("Unique .md file be created with name: " + md_file_name)
    print("Unique .pdf file be created with name: " + pdf_file_name)

all_my_md_files = findMdFiles()  # Search for all .md file
excluded_files = getValueToExcludeFromEnvVar()

if debug_level:
    print("Next files will be exluded:")
    print(excluded_files)

my_md_files = exclude_files(
    files_list=all_my_md_files, values_to_exclude=excluded_files
)  # Exlude some file if needed

if debug_level:
    print("Next files will be merged in one .md file:")
    print(my_md_files)

createUniqueMdFile(
    file_list=my_md_files, my_file_name=md_file_name
)  # Create a unique .md file

# Load CSS file if exists to apply custom styles to the PDF output. If the file is not found, proceed without custom styles.
try:
    with open("style.css", "r", encoding="utf-8") as f:
        css = f.read()
        if debug_level:
            print("CSS file loaded successfully.")
except FileNotFoundError:
    css = ""  # If no CSS file is found, use an empty string as default
    if debug_level:
        print("CSS file not found. Proceeding without custom styles.")

pdf = MarkdownPdf(toc_level=False)
pdf.add_section(
    Section(
        open(md_file_name, encoding="utf-8").read()
    ),
    user_css=css  # Apply custom CSS styles to the PDF output if provided 
)
pdf.meta["title"] = "MarkdownPdf module"
pdf.save("pdf_documentation/" + pdf_file_name)  # Pdf creation
