# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET

def createStandardReport():
    report = ET.Element("report", xmlns = "http://www.eclipse.org/birt/2005/design", version = "3.2.23", id = "1")
    createStandardReportPropertyReport(report)
    createDataSource(report)
    createStandardReportStyles(report)
    createStandardReportPageSetup(report)
    return report

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
    reportName.append(raw_input("Qual será o nome do relatório: "))
    reportName.append(".rptdesign")
    reportName = ''.join(reportName)
    return reportName

def createDataSource(report):
    dataSource = ET.SubElement(report, "data-sources")
    createDataSourceOdaDataSource(dataSource)

def createDataSourceOdaDataSource(dataSource):
    odaDataSource = ET.SubElement(dataSource, "oda-data-source", extensionID = "org.eclipse.birt.report.data.oda.jdbc", name = "Data Source", id = "7")
    createDataSourceOdaDataSourceProperties(odaDataSource)

def createDataSourceOdaDataSourceProperties(odaDataSource):
    ET.SubElement(odaDataSource, "text-property", name = "displayName")
    listProperty = ET.SubElement(odaDataSource, "list-property", name = "privateDriverProperties")
    createDataSourceOdaDataSourcePropertiesListProperty(listProperty)
    ET.SubElement(odaDataSource, "property", name = "odaDriverClass").text = "oracle.jdbc.driver.OracleDriver"
    ET.SubElement(odaDataSource, "property", name = "odaURL").text = "jdbc:oracle:thin:@192.168.122.5:1521/PDBORCL"
    ET.SubElement(odaDataSource, "property", name = "odaUser").text = "vivo_sabor"
    ET.SubElement(odaDataSource, "encrypted-property", name = "odaPassword", encryptionID = "base64").text = "dGVrbmlzYQ=="

def createDataSourceOdaDataSourcePropertiesListProperty(listProperty):
    exProperty = ET.SubElement(listProperty, "ex-property")
    ET.SubElement(exProperty, "name").text = "metadataBidiFormatStr"
    ET.SubElement(exProperty, "value").text = "ILYNN"
    exProperty = ET.SubElement(listProperty, "ex-property")
    ET.SubElement(exProperty, "name").text = "disabledMetadataBidiFormatStr"
    exProperty = ET.SubElement(listProperty, "ex-property")
    ET.SubElement(exProperty, "name").text = "contentBidiFormatStr"
    ET.SubElement(exProperty, "value").text = "ILYNN"
    exProperty = ET.SubElement(listProperty, "ex-property")
    ET.SubElement(exProperty, "name").text = "disabledContentBidiFormatStr"

def main():
    report = createStandardReport()
    reportTree = ET.ElementTree(report)
    reportTree.write(getReportName(), xml_declaration = True, encoding = "UTF-8", method = "xml")

if __name__ == "__main__":
    main()
