# Asset Curator

The *asset curator panel* is a tool to help find and fix problems with [assets](assets-overview.md). If the panel is not visible, use *Panels > Asset Curator* to open it.

![Asset Curator Panel](media/asset-curator.png)

## Activity

At its top the asset curator panel displays a timeline of recently processed assets. Each bar represents one asset being transformed, with the Y-axis showing the individual worker processes and the X-axis showing time. Periods of inactivity are compressed to keep the view compact, indicated by a diagonal pattern. This makes it easy to see how many assets were processed in parallel and how long each one took.

## Transform Issues

If an asset fails to transform for some reason, it will be listed in the view to the bottom left. The most common issue is a missing file reference. For example when a texture source file has been moved or renamed, the texture asset can't find it anymore and thus fails to transform.

When you select an asset from that list, the log at the bottom right will display any error message from the failed transform. Double click the asset to directly open the document.

If **Show Indirect Issues** is disabled (the default), only assets that have problems finding their source files are displayed. Otherwise all assets which failed to transform are displayed, however, most of them will be follow-up issues due to other assets being incomplete.

Once you fix an asset and make sure it is transformed, the asset curator will no longer show it in the issues list.

## Video

[![video](https://img.youtube.com/vi/q9_bGgBjENA/0.jpg)](https://www.youtube.com/watch?v=q9_bGgBjENA)

## See Also

* [Asset Browser](asset-browser.md)
* [Assets](assets-overview.md)
