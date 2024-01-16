import os
import re

def CreateRelativeLink(srcFile: str, linkFile: str):

    if linkFile == "":
        print(f"Error: empty link in '{srcFile}'")
        return

    result = ""
    result = os.path.relpath(linkFile, srcFile)
    result = result.replace("\\", "/")
    return result

def IsPageTodo(filename: str):

    if not filename.endswith(".md"):
        return False

    if not os.path.exists(filename):
        return False

    with open(filename, "r") as file:

        content = file.read()
        return content.find("<!-- PAGE IS TODO -->") >= 0

    return False

def DetermineLinkName(curName: str, filePath: str):

    baseName, ext = os.path.splitext(curName)

    if ext.lower() != "md":
        baseName = curName

    baseName = baseName.strip()

    if baseName.endswith(" (TODO)"):
        baseName = baseName[0: -7]

    postfix = ""

    if IsPageTodo(filePath):
        postfix = " (TODO)"

    if baseName != "" and baseName != "LINK-ERROR":
        return baseName + postfix

    if filePath == "":
        print(f"Error: empty link path")
        return "LINK-ERROR"

    if filePath.lower().endswith("md"):

        with open(filePath, "r") as file:
            content = file.read()

        pattern = "^\\s*#\\s*(.*)\\s*$"
        match = re.search(pattern, content, re.MULTILINE)

        if match:
            return match.group(1) + postfix

    else:

        return baseName

    print(f"Error: invalid link format")
    return "LINK-ERROR"


def FixFileLinks(srcFile: str, nameToFile: dict):

    if not srcFile.lower().endswith(".md"):
        return

    srcDir = os.path.dirname(srcFile)

    with open(srcFile, "r") as file:
        content = file.read()

    pattern = r"\#+\s+([^\n]+)\n"
    allowedSublinks: dict = {}

    for match in re.finditer(pattern, content):

        sublink = match.group(1).lower()
        sublink = sublink.replace(" ", "-")
        sublink = sublink.replace("(", "")
        sublink = sublink.replace(")", "")
        sublink = sublink.replace("`", "")
        sublink = sublink.replace(".", "")
        sublink = sublink.replace("/", "")

        allowedSublinks["#" + sublink] = match.group(0)


    result = content
    pattern = r"\[([^\]]*)\]\(([^\)]*)\)"

    failure = False

    for match in re.finditer(pattern, content):

        fullPattern:str = match.group(0)
        displayName:str = match.group(1)
        orgLink:str = match.group(2)

        head, linkName = os.path.split(orgLink.lower())

        targetFile = nameToFile.get(linkName, "")

        if targetFile != "":
            newRelLink = CreateRelativeLink(srcDir, targetFile)
            displayName = DetermineLinkName(displayName, targetFile)
        else:
            newRelLink = orgLink
            targetFile = orgLink

            isValid = False

            if not isValid and orgLink.startswith("http"):
                isValid = True
                
            if not isValid and orgLink.startswith("mailto"):
                isValid = True

            if not isValid and allowedSublinks.get(orgLink, "") != "":
                isValid = True

            if not isValid:
                print(f"Warning in '{srcFile}': Unknown link: '{orgLink}'")
                failure = True

        newString = f"[{displayName}]({newRelLink})"

        result = result.replace(fullPattern, newString)

    with open(srcFile, "w") as file:
        file.write(result)

    if failure:
        print(f"Failure!\n\n")
        print(f"\n\n ======= INPUT ========== \n\n")
        print(content)
        print(f"\n\n ======= OUTPUT ========== \n\n")
        print(result)
        print(f"\n\n ======= END ========== \n\n")


def FixAllFileLinks(nameToFile: dict):

    for name, path in nameToFile.items():

        FixFileLinks(path, nameToFile)
