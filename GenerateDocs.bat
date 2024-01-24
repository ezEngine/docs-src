@echo off

echo Generating TOC...
python scripts\create-toc.py

echo Updating Snippets...
python scripts\code-snippets.py
