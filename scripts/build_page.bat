@echo off

call generate_toc.bat

echo Building documentation...
..\tools\docfx\docfx.exe ..\docfx.json --build