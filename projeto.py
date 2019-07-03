import xml.etree.cElementTree as ET

def createStandardReport():
    report = ET.Element("report", xmlns = "http://www.eclipse.org/birt/2005/design", version = "3.2.23", id = "1")
    createStandardReportPropertyReport(report)
    createStandardReportStyles(report)
    createStandardReportPageSetup(report)
    tree = ET.ElementTree(report)
    tree.write(getReportName(), xml_declaration = True, encoding = "UTF-8", method = "xml")
    
def createStandardReportPropertyReport(report):
    ET.SubElement(report, "property", name = "createdBy").text = "Eclipse BIRT Designer Version <4.4.0.v201405191524 Build &lt;4.4.0.v20140606-1451>"
    ET.SubElement(report, "property", name = "units").text = "in"
    ET.SubElement(report, "property", name = "iconFile").text = "/templates/blank_report.gif"
    ET.SubElement(report, "property", name = "bidiLayoutOrientation").text = "ltr"
    ET.SubElement(report, "property", name = "imageDPI").text = "96"

def createStandardReportStyles(report):
    styles = ET.SubElement(report, "styles")
    createStandardReportStylesStyleReport(styles)
    createStandardReportStylesStyleCrosstab(styles)
    createStandardReportStylesStyleCrosstabCell(styles)

def createStandardReportStylesStyleReport(styles):
    style = ET.SubElement(styles, "style", name = "report", id = "4")
    createStandardReportStylesStyleReportProperty(style)

def createStandardReportStylesStyleReportProperty(style):
    ET.SubElement(style, "property", name = "fontFamily").text = "sans-serif"
    ET.SubElement(style, "property", name = "fontSize").text = "10pt"

def createStandardReportStylesStyleCrosstab(styles):
    style = ET.SubElement(styles, "style", name = "crosstab", id = "5")
    createStandardReportStylesStyleCrosstabProperty(style)

def createStandardReportStylesStyleCrosstabProperty(style):
    ET.SubElement(style, "property", name = "borderBottomColor").text = "#CCCCCC"
    ET.SubElement(style, "property", name = "borderBottomStyle").text = "solid"
    ET.SubElement(style, "property", name = "borderBottomWidth").text = "1pt"
    ET.SubElement(style, "property", name = "borderLeftColor").text = "#CCCCCC"
    ET.SubElement(style, "property", name = "borderLeftStyle").text = "solid"
    ET.SubElement(style, "property", name = "borderLeftWidth").text = "1pt"
    ET.SubElement(style, "property", name = "borderRightColor").text = "#CCCCCC"
    ET.SubElement(style, "property", name = "borderRightStyle").text = "solid"
    ET.SubElement(style, "property", name = "borderRightWidth").text = "1pt"
    ET.SubElement(style, "property", name = "borderTopColor").text = "#CCCCCC"
    ET.SubElement(style, "property", name = "borderTopStyle").text = "solid"
    ET.SubElement(style, "property", name = "borderTopWidth").text = "1pt"

def createStandardReportStylesStyleCrosstabCell(styles):
    style = ET.SubElement(styles, "style", name = "crosstab-cell", id = "6")
    createStandardReportStylesStyleCrosstabCellProperty(style)

def createStandardReportStylesStyleCrosstabCellProperty(style):
    ET.SubElement(style, "property", name = "borderBottomColor").text = "#CCCCCC"
    ET.SubElement(style, "property", name = "borderBottomStyle").text = "solid"
    ET.SubElement(style, "property", name = "borderBottomWidth").text = "1pt"
    ET.SubElement(style, "property", name = "borderLeftColor").text = "#CCCCCC"
    ET.SubElement(style, "property", name = "borderLeftStyle").text = "solid"
    ET.SubElement(style, "property", name = "borderLeftWidth").text = "1pt"
    ET.SubElement(style, "property", name = "borderRightColor").text = "#CCCCCC"
    ET.SubElement(style, "property", name = "borderRightStyle").text = "solid"
    ET.SubElement(style, "property", name = "borderRightWidth").text = "1pt"
    ET.SubElement(style, "property", name = "borderTopColor").text = "#CCCCCC"
    ET.SubElement(style, "property", name = "borderTopStyle").text = "solid"
    ET.SubElement(style, "property", name = "borderTopWidth").text = "1pt"

def createStandardReportPageSetup(report):
    pageSetup = ET.SubElement(report, "page-setup")
    createStandardReportPageSetupSimpleMasterPage(pageSetup)

def createStandardReportPageSetupSimpleMasterPage(pageSetup):
    simpleMasterPage = ET.SubElement(pageSetup, "simple-master-page", name = "Simple MasterPage", id = "2")
    createStandardReportPageSetupSimpleMasterPagePageFooter(simpleMasterPage)

def createStandardReportPageSetupSimpleMasterPagePageFooter(simpleMasterPage):
    pageFooter = ET.SubElement(simpleMasterPage, "page-footer")
    createStandardReportPageSetupSimpleMasterPagePageFooterText(pageFooter)

def createStandardReportPageSetupSimpleMasterPagePageFooterText(pageFooter):
    text = ET.SubElement(pageFooter, "text", id = "3")
    createStandardReportPageSetupSimpleMasterPagePageFooterTextProperty(text)
    
def createStandardReportPageSetupSimpleMasterPagePageFooterTextProperty(text):
    ET.SubElement(text, "property", name = "contentType").text = "html"
    ET.SubElement(text, "text-property", name = "content").text = "<![CDATA[<value-of>new Date()</value-of>]]>"

def getReportName():
    reportName = []
    reportName.append(input("Qual será o nome do relatório: "))
    reportName.append(".rptdesign")
    reportName = ''.join(reportName)
    return reportName

def main():
    createStandardReport()


if __name__ == "__main__":
    main()
