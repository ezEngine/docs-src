import os
import re
from typing import List, Tuple

def DetermineTocOrder(curDir, order: list):

    tocTxt = os.path.join(curDir, "toc.txt")
    subItems = []

    #ymlContent = ""
    #writeLocalYml = False

    if os.path.exists(tocTxt):
        
        with open(tocTxt, "r") as tocFile:
            subItems = tocFile.readlines()

    else:

        for item in os.listdir(curDir):
            subItems.append(item)

    for item in subItems:

        itemName = item.strip()

        if itemName == "":
            continue
        if itemName == "media":
            continue
        if itemName.endswith(".yml"):
            continue

        folderName = itemName
        displayName = itemName

        if folderName == "---":

            order.append("---")

        else:

            displayName = displayName.replace("-", " ")
            displayName = displayName.replace(".md", "")
            displayName = displayName.title()

            sep = itemName.find("|")
            
            if sep >= 0:
                folderName = itemName[0:sep]
                displayName = itemName[sep+1:]

            folderName = folderName.strip()
            displayName = displayName.strip()

            if folderName.startswith("http"):

                if sep < 0:
                    order.append(f"[{folderName}]({folderName})")
                else:
                    order.append(f"[{displayName}]({folderName})")
            
            else:

                subPath = os.path.join(curDir, folderName)

                if os.path.isdir(subPath):

                    order.append(">>>" + displayName)
                    DetermineTocOrder(subPath, order)
                    order.append("<<<")


                    #ymlContent += f"- name: {displayName}\n"
                    #ymlContent += f"  href: {folderName}/\n"

                else:
                    order.append(subPath)

                    #ymlContent += f"- name: {displayName}\n"
                    #ymlContent += f"  href: {folderName}\n"

    #if writeLocalYml:
    #    with open(os.path.join(curDir, "toc.yml"), "w") as ymlToc:
    #        ymlToc.write(ymlContent)

    return

def GenerateTocMD(nameToFile: dict, order: list):

    tocContent = ""

    topLevel = True
    indentation = ""

    for item in order:

        line:str = item

        if item == "<<<":

            if indentation == "":
                topLevel = True
            else:
                indentation = indentation[0:-2]
            
            continue

        if line.startswith(">>>"):

            headline = line[3:]

            if topLevel:
                tocContent += f"\n## {headline}\n\n"

                topLevel = False
                indentation = ""
            else:
                tocContent += f"{indentation}* __{headline}__\n"

                indentation = indentation + "  "

        elif line.startswith("---"):

            tocContent += f"\n{indentation}---\n"

        else:

            tocContent += f"{indentation}* []({item})\n"

    print(f"\n\n ======= GenerateTocMD ========== \n\n")
    print(tocContent)
    print(f"\n\n ======= END ========== \n\n")

    return tocContent

def indentLevel(n):
    word = '#'
    for x in range(n):
        word += '#'
    
    return word

def GenerateTocDocFX(nameToFile: dict, order: list):

    tocContent = ""

    indentation = 0

    for item in order:

        line:str = item

        if item == "<<<":

            indentation = indentation - 1
            continue

        if line.startswith(">>>"):

            headline = line[3:]

            tocContent += f"{indentLevel(indentation)} {headline}\n"
            indentation = indentation + 1

        elif line.startswith("---"):

            #tocContent += f"\n{indentation}---\n"
            continue

        elif line.startswith("["):

            tocContent += f"{indentLevel(indentation)} {line}\n"

        else:

            tocContent += f"{indentLevel(indentation)} []({item})\n"

    print(f"\n\n ======= GenerateTocDocFX ========== \n\n")
    print(tocContent)
    print(f"\n\n ======= END ========== \n\n")

    return tocContent