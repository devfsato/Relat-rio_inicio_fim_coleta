import conexao_bd

conexao_bd.listar()
print(conexao_bd)

import xlwt
from datetime import datetime, timedelta

##style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
##    num_format_str='#,##0.00')

style0 = xlwt.easyxf('font: name Times New Roman, color-index blue, bold on, size 12')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

data1 = (datetime.now() - timedelta(days=1))
data1format = data1.strftime("%d%m%Y")

data2 = datetime.now()
data2format = data2.strftime("%d%m%Y")

print(data1format)

##wb = "Documents\teste_excel"
wb = xlwt.Workbook()
ws = wb.add_sheet('Teste')

ws.write(0, 0, "Setor", style0)
ws.write(0, 1, "Prefixo", style0)
ws.write(0, 2, "Unidade", style0)
ws.write(0, 3, "data", style0)
##ws.write(1, 0, datetime.now(), style1)
ws.write(1, 0, 1)
ws.write(1, 1, 1)
ws.write(1, 2, 1)
ws.write(1, 3, xlwt.Formula("B2:B3"))

wb.save('{}_{}.xls'.format(data1format,data2format))
