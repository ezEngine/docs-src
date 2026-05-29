#!python3

import os
import re
import sys

import Doc

snippets = {}

if os.path.exists("./ezEngine/Code"):
    Doc.SearchSourceSnippets("./ezEngine/Code", snippets)
    Doc.SearchSourceSnippets("./ezEngine/Data", snippets)
elif os.path.exists("./../ezEngine/Code"):
    Doc.SearchSourceSnippets("./../ezEngine/Code", snippets)
    Doc.SearchSourceSnippets("./../ezEngine/Data", snippets)
else:
    raise Exception("Couldn't find ezEngine repository")

if Doc.ReplaceTargetSnippets("./pages/docs", snippets):
    sys.exit(1)