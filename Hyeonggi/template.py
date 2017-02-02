'''
Created on Nov 18, 2016
Modified on Jan 25, 2017

@author: Hyeong-Gi Hong
'''
import os.path
import csv
import tkinter as tk
from tkinter.filedialog import askopenfilenames

def create_keys():
    """
    This function will generate keys (indicators)
    Keys format is:  number.letter.number
    """
    indicators =  ("0.b.",)
    
    for sec1 in range(1, 10):
        if sec1 == 1:
            for sec2 in range(97, 102):
                if chr(sec2) == "a":
                    for sec3 in range(1,4):
                        key = str(sec1) + "." + chr(sec2) + "." + str(sec3)
                        indicators += (key, )
                elif chr(sec2) == "c":
                    for sec3 in range(1,3):
                        key = str(sec1) + "." + chr(sec2) + "." + str(sec3)
                        indicators += (key, )
                else:
                    key = str(sec1) + "." + chr(sec2) + "."
                    indicators += (key, )
        
        if sec1 == 2:
            indicators += ("2.2.", "2.3.",)
            for sec2 in range(97,113):
                if chr(sec2) == "h" or chr(sec2) == "m":
                    for sec3 in range(1,5):
                        key = str(sec1) + "." + chr(sec2) + "." + str(sec3)
                        indicators += (key, )
                elif chr(sec2) == "i" or chr(sec2) == "n":
                    for sec3 in range(1,7):
                        if sec3 == 2:
                            continue
                        else:
                            key = str(sec1) + "." + chr(sec2) + "." + str(sec3)
                            indicators += (key, )
                else:
                    for sec3 in range(1,3):
                        key = str(sec1) + "." + chr(sec2) + "." + str(sec3)
                        indicators += (key, )
                    
        if sec1 == 3:
            for sec2 in range(97,100):
                key = str(sec1) + "." + chr(sec2) + "."
                indicators += (key, )
        
        if sec1 == 4 or sec1 == 5 or sec1 == 7:
            if sec1 == 5:
                indicators += (5.,)
            for sec2 in range(97,99):
                key = str(sec1) + "." + chr(sec2) + "."
                indicators += (key, )
        
        if sec1 == 6 or sec1 == 8:
            indicators += (str(sec1) + ".",)
        
        if sec1 == 9:
            for sec2 in range(97,102):
                key = str(sec1) + "." + chr(sec2) + "."
                indicators += (key, )
                
    return indicators

def indicators(info_list):
    """
    function will store each indicator index in the list
    
    info_list: a list cntains all doucment information
    """
    indicators_indice = []
    for index in range(len(info_list)):
        if (info_list[index].startswith("1. POPULATION:") or info_list[index].startswith("2. BUILDINGS:") 
            or info_list[index].startswith("3.  NEW") or info_list[index].startswith("4. OVERHANG") 
            or info_list[index].startswith("5. SALE") or info_list[index].startswith("6. MORTGAGE") 
            or info_list[index].startswith("7. TOTAL") or info_list[index].startswith("8. DESCRIPTION") 
            or info_list[index].startswith("9. LOCATION")):
            indicators_indice.append(index)
            
    return indicators_indice
    
def create_a_list(fin):
    """traverse entire list and create a list that contains data
    
    fin: input file
    """
    temp_line = ""
    for line in fin:
        line = line.strip()
        temp_line += line + "="
        
    temp_list = temp_line.split("=")
    
    return temp_list[:len(temp_list)-1]
    
        
def process_file(info, indice):
    """
    function will remove not necessary subscripts in data list
     
    info: a list contains all document information
    """
    processed_list = []
    
    for index in range(len(indice)):
        if index == 0:
            # adding 0.b
            processed_list.append(info[indice[index]-1])
            # adding #1 indicator information
            for subscript in range(indice[index]+2, indice[index+1]):
                if subscript % 2 == 1:
                    processed_list.append(info[subscript])
        elif index == 1:
            processed_list.extend([info[indice[index]+2], info[indice[index]+4]])
            
            for subscript in range(indice[index], indice[index+1]):
                if (info[subscript].startswith("a.  Type") or info[subscript].startswith("b.  Construction") or
                    info[subscript].startswith("c.   Average") or info[subscript].startswith("d.  Repair") or
                    info[subscript].startswith("e.   Occupancy") or info[subscript].startswith("f. Owner") or
                    info[subscript].startswith("j.    Sales") or info[subscript].startswith("k.   Predicted") or
                    info[subscript].startswith("o.   Rental") or info[subscript].startswith("p.   Predicted")):
                    processed_list.extend([info[subscript+1], info[subscript+2]])
                elif (info[subscript].startswith("g.   1935") or info[subscript].startswith("l.    1935")):
                    processed_list.extend([info[subscript+1],info[subscript+3]])
                elif (info[subscript].startswith("h.   1937") or info[subscript].startswith("m.  1937")):
                    processed_list.extend([info[subscript+1],info[subscript+2],info[subscript+3],info[subscript+4]])
                elif (info[subscript].startswith("i.") or info[subscript].startswith("n.")):
                    processed_list.extend([info[subscript+1],info[subscript+3],info[subscript+4],info[subscript+5],info[subscript+6]])
        elif index == 2:
            for subscript in range(indice[index]+1, indice[index+1]):
                if subscript % 2 == 0:
                    processed_list.append(info[subscript])
        elif index == 3:
            for subscript in range(indice[index]+2, indice[index+1]):
                if subscript % 2 == 1:
                    processed_list.append(info[subscript])
        elif index == 4:
            for subscript in range(indice[index], indice[index+1]):
                if subscript % 2 == 1:
                    processed_list.append(info[subscript])            
        elif index == 5:
            processed_list.append(info[indice[index]+1])
        elif index == 6:
            for subscript in range(indice[index]+1, indice[index+1]):
                processed_list.append(info[subscript])
        elif index == 7:
            processed_list.append(info[indice[index]+1])
        elif index == 8:
            for subscript in range(indice[index]+1, len(info)):
                if subscript % 2 == 0:
                    processed_list.append(info[subscript]) 
            processed_list.append(info[len(info)-1])

    return processed_list

def output_file(keys, processed_list):
    if os.path.isfile("summary.csv"):
        fout = open("summary.csv", "a", newline= "")
        fout_writer = csv.writer(fout)
        fout_writer.writerow(processed_list)
        
    else:
        fout = open("summary.csv", "w", newline = "")
        fout_writer = csv.writer(fout)
        fout_writer.writerow(keys)
        fout_writer.writerow(processed_list)
             
        
def main():
    """
    main function.
    Program will be started from this function
    """
    # creating keys first. This function won't process more than once.
    keys = create_keys()
    
    # remove empty window for file chooser
    tk.Tk().withdraw()
    # file chooser dialog pop up
    r_files = askopenfilenames()
    
    for file_name in r_files:
        fin = open(file_name)
        info_list = create_a_list(fin)
        indicator_indice = indicators(info_list)
        processed_list = process_file(info_list, indicator_indice)
        output_file(keys, processed_list)
    
main()