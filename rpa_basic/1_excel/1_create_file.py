from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "NadoSheet"
wb.save("Sample1.xlsx")
wb.close()