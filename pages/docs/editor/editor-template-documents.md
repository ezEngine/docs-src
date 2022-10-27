# Template Documents

When you create a new document, it is typically blank. You can change this, by saving a pre-configured *template document* in your project's directory.

Every time a new document is created, the editor checks whether such a template document is present, and if so, clones that instead.

For the editor to find your template document, it has to be stored in the sub-folder `Editor/DocumentTemplates` and has to have the name `Default`. The file extension of course has match the document type.

So for example if your project is located under `C:/MyGame` then to create a custom scene template, you would store a scene file under `C:/MyGame/Editor/DocumentTemplates/Default.ezScene`.

This can be done for any document type.

## See Also

* [Editor Documents](editor-documents.md)

