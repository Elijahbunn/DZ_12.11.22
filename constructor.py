import EXWriting
import md_writer
import excel_and_text
import number_charact

def character_creater():
    vn_result = []
    excel_and_text.exAndTxtCreat(vn_result)
    vn_result = excel_and_text.exAndTxtCreat(vn_result)

    number_charact.number_charactristic(vn_result)
    EXWriting.Excel_file_writing(vn_result)
    md_writer.text_md(vn_result)