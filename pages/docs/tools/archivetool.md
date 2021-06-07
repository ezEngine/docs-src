# ArchiveTool

The ArchiveTool is used to create or extract `.ezArchive` files. Archives are similar to zip files, they contain all the files in a folder, using compression. ezArchive files can be mounted at runtime as [data directories](../projects/data-directories.md).

## ezArchive Format

The internal structure of ezArchives is optimized to make mounting as a data directory extremely efficient. The files are memory mapped and file lookups are faster than for regular folders. Each file in the archive may use compression or not, depending on whether it would make sense for the particular file. Different compression algorithms are possible, though the main compression used is [zstd](../appendix/third-party-code.md#zstd) which yields good compression and is extremely fast to decode.

## Usage

The ArchiveTool is a command line tool.

### Default Usage

The most convenient way to use it, is to pass a single path as the only argument:

```cmd
ArchiveTool.exe C:/my/data
```

When the path points to a folder, it will compress the folder and store the ezArchive file next to it. In the example above: `C:/my/data.ezArchive`

```cmd
ArchiveTool.exe C:/your/data.ezArchive
```

When the path points to an existing archive, the tool will extract the data to a folder next to the file. In the example above: `C:/your/data`

### All Options

The following options allow you to be more specific:

* **-pack** `"path/to/folder"` `"path/to/another/folder"` ...
* **-unpack** `"path/to/file.ezArchive"` `"another/file.ezArchive"`
* **-out** `"path/to/file/or/folder"`

**-pack** and **-unpack** can take multiple inputs to either aggregate multiple folders into one archive (pack) or to unpack multiple archives at the same time.

**-out** specifies the target to pack or unpack things to. For packing mode it has to be a file. The file will be overwritten, if it already exists.
For unpacking the target should be a folder (may or may not exist) into which the archives get extracted.

If no *-out* is specified, it is determined to be where the input file is located.

If neither *-pack* nor *-unpack* is specified, the mode is detected automatically from the list of inputs:

* If all inputs are folders, mode is going to be 'pack'.
* If all inputs are files, mode is going to be 'unpack'.

## Examples

Pack all data in "C:\Stuff" into "C:\Stuff.ezArchive":

```cmd
ArchiveTool.exe "C:\Stuff"
```
  
Pack all data in "C:\Stuff" into "C:\MyStuff.ezArchive":

```cmd
ArchiveTool.exe "C:\Stuff" -out "C:\MyStuff.ezArchive"
```
  
Unpack all data from the archive into "C:\Stuff"

```cmd
ArchiveTool.exe "C:\Stuff.ezArchive"
```
  
Unpack all data from the archive into "C:\MyStuff"

```cmd
ArchiveTool.exe "C:\Stuff.ezArchive" -out "C:\MyStuff"
```

## See Also


* [Data Directories](../projects/data-directories.md)
* [FileSystem](../runtime/filesystem.md)
