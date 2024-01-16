
# importing xlwt module 
import xlwt 
  
workbook = xlwt.Workbook()  
  
sheet = workbook.add_sheet("Sheet Name") 
  
# Applying multiple styles 
style = xlwt.easyxf('font: bold 1, color red;') 
  
# Writing on specified sheet 
sheet.write(0, 0, 'SAMPLE', style) 
sheet.write(2, 2, 'test 1', style) 
sheet.write(3, 2, 'test 2', style) 
  
workbook.save("sample.xls") 