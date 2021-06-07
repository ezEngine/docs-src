#!python3

import os
import re

import Doc

def GenerateFolderTOC(nameToFile: dict, folder: str):

    tocMdFile = os.path.normpath(f"{folder}/toc.md")

    if os.path.exists(tocMdFile):
        os.remove(tocMdFile)

    tocOrder = []
    Doc.Toc.DetermineTocOrder(folder, tocOrder)

    tocContent = Doc.Toc.GenerateTocDocFX(nameToFile, tocOrder)

    with open(tocMdFile, "w") as indexMd:
        indexMd.write(tocContent)

    Doc.Link.FixFileLinks(tocMdFile, nameToFile)



nameToFile = Doc.File.BuildFileDictionary("./pages")

GenerateFolderTOC(nameToFile, "./pages/docs")
GenerateFolderTOC(nameToFile, "./pages/releases")
GenerateFolderTOC(nameToFile, "./pages/getting-started")
GenerateFolderTOC(nameToFile, "./pages/samples")

Doc.Link.FixAllFileLinks(nameToFile)
