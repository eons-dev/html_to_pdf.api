import logging
import apie
import pdfkit
from pathlib import Path

class html_to_pdf(apie.Endpoint):
    def __init__(this, name="HTML to PDF Converter"):
        super().__init__(name)
        this.mime="application/pdf"
        this.supportedMethods=["GET"]
        this.requiredKWArgs.append("url")
        this.requiredKWArgs.append("file_name")
        this.staticKWArgs.append("tmp_dir")

    # Required Endpoint method. See that class for details.
    def GetHelpText(this):
        return f'''\
Convert a webpage to a PDF document.
For example: curl 'https://eons.sh/html_to_pdf?url=https://westernforbs.org/species/dieteria-machaeranthera-canescens-hoary-tansyaster/&file_name=hoary.pdf' -o hoary.pdf
'''
    def Call(this):
        tmpFile = Path(this.tmp_dir).joinpath(this.file_name)
        logging.debug(f"Writing {tmpFile}")
        pdfkit.from_url(this.url, tmpFile)
        fileData = open(tmpFile, mode="rb")
        logging.debug(f"Reading {tmpFile}") 
        this.response.content.string = fileData.read()
        fileData.close()
        this.response.headers["Content-Disposition"] = f"attachment; filename={this.file_name}"