@echo off

call build_page.bat

echo Hosting documentation...
..\tools\docfx\docfx.exe ..\docfx.json --serve
