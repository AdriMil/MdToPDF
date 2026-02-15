# Convert your markdown files into PDF

The [convert.py file](convert.py) will call [functions](gather_files.py) to find all ".md" files from a path and subpath. All detected .md files will be gather and merge in only one ".md" file. Then this new .md file will be converted in a pdf file.

## Build docker container

You will find the [dockerfile here](dockerfile) used to build the image.

**Build docker image** \
` docker build -t md_to_pdf .`

**Run the container** \
`docker run --name ConvertMdToPdf -it --rm -v .:/app/pdf_documentation  md_to_pdf:latest`\
**Comment:** A volume is used to mount wihtin the container your .md files that you want convert into pdf. As result, the generated .pdf file will be save inside the container in path */app/pdf_documentation*. Thanks to this volume you will be able to get the generated .pdf file.

**Add personnalized style to the generated Documentation** \
You can load custome colors for titles sections to the generated pdf. \
You must add a `style.css` file when running the container using a volume `-v ./style.css:/app/style.css`, example:

`docker run --name ConvertMdToPdf -it --rm -v .:/app/pdf_documentation -v ./style.css:/app/style.css md_to_pdf:latest;`

**Add extra env var**
* DEBUG: If DEBUG is not empty (no matter the value), debug will be activated and some prompts will appears.
* TO_EXCLUDE: Files names that you do not want add in the generated pdf. 
* FILE_NAME: Name of the generated files (.md and .pdf). Do not add extension. Default value is "Documentation".

Command example with these var env: \
`docker run --name ConvertMdToPdf -it --rm -v .:/app/pdf_documentation -e DEBUG=True  -e TO_EXCLUDE="README,test.md" -e FILE_NAME="MyFileName" md_to_pdf:latest`

## Push docker image to GitHub registry

**Build docker image** \
From [github repository](https://github.com/AdriMil/MdToPDF/pkgs/container/mdtopdf/versions), check last version available. You will need to up the version. Then build image using this name: \
`docker build -t ghcr.io/<Github_User_Name>/mdtopdf:<verison> .` \
*Example:* `docker build -t ghcr.io/adrimil/mdtopdf:0.0.5 .`

**Add a token** \
Create a token from GitHub settings with read and write rights.

**Connect to github image registry** \
`echo <TOKEN> | docker login ghcr.io -u adrimil --password-stdin`

**Push your image to the registry** \
`docker push ghcr.io/<Github_User_Name>/mdtopdf:<verison>` \
*Example:* `docker push ghcr.io/adrimil/mdtopdf:0.0.5`