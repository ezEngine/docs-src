@echo off

REM set current working directory to this folder's parent, because that's what the create-toc script expects
Pushd %cd%\..
echo Generating TOC...
py scripts\create-toc.py
popd

