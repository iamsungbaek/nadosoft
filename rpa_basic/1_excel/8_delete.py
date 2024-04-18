from openpyxl import load_workbook
wb = load_workbook("Sample2.xlsx")
ws = wb.active

#ws.delete_rows(8) # 8번째 줄 삭제 한줄삭제
#ws.delete_rows(8,3) # 8번째 줄부터 3줄 삭제


#ws.delete_cols(2) # B열 줄 삭제 한열삭제
ws.delete_cols(2,3) # B열부터 3줄 삭제


#wb.save("sample_delete_rows.xlsx")
wb.save("sample_delete_cols.xlsx")