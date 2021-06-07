#!python3

import os
import re

import Doc

snippets = {}
Doc.SearchSourceSnippets(r"D:\GitHub\ezEngine\Code", snippets)

Doc.ReplaceTargetSnippets("./docs", snippets)