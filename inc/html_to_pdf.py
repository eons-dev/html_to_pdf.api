import logging
import apie
import pdfkit

class html_to_pdf(apie.Endpoint):
    def __init__(this, name="API Endpoint for any Operation"):
        super().__init__(name)


    # Required Endpoint method. See that class for details.
    def GetHelpText(this):
        return f'''\
            '''

    def Call(this):
        pdfkit.from_url('https://westernforbs.org/species/dieteria-machaeranthera-canescens-hoary-tansyaster/','hoary.pdf')