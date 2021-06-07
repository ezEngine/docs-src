# How Particle Effects Work

This article gives a broad introduction how particle effects work. It is meant for people completely new to this topic. The information here is not very engine specific, as particle effects conceptually work the same in all engines.

## Particles

A **particle** is the smallest unit that a particle effect is made up of. Each particle has a small number of properties. Every particle has a position, a duration how long it lives, and typically also velocity (speed and direction), size and color. It may have additional properties, when needed, but those are the most common ones.

In a particle effect we often have hundreds, sometimes even thousands of particles. Each particle is small, but by having hundreds of particles scattered throughout a volume, the end result is something that looks volumetric and behaves in complex patterns.

There a multiple ways a single particle may get rendered. The most common method are so called *billboards*. A billboard is a quad which always rotates such that it faces the viewer. By using a texture with a circular image (for instance a flare) and making the quad transparent, the particle will appear volumetric (it appears circular from all directions), although it is just rendered with a simple polygon that is a flat plane. The reason this is the preferred method for rendering particles is that it is otherwise quite difficult to render volumetric, transparent objects with triangles (the only thing GPUs can render). Billboards are an effective illusion.
Particles can represent other things, as well, for example small meshes, light sources or even sounds, but billboards are by far the most common.

A large part of building a particle effect is about configuring how the different properties of all those particles evolve over time. For example, if you configure particles to have a lifespan of two seconds, rise up with medium speed, change their color from red to yellow and fade out shortly before they die, then you get an effect that looks a lot like fire.

## Particle Systems and Effects

You never work or configure individual particles. Instead, you mostly work with **particle systems**. A particle system represents a large amount of particles that all behave according to the same rules. A complete **particle effect** often consists of multiple particle systems, but always at least one. Each particle system defines different rules how the particles of that system behave.

So in the fire example, you would have one particle system which is configured to spawn five particles every tenth of a second. All these particles are rendered as billboards, use the same flare texture, rise up, and change their color according to some fire gradient over their lifetime. This system represents the flames.
To add smoke above the flame, you would add a second particle system, which may only spawn one particle every tenth of a second, use a smoke-like texture, rise up more slowly and start with a zero size at the beginning, slowly growing larger and larger, such that it becomes visible just above the flame.
The flame particles and the smoke particles have no relation, whatsoever, but together they form a better illusion of fire.

## Evolving Properties

The code that updates a particle system mostly handles every property of the particles in isolation. And that is also how you need to think about each property, when you want to create an effect. The way a property, such as position, changes, is called the *behavior*. So for example, a particle may rise up slowly, or it may fall down according to gravity. Whether the position *behaves* one way or the other results in a drastically different effect. The same is true for all other properties. A particle may have a constant size or it may start small but grow over time. Its color may be just white, or some random blue-ish tone or it may change its color such that it appears to be burning up or fading out. Every property has its own rule, how it behaves. Put it all together and you can build an infinite amount of different effects.

## Building Blocks

What the particle editor presents to you, are a number of building blocks that you choose and configure. For example, there are a few *behaviors* how the position of a particle should be calculated. There are a few building blocks for determining a particle's color, its size, and how to render it. Many behaviors are mutually exclusive. So if you already chose the "gravity" building block, which lets particles fall down, then you can't choose a second behavior that also affects particle positions. Most building blocks expose options for you to tweak. For example the "gravity" behavior allows you to tweak the strength of the applied gravity.

To create an effect, you create multiple particle systems, and for each one you select and configure the desired behaviors.

## Spawning and Lifetime

We already mentioned that particles have a limited (usually very short) lifespan. Generally you can separate particle effects into two types: short **one shot** type of effects, and long lasting or even unending **continuous** effects. Explosions, water splashes and bullet impacts are all of the former type. They typically spawn all of their particles in one big burst. Those particles live for a second or so and then the effect is over. Fire, smoke and mist are of the latter type. Those effects typically spawn particles continuously. Each particle lives for several seconds and by the time it dies, many other particles have already been spawned to take its place. Continuous effects can be configured such that they are not endless, for example a smoke effect may stop by itself after 10 seconds. However, often it is more convenient to build such effects as endless effects, that never stop, and then use custom (script) code to make a particle effect stop spawning new particles at the desired time. This way the desired duration of an effect can be dynamically adjusted.

Whether an effect acts one way or the other, is determined by the selected type of **emitter**. The emitter building block specifies how often and how many new particles get spawned. Emitters can be configured to be smooth or erratic, doing short bursts or long intervals. Most of the time one uses one of two emitter types, but there are also emitters that only spawn particles when some event happens, which can be used for even more complex effects.

How long a particle will live is decided randomly when it gets spawned (within a range). How much time a particle has left to live, is often used to look up other properties. For example the color of a particle often depends on its lifetime, such that particles will fade out towards their end.

## See Also


* [Particle Effects](particle-effects-overview.md)
