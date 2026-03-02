# ProcGen Graph Vertex Color Output

The *Vertex Color Output* node defines what procedurally computed color values get written per vertex onto a mesh. It is the counterpart to the [Placement Output](procgen-graph-output-placement.md) node, but instead of spawning objects it drives vertex colors on an existing mesh.

A [ProcGen graph](procgen-graph-asset.md) can contain multiple vertex color output nodes. Each one represents an independent RGBA layer of vertex color data. They are consumed by the [Procedural Vertex Color Component](procgen-vertex-color-component.md), which applies them to a mesh at runtime.

<!-- ![ProcGen vertex color output node](media/procgen-vertexcolor-output-node.jpg) -->

## How It Works

When a [Procedural Vertex Color Component](procgen-vertex-color-component.md) evaluates the ProcGen graph, it iterates over every vertex of the attached mesh. For each vertex it feeds the following data into the graph as inputs:

* The vertex's **world-space position** (accessible via the [Position node](procgen-graph-inputs.md#position-node))
* The vertex's **world-space normal** (accessible via the [Normal node](procgen-graph-inputs.md#normal-node))
* The mesh's **original, authored vertex color** (accessible via the [Mesh Vertex Color node](procgen-graph-inputs.md#mesh-vertex-color-input-node))

The vertex color output node collects the R, G, B and A values produced by the graph for that vertex and writes them into a GPU buffer. The mesh's material shader can then read this buffer to drive blending, masking, or any other per-vertex effect.

The result is computed once and cached. It is recomputed automatically whenever the mesh, the ProcGen graph asset, or any [procedural volume](procgen-volume-box-component.md) in the affected area changes.

## Node Properties

* `Name`: A unique name for this output within the graph. This name must match the `Name` field in the corresponding entry of the [Procedural Vertex Color Component's](procgen-vertex-color-component.md) `OutputDescs` list. This is how the component knows which graph output maps to which channel slot.
* `Active`: If disabled, this output node is skipped entirely and no data is computed for it.

## Input Pins

* `R`: The red channel of the output color. Expects a value in [0;1] range.
* `G`: The green channel of the output color. Expects a value in [0;1] range.
* `B`: The blue channel of the output color. Expects a value in [0;1] range.
* `A`: The alpha channel of the output color. Expects a value in [0;1] range.

Connect these pins to any combination of [input nodes](procgen-graph-inputs.md) and [math nodes](procgen-graph-math.md). Unconnected pins default to `0` (black) for R, G, B and `1` (white) for A.

## See Also

* [Procedural Vertex Color Component](procgen-vertex-color-component.md)
* [ProcGen Graph Asset](procgen-graph-asset.md)
* [ProcGen Graph Input Nodes](procgen-graph-inputs.md)
* [ProcGen Graph Math Nodes](procgen-graph-math.md)
* [ProcGen Graph Placement Output](procgen-graph-output-placement.md)
