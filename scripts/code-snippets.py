#!python3

import os
import re

import Doc

snippets = {}

if os.path.exists("./ezEngine/Code"):
    Doc.SearchSourceSnippets("./ezEngine/Code", snippets)
elif os.path.exists("./../ezEngine/Code"):
    Doc.SearchSourceSnippets("./../ezEngine/Code", snippets)
else:
    raise Exception("Couldn't find ezEngine repository")

Doc.ReplaceTargetSnippets("./pages/docs", snippets)