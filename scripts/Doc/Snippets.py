import os
import re

from .File import *

def SearchSourceSnippets(srcDir: str, snippets: dict):

    def FoundFile(parentDir: str, name: str):

        if not name.endswith(".h") and not name.endswith(".cpp"):
            return True

        with open(os.path.join(parentDir, name), mode='r', encoding='utf-8') as file:
            lines = file.readlines()

        lineIdx = 0
        lenLines = len(lines)

        while(lineIdx < lenLines):

            line = lines[lineIdx]
            lineIdx += 1

            idx = line.find("BEGIN-DOCS-CODE-SNIPPET:")
            if idx >= 0:

                snippetName = line[idx + 24:].strip(' \r\n\t').lower()

                print(f"Found snippet: {snippetName}")

                nesting = 0
                snippetText = ""
                maxWhiteSpace = 100
                snippetLineIdx = lineIdx

                snippetLines = []

                while(snippetLineIdx < lenLines):
                    snippetLineIdx += 1
                    line = lines[snippetLineIdx - 1]
                    line = line.replace("\t", "  ")

                    if line.find("BEGIN-DOCS-CODE-SNIPPET:") >= 0:
                        nesting += 1
                        continue

                    if line.find("END-DOCS-CODE-SNIPPET") >= 0:
                        if nesting == 0:
                            break
                        nesting -= 1
                        continue

                    if len(line.strip()) > 0:
                        wsc = len(line) - len(line.lstrip(' '))
                        maxWhiteSpace = min(maxWhiteSpace, wsc)

                    snippetLines.append(line)

                for line in snippetLines:

                    if len(line) >= maxWhiteSpace:
                        line = line[maxWhiteSpace:]
                        
                    snippetText += line

                snippets[snippetName] = snippetText

        return True

    WalkFileStructure(srcDir, FoundFile, reportFolders=False)



def ReplaceTargetSnippets(targetDir: str, snippets: dict):

    def FoundFile(parentDir: str, name: str):

        if not name.endswith(".md"):
            return True

        with open(os.path.join(parentDir, name), "r") as file:
            lines = file.readlines()

        lineIdx = 0

        newLines = []
        replacedAny = False

        while(lineIdx < len(lines)):

            line = lines[lineIdx]
            lineIdx += 1

            newLines.append(line)

            idx = line.find("BEGIN-DOCS-CODE-SNIPPET:")
            if idx >= 0:

                snippetName = line[idx + 24:].lower()
                snippetName = snippetName.replace("-->", "")
                snippetName = snippetName.strip(' \r\n\t')

                print(f"Replacing snippet: {snippetName}")
                replacedAny = True

                newLines.append("```cpp\n")
                newLines.append(snippets[snippetName])
                newLines.append("```\n")

                while(lineIdx < len(lines)):
                    if lines[lineIdx].find("END-DOCS-CODE-SNIPPET") >= 0:
                        break

                    lineIdx += 1

        if replacedAny:

            with open(os.path.join(parentDir, name), "w") as file:
                file.writelines(newLines)

        return True

    WalkFileStructure(targetDir, FoundFile, reportFolders=False)