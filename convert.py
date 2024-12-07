from markdown_pdf import MarkdownPdf, Section
from gather_files import exclude_files, findMdFiles, createUniqueMdFile

#VARIABLES
file_name_without_extention = "Documentation"
md_file_name = file_name_without_extention + ".md"
pdf_file_name = file_name_without_extention + ".pdf"


all_my_md_files = findMdFiles()                                             #Search for all .md file
my_md_files = exclude_files(files_list=all_my_md_files)                     #Exlude some file if needed
createUniqueMdFile(file_list=my_md_files, my_file_name=md_file_name)        #Create a unique .md file

pdf = MarkdownPdf(toc_level=False)
pdf.add_section(Section(open(md_file_name, encoding='utf-8').read()))
pdf.meta["title"] = "MarkdownPdf module"                                    
pdf.save("pdf_documentation/" + pdf_file_name)                              #Pdf creation