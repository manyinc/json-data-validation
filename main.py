import json
import csv
import subprocess
import os
import time

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

    if iteration == total: 
        print()

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

def validate_line(temp_filename):
    try:
        subprocess.run(['python', '-m', 'json.tool', temp_filename], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "Valid JSON"
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

def gen_raport(save_file_path, csv_file_path, delimiter):
    with open(save_file_path, 'w', encoding='utf-8') as rjvi:
        line_num = 1


        with open(csv_file_path, 'r', encoding='utf-8') as fp:
            for file_line_count in enumerate(fp):
                pass
        fp.close()
        file_line_count = file_line_count[0]
        i = 1
        printProgressBar(0, file_line_count, prefix = 'Progress:', suffix = 'Complete', length = 50)


        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            
            for line in reader:
                

                printProgressBar(i + 1, file_line_count, prefix = 'Progress:', suffix = 'Complete', length = 50)
                i = i + 1

                id_line = line["id"]
                json_data = line["data"]
                isValid = validateJSON(json_data)
                
                if not isValid:
                    if len(json_data.strip()) == 0:
                        rjvi.writelines("#######################################################################################\n")
                        rjvi.writelines(f"\n---> Line num: {line_num}\n---> Is validate: {isValid}\n---> Line_id: {id_line}\n---> Line_value: \nEmpty\n\n")
                    else:
                        temp_file_name = "json_temp.txt"
                        with open(temp_file_name, 'w', encoding='utf-8') as temp:
                            temp.writelines(json_data)
                        temp.close()
                        response_json = validate_line(temp_file_name)
                        response_json = response_json.replace("\n" , "")
                        rjvi.writelines("#######################################################################################\n")
                        rjvi.writelines(f"\n---> Line num: {line_num}\n---> Is validate: {isValid}\n---> Line_id: {id_line}\n---> Error_msg: {response_json}---> Line_value: \n{json_data}\n\n")

                line_num += 1
        file.close()
        rjvi.writelines("#######################################################################################\n")
    rjvi.close()
    os.system('cls')
    print(f"------------> Raport saved in {save_file_path} <------------")

if __name__ == "__main__":
    csv_file_path = 'json-err.json'
    delimiter = "	"
    save_file_path = "return_json_valid_info.txt"
    
    gen_raport(save_file_path, csv_file_path, delimiter)
