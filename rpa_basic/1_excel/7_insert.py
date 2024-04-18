from openpyxl import load_workbook
wb = load_workbook("Sample2.xlsx")
ws = wb.active #현재 활성화된 시트가져오기

#ws.insert_rows(8) # 엑셀에서 행 삽입하기(8번째 줄 삽입됨)
#ws.insert_rows(8,5) # 엑셀에서 행 삽입하기(8번째 줄 위치에서 5줄 추가)
#ws.insert_cols(2) # B열 추가
ws.insert_cols(2,3) # B열 위치 부터 3열 추가


#wb.save("sample_insert_rows.xlsx")
wb.save("sample_insert_cols.xlsx")
