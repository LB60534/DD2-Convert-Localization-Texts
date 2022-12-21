#!/usr/bin/env python
# coding: utf-8

import os
import re
import pandas as pd
from pathlib import Path

# Read and process all files in localization source directory
def processAllFiles(inputPath,inputSeparate):
    # Change the directory
    os.chdir(inputPath)
    outDataFrame = pd.DataFrame(dataTemplate())
    # iterate through all file
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{inputPath}\{file}" # Todo: May change to outputPath later
            # call process text file function
            processOut = process_text_file(file_path)
            if not processOut.empty:
                if inputSeparate:
                    writeCsv(processOut,Path(file).stem)
                else:
                    outDataFrame = pd.concat([outDataFrame, processOut])
    if (inputSeparate == False) & (outDataFrame.empty == False):
        writeCsv(outDataFrame,"barks_act_outs")

# Process text File line by line
def process_text_file(file_path):
    outputDF = pd.DataFrame()
    # Check if it is barks file
    fileStem = Path(file_path).stem
    if fileStem.find("barks") != -1:
        print("Process file: "+fileStem)
        data = dataTemplate()
        with open(file_path, 'r') as f:
            for line in f.readlines():
                strLine = line.strip()
                processLine(strLine,data)
        outputDF = pd.DataFrame(data)
        return outputDF
    return outputDF

# Process a line
def processLine(str, data):
    # print("\tProcess line:",str)
    splitStr = re.split("\=",str)
    if (len(splitStr) == 2):
        if (splitStr[1] != ""):
            outContent = splitStr[1]
            splitAttibutes = re.split("\+",splitStr[0])
            # outType = splitAttibutes[0]
            # splitAttibutes.remove(splitAttibutes[0])
            outCharacter = ""
            outRelation = ""
            outAttribute = ""
            for attr in splitAttibutes:
                findChar = findCharacter(attr)
                if findChar != "":
                    outCharacter = findChar
                else:
                    findRelation = findRelationship(attr)
                    if findRelation != "":
                        outRelation = findRelation
                    else:
                        outAttribute = outAttribute + " & " + re.sub(r"bark_|act_out_","",attr)
            data["Character"].append(outCharacter)
            data["Relation"].append(outRelation)
            data["Attribute"].append(re.sub("\s&\s","",outAttribute,1))
            # data["Attribute"].append(outAttribute)
            data["Content"].append(outContent)
    else:
        return;

def findCharacter(charName):
    searchName = charData[charData.class_name == charName].name
    if not searchName.empty:
        displayName = searchName.values[0]
        #print(displayName)
        return displayName;
    else:
        return ""

def findRelationship(relationName):
    searchRelation = relationData[relationData.relationship == relationName].relationship
    if not searchRelation.empty:
        displayName = searchRelation.values[0]
        return displayName;
    else:
        return ""

def dataTemplate():
    return {"Character":[], "Relation":[], "Attribute":[], "Content":[]}; # Probably not needed

# Write output data into csv file
def writeCsv(pdDataFrame, fileName):
    #Write df to fileName.csv
    outputFileName = "Output-"+fileName+".csv"
    pdDataFrame.to_csv(outputFileName, index=False)
    print("Write to output file: "+outputFileName)
    return;


# load prepared data
# charData = pd.read_csv(r'heroName.csv', encoding='utf-8')
# relationData = pd.read_csv(r'relationship.csv', encoding='utf-8')
charData = {
    "class_name":["highwayman","man_at_arms","grave_robber","plague_doctor","occultist","jester","leper","hellion","runaway","bounty hunter","bounty_hunter","vestal"],
    "name": ["Highwayman","Man-at-arms","Grave Robber","Plague Doctor","Occultist","Jester","Leper","Hellion","Runaway","Bounty Hunter","Bounty Hunter", "Vestal"]
}
relationData = {
    "relationship": ["amorous","hopeful","respectful","hateful","suspicious","envious","resentful","inseparable","tumultuous","nihilistic"]
}
charData = pd.DataFrame(charData)
relationData = pd.DataFrame(relationData)


inputPath = input("Please input the directory of all text files (OR current working directory if input blank):\n")
# inputPath = "F:\Workspace\JupyterNotebook\My Program\TestData" # Temp for testing
# inputPath = "F:\Program Files\Epic Games\DDIIExperimental\Darkest Dungeon II_Data\StreamingAssets\Localization\Sources"
if inputPath == "":
    inputPath = os.getcwd()

inputSeparate = int(input("\n\nPlease select (Default mode: 1)\n\r1: Output to a single file Output-barks_act_outs.csv\n\r2: Output to separate files\n"))
if (inputSeparate == 1):
    inputSeparate = False
elif (inputSeparate == 2):
    inputSeparate = True
else:
    inputSeparate = False

processAllFiles(inputPath,inputSeparate)
os.system("pause")
