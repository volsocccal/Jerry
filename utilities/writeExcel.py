import pandas as pd
from pandas import ExcelWriter
pd.options.mode.chained_assignment = None  # default='warn'
import os
from os import path

def write_excel(df: pd.DataFrame, output_path: str, file_name: str, title: str, sheet_name: str, write_title_flag: bool, overwriteIfExist: bool, createIfEmpty: bool, landscape_layout: bool):

    # Remove Duplicate Lines
    df_noduplicate = df.drop_duplicates()
    
    # Create output_path if it doesn't exists
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    
    # Full Path
    full_output_path = output_path + "/" + file_name
    if os.path.exists(full_output_path):
        if not overwriteIfExist: # Delete existing file
            os.remove(full_output_path)

    # Check if the dataset is empty
    if df.empty():
        if not createIfEmpty:
            return 
            
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(full_output_path, engine='xlsxwriter', datetime_format='dd / mmm / yyyy', date_format='dd / mmmm / yyyy')

    # Convert the dataframe to an XlsxWriter Excel object.
    if write_title_flag:
        df_noduplicate.to_excel(writer, sheet_name, index=False, startrow=3, header=False)
    else:
        df_noduplicate.to_excel(writer, sheet_name, index=False, startrow=1, header=False)

    # Add Header
    workbook  = writer.book
    worksheet = writer.sheets[sheet_name]
    if write_title_flag:
        worksheet.repeat_rows(2)
    else:
        worksheet.repeat_rows(0)
    worksheet.set_paper(9) # 9 = A4 format
    header_format = workbook.add_format()
    header_format.set_align('left')
    header_format.set_align('vcenter')
    header_format.set_bold(True)
    header_format.set_underline(True)
    header_format.set_border(0)
    if (landscape_layout):
        worksheet.set_landscape()

    # Add Title
    if write_title_flag:
        worksheet.write(0, 0, title, header_format)

    # Write the column headers with the defined format.
    header_format.set_align('center')
    header_format.set_border(6) # Double Border
    header_format.set_underline(False)
    for col_num, value in enumerate(df.columns.values):
        if write_title_flag:
            worksheet.write(2, col_num, value, header_format)
        else:
            worksheet.write(0, col_num, value, header_format)

    # Iterate through each column and set the width == the max length in that column.
    # A padding length of 4 is also added.
    worksheet = writer.sheets[sheet_name]
    cell_format = workbook.add_format()
    cell_format.set_align('center')
    cell_format.set_align('vcenter')
    cell_format.set_border()
    for idx, col in enumerate(df):  # loop through all columns
        series = df[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            )) + 4  # adding a little extra space
        worksheet.set_column(idx, idx, max_len, cell_format)  # set column width
    worksheet = writer.sheets[sheet_name]

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()