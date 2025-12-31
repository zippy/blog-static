---
title: "blogging and tech support"
date: 2006-01-24
categories: 
  - "collective-intelligence"
  - "solutions"
slug: "blogging-and-tech-support"
---

I've found that numerous times when I type into google a technical question, be it an error message that I'm seeing when installing some software package or some feature about a programming language, that where I often end up is in some person's blog where they describe how they coped with exactly the same problem. This phenomenon seems to me a generalized solution to tech support, and also a wonderfully comunal and [gift economy](http://www.thetransitioner.org/wiki/tiki-index.php?page=Gift+Economy) approach to problem solving. So I've decided to play the game too by creating a category for this blog called solutions, and, as often as I can, post my minor little breakthroughs in hopes that they will be helpful to someone else. And here's my first:

I've been learning [Smalltalk](http://en.wikipedia.org/wiki/Smalltalk) using [squeak](http://squeak.org) and I assumed that, like other object-oriented languages, there would be a constructor method that could take many parameters which would be used by the constructor to load up the values of instance variables. For example in perl a simplified constructure would look like:

`sub new { my $class = shift; my $self = {}; bless $self, $class; $self->{'FOO'} = shift; # save the constructor parameters into our data structure $self->{'BAR'} = shift; return $self; }`

which would be instantiated like this: `theObjectClassName->new('fish','dog');`

In Smalltalk, it appears, you don't do that. Instead you just create settors for your parameters and chain them to the new call. So you would have two methods:

`setFoo: fooVal foo := fooVal setBar: barVal bar := barVal`

and your call to instantiate an object is then just: `theObjectClassName new setFoo:'fish' setBar:'dog'`

because the first two words create the object and the the second two are just messages that get to the object after it is created, one at a time.

I love the beautiful parsimony of notions in Smalltalk.
