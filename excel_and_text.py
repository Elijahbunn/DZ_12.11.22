import xlrd 
import random 
import pandas as pd
import numpy as np
import pyexcel
import number_charact

def exAndTxtCreat(vn_result):
    df1 = pd.read_excel("Данные1.xlsx", sheet_name=0)
    df2 = pd.read_excel("Данные2.xlsx", sheet_name=0)

    list1 = list(df1['name'].dropna()) 
    list2 = list(df1['surname'].dropna())
    list3 = list(df1['species'].dropna())
    print(list1, list2, list3)

    list4 = list(df2['age'].dropna())
    list5 = list(df2['height'].dropna())
    list6 = list(df2['clothes'].dropna())
    list7 = list(df2['FeaturesFace'].dropna())
    list8 = list(df2['АhysiqueFeatures'].dropna())

    random.shuffle(list1)
    random.shuffle(list2)
    random.shuffle(list3)
    # random.sample(list3, len(list3))
    random.shuffle(list4)
    random.shuffle(list5)
    random.shuffle(list6)
    random.shuffle(list7)
    random.shuffle(list8)
    # list2.extend([list3])

    # l3= list3.remove(np.nan)
    # print(list3)

    record = zip(list1, list2, list3, list4, list5, list6, list7, list8)
    record3 = zip(list1, list2, list3, list4, list5, list6, list7, list8)
    result = list(record3)
    vn_result = list(result[0])
    
    # print(list(record))

    with open("Общий список без переносов.txt", "w") as file:
            ToFile=(list(record))
            for i in range(len(ToFile)):
                ToFile[i] = list(ToFile[i])
                number_charact.number_charactristic(ToFile[i])
            print(ToFile)
            print(*ToFile, file=file)    

    # Get the data

    df = pd.DataFrame(ToFile).T
    df.to_excel(excel_writer = "Общая таблица персонажей.xlsx")
    # Save the array to a file
    # pyexcel.save_as(array=list1, dest_file_name="result.xls")

    
    # Пишем в файл без скобок, каждый список начинается с новой строки
    record1 = zip(list1, list2, list3, list4, list5, list6, list7, list8)
    with open("Общий список с переносами.txt", "w") as file1:
        for SaveToFileOne in (record1):
            #print(f' THIS IS SaveToFileOne: {SaveToFileOne}')
            ToFile1 = (list(SaveToFileOne))
            number_charact.number_charactristic(ToFile1)
            print(ToFile1)  
            # for height, FeaturesFace, АhysiqueFeatures in zip(list5, list6, list7):
            #     print(height, FeaturesFace, АhysiqueFeatures )
            #     ToFile=(ToFile, height, FeaturesFace, АhysiqueFeatures )
            print(*ToFile1, file=file1)    

    return vn_result