import os
import re

def WalkFileStructure(curDir, callback, reportFiles = True, reportFolders = True):

    for name in os.listdir(curDir):

        if name.startswith("."):
            continue

        fullPath = os.path.join(curDir, name)

        if (reportFiles and os.path.isfile(fullPath)) or (reportFolders and os.path.isdir(fullPath)):

            if not callback(curDir, name):
                return False

        if os.path.isdir(fullPath):
            if not WalkFileStructure(fullPath, callback, reportFiles, reportFolders):
                return False

    return True


def BuildFileDictionary(dir):

    nameToPath = {}

    def foundPath(parentDir: str, nameWithCase: str):

        if not nameWithCase.endswith(".md") and not nameWithCase.endswith(".jpg") and not nameWithCase.endswith(".png"):
            return True

        fullPath = os.path.join(parentDir, nameWithCase)

        name = nameWithCase.lower()

        if name != "toc.md" and name in nameToPath:
            print(f"Error: File name is not unique: '{name}' - {fullPath}")
            #return False

        nameToPath[name] = fullPath

        if name.endswith(".md"):

            with open(fullPath, "r") as file:
                content = file.read()

            pattern = r"\#+\s+([^\n]+)\n"

            for match in re.finditer(pattern, content):

                sublink = match.group(1).lower()
                sublink = sublink.replace(" ", "-")
                sublink = sublink.replace("(", "")
                sublink = sublink.replace(")", "")
                sublink = sublink.replace("`", "")
                sublink = sublink.replace(".", "")
                sublink = sublink.replace("/", "")

                nameToPath[name + "#" + sublink] = fullPath + "#" + sublink

                #print(f"Headline: '{match.group(1)}' - '{sublink}'")


        return True

    WalkFileStructure(dir, foundPath, reportFolders=False)
    return nameToPath