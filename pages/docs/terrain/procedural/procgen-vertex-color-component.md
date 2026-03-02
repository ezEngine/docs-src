# Procedural Vertex Color Component

The *Procedural Vertex Color Component* applies procedurally computed vertex colors to a mesh at runtime. It uses a [ProcGen graph](procgen-graph-asset.md) containing one or more [Vertex Color Output](procgen-graph-output-vertexcolor.md) nodes, and writes the resulting per-vertex RGBA data into a GPU buffer that the mesh's material shader can sample.

<!-- ![Procedural vertex colors applied to a mesh](media/procgen-vertexcolor-component.jpg) -->

This is the vertex-color equivalent of the [Procedural Placement Component](procgen-placement-component.md). It is what connects the graph's vertex color outputs to an actual mesh in the scene.

## How It Works

The component requires a [mesh component](../../graphics/meshes/mesh-component.md) on the **same game object**. When the component activates — or when any relevant data changes — it iterates over every vertex of that mesh. For each vertex it evaluates the ProcGen graph, passing the vertex's world-space position, world-space normal, and original authored vertex colors as inputs. The resulting RGBA values are uploaded to a GPU buffer.

The mesh's material shader then reads from this buffer to drive blending, masking, or other per-vertex effects. Exactly how the data is interpreted depends entirely on the shader.

The vertex colors are recomputed automatically when:

* The game object is moved (its transform changes).
* The referenced ProcGen graph asset is reloaded.
* The mesh resource changes.
* A [procedural volume](procgen-volume-box-component.md) in the affected area is invalidated.

## Output Descriptions

Each entry in the `OutputDescs` list connects one named [Vertex Color Output](procgen-graph-output-vertexcolor.md) node from the graph to a color slot, and optionally remaps its channels.

* `Name`: The name of the vertex color output node in the ProcGen graph to use for this slot. The name must match exactly.
* `Mapping`: Defines how the four channels (R, G, B, A) of the computed color are written into the output slot. Each output channel can be mapped to any input channel from the graph result, or set to a constant `Black` (0) or `White` (1). By default each channel maps to itself (R→R, G→G, B→B, A→A). Remapping is useful when a shader expects data in a specific channel order that differs from how the graph computes it.

Multiple entries can be added when the material shader needs more than one independent RGBA slot per vertex. Each entry corresponds to a separate named output in the ProcGen graph.

## Component Properties

* `Resource`: The [ProcGen graph asset](procgen-graph-asset.md) to evaluate. The graph must contain at least one [Vertex Color Output](procgen-graph-output-vertexcolor.md) node.

* `OutputDescs`: A list of output description entries. Each entry selects one named vertex color output from the graph and controls how its channels are mapped into the output. See [Output Descriptions](#output-descriptions) above.

## See Also

* [ProcGen Graph Asset](procgen-graph-asset.md)
* [ProcGen Graph Vertex Color Output](procgen-graph-output-vertexcolor.md)
* [ProcGen Graph Input Nodes](procgen-graph-inputs.md)
* [Procedural Placement Component](procgen-placement-component.md)
* [Procedural Object Placement](procedural-object-placement.md)
