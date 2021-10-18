#!python3

import os
import re

import Doc

snippets = {}
Doc.SearchSourceSnippets(r"C:\GitHub\ezEngine\Code", snippets)

Doc.ReplaceTargetSnippets("./pages/docs", snippets)