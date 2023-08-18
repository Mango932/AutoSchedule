from openpyxl import Workbook, load_workbook

wb = load_workbook('ScheduleMrLube.xlsx')
ws = wb.active
print(ws)

wb.save('ScheduleMrLube.xlsx')