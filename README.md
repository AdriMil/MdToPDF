# Convert your markdown file into PDF

## Build docker container

**Build docker image** \
` docker build -t md_to_pdf .` \

**Run the container** \
`docker run --name ConvertMdToPdf -it --rm -v .:/app/pdf_documentation  md_to_pdf:latest`\
**Comment:** final pdf will be save inside container on path */app/pdf_documentation*. Then a volume is mounted to be able to get this pdf.  This volume is use to add inside the container the .md files that you want convert into pdf.

**Add extra env var**
* DEBUG: If DEBUG is not empty (no matter the value), debug will be activated and some prompt will appears.
* TO_EXCLUDE: Add words or files names to exclude from the convertion. 
* FILE_NAME: file name used for created files (.md and .pdf). Do not add extension. If not defined, default value is "Documentation".

Command example with these var env: \
`docker run --name ConvertMdToPdf -it --rm -v .:/app/pdf_documentation -e DEBUG=True  -e TO_EXCLUDE="README,test.md" -e FILE_NAME="MyFileName" md_to_pdf:latest`

