# How to Contribute

If you want to contribute to ezEngine, there are several ways how you can help out.

## Using the Engine

Just using the engine and [filing bug reports](https://github.com/ezEngine/ezEngine/issues), feature requests or generally giving feedback is already a very, very valuable way of contributing. Be sure to include a detailed description of what you where doing, what you saw vs. what you expected, such that it is easy for us to reproduce. We cannot test every feature under all conditions and we do not know all the ways people want to use a feature, so giving feedback is a great way of contributing.

## Extend the Samples

The samples are there for you to get to know the engine and have a playground to try out stuff. As you may notice, most samples are not "complete", ie. they could be extended a great deal with functionality, with code comments, etc. This was not a didactic decision, but rather due to limited time on our side, so if you play with a sample and improve it, even just slightly, please feel welcome to contribute your changes back, so that others can benefit from it.

Of course you are also invited to write entirely new samples.

## Code Documentation

We try to document our code as well as possible, but there are undocumented or poorly documented pieces, and of course there are also comments that are outdated or not as good as they could be. If you improve any documentation, please contribute it back, even if you only did minor changes or fixed typos.

## Bugfixes

If you find a bug, and manage to fix it yourself, don't hold back! Create a PR and we will gladly integrate it. Become our personal hero by also adding an automated test to prevent regressions.

If you itch to fix *something* you can also search our [bug tickets](https://github.com/ezEngine/ezEngine/issues). Items that we consider 'relatively easy' to fix without much knowledge of the engine, have the label *good first issue*.

## Unit Tests

EZ ships with a large number of unit tests. Especially the lower level functionality is well covered with tests, but the higher up code coverage becomes more and more spotty. If you want to add a test, that's great. Especially if you run into a bug, no matter whether you are able to fix it yourself or not, adding a test that reproduces the bug (and thus ensures it won't reappear after a fix) is very useful. If you do not want to go through the hassle of setting up a proper test, even just posting a piece of code that reproduces an issue in general, allows us to put that into a proper test scenario with little effort.

And if you really want to contribute to the overall test coverage, search the code-base for "\\\\\\test" or "TODO" to find code pieces that developers already marked up to need a test.

## Features

We also value feature contributions, but with those we might be much more picky. If you feel confident enough to add a whole new feature, go for it. [Contact us](../contact.md) if you need help with something. In fact, unless it is a very small feature, it may be beneficial to contact us just to get on the same page what a feature should do, how it should be exposed to the user and what's the best way to implement it. You should have a strong background in C++, though, as we simply don't have the time to walk you through basic programming steps, we can only give high-level help on how to make stuff work inside EZ.

## See Also


* [Contact](../contact.md)
* [Frequently Asked Questions](faq.md)
