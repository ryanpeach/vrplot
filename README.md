# VR Plot

We use [A-Frame](https://aframe.io/) and [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) to create data
visualizations directly in [WebVR](https://webvr.info/)! It works with any web browser and is as easy to use as
 [Seaborn](https://seaborn.pydata.org/).
 
We want this to be not only a toolkit for plotting data in VR, but using VR as a mechanism to expand out into the domain
of high dimensional plotting in general.

# Development

I'm livestreaming on [Twitch](https://www.twitch.tv/rgpeach10)

I'm a Machine Learning Researcher at a worldwide company located in Atlanta Ga.

Doing this mostly on weekends.

It's probably the most fun I've had on a project looking out the VR headset at my fancy plots.

# Contribution

*Please Contribute!!!*

We need:

* Examples
* Documentation
* New Plotting Types
* Bug Fixes

It's really not hard!

* New Entities (which are like Points, Boxes, Polygons, Etc.) go in `vrplot/basic_objects.py`
* New Plotting types get their own file (unless they are loosely related to other plotting types).
* New Plotting types get their own example in `examples` and go here in the readme. Their output should be
  of the same name under `examples/output`
* Follow types in `vrplot/types.py` and type hint all your code.
* Make well written exceptions and put them in `vrplot/exceptions.py`. Common exceptions can get their own checker.
* Follow PEP8
 
# Examples

* [Archimedean Spiral](examples/output/archimedeanspiral.html)
* [Double Ramp](examples/output/doubleramp.html)