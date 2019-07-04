# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import sys

version = float(str(sys.version_info[0]) + '.' + str(sys.version_info[1]))

def getReportName():
    reportName = []
    if version <= 2.7:
        reportName.append(raw_input("Qual será o nome do relatório: "))
    else:
        reportName.append(input("Qual será o nome do relatório: "))
    reportName.append(".rptdesign")
    reportName = ''.join(reportName)
    return reportName

def main():
    reportName = getReportName()
    if version <= 2.7:
        reportTitle = raw_input("Qual será o título do relatório: ").decode("utf-8")
    else:
        reportTitle = input("Qual será o título do relatório: ")
    reportTree = ET.parse('layout.rptdesign')
    report = reportTree.getroot()
    textProperty = report.find('page-setup/simple-master-page/page-header/text/text-property')
    textProperty.text = reportTitle
    reportTree = ET.ElementTree(report)
    reportTree.write(reportName, xml_declaration = True, encoding = "utf-8", method = "xml")

if __name__ == '__main__':
    main()