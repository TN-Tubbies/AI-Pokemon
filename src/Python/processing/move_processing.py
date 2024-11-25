import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas
from classes.move import Move
from data.get_function_from_code import get_function_from_code

column_names_list = ["Type","Catégorie","Puissance","Précision","PP","Target",
                     "Effect Probability","Contact?","Protect?","Mirrored?","Priority", "Function Code"]

def get_move_dict(language:str)->dict[str,Move]:
    if language == "en":
        column_names_list.append("Name")
    elif language == "fr":
        column_names_list.append("Name (Fr)")
    else:
        raise ValueError("Invalid language. Supported languages are 'en' and 'fr'.")

    res = {}

    file_path = "databases/move_database.xlsx"
    original_data = pandas.read_excel(file_path,header=0)
    move_amounts = len(original_data["Name"])
    data = [{} for i in range(move_amounts)]

    for row_id in range(move_amounts):
        for column_name in column_names_list:
            if column_name in ["Puissance", "Précision", "PP", "Priority"]:
                if str(original_data[column_name][row_id]) == "nan":
                    data[row_id][column_name] = None
                else:
                    data[row_id][column_name] = int(original_data[column_name][row_id])
            elif column_name == "Function Code":
                data[row_id]["Function"] = get_function_from_code(original_data[column_name][row_id])
            else:
                data[row_id][column_name] = original_data[column_name][row_id]

    for move in data:
        if language == "en":
            move_obj = Move(move["Name"], move["Type"], move["Puissance"], move["Précision"],
                            move["Catégorie"], move["PP"], move["Target"], data[row_id]["Function"], move["Priority"],
                            move["Contact?"], move["Protect?"], move["Mirrored?"])
            res[move["Name"]] = move_obj

        elif language == "fr":
            move_obj = Move(move["Name (Fr)"], move["Type"], move["Puissance"], move["Précision"],
                            move["Catégorie"], move["PP"], move["Target"], data[row_id]["Function"], move["Priority"],
                            move["Contact?"], move["Protect?"], move["Mirrored?"])
            res[move["Name (Fr)"]] = move_obj

    return res

if __name__ == "__main__":
    move_dict = get_move_dict("fr")
    print(move_dict)