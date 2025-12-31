---
title: "Where and the Grammatics of Location"
date: 2021-09-16
tags: 
  - "grammatics"
slug: "where-and-the-grammatics-of-location"
---

Consider playing soccer or football blindfolded. Unless you have gotten really good with echolocation, playing the game becomes impossible for the simple reason that you stop being able to answer the questions “where is the ball?” and “where are my teammates?”.

More subtly, consider the difficulties of having hard or delicate conversations using just a pen and slips of paper. The textual medium blindfolds our built-in ability to read facial and tonal emotional cues, thus making it harder to answer the question “where are you emotionally?”. Without them it is less likely that such conversations will come out well.

Collaborative endeavors, like playing soccer or having a conversation, require knowing the locations of the relevant parties in their spaces. As we examine the vast realms of collaboration we see that the ubiquitous need to know “where” both in familiar physical locations, but also in such non-cartesian spaces as education, familiarity, health, happiness, class, wealth, skill, reputation(s), responsibility, intention, completion, etc...

This seems like a fairly straightforward insight. It’s kind of obvious that maps are important to help guide us in achieving our goals in the territory that the map maps.  What doesn't seem obvious to me are the generalized patterns for groups to understand all the different types of spaces that they might want to locate themselves in, and find the grammar of those patterns so as to build new maps on the fly as the new spaces to navigate are recognized and as existing spaces change.

![where](/blog/images/where.gif)To begin some exploration of this meta-space we present **[Where](https://github.com/lightningrodlabs/where)**, a simple-as-possible Holochain hApp that equips teams with a tool to create maps and lets team members self-locate on those maps. The underlying Holochain DNA assumes that a Space consists of a coordinate system (more on this below) and various bits of meta-data.  Locations in the space are then simply recordings by agents using the coordinate system of the space, along with optional additional data values to add contextual information about any given recording of a location.

As a starting place we begin with spaces that are just limited to cartesian X,Y coordinates and that all include as meta-data a URL of an image for rendering the "surface" of the space. The initial UI for Where is thus very simple. You can create new maps, move between different maps, zoom them if they are large, and add yourself into the map along with textual tag information to be displayed at that location. 

That's a pretty simple place to start, but I think it's a powerful grammar for initial exploration. Using somewhat symbolic images like a mountain-scape, or a forest, small groups can attach group-specific meaning to different parts of the image. This is an initial hack for various non-cartesian coordinate systems of dimensionality less than two, like tree structures, or various linear structures (e.g. time-zones), simply by ignoring parts of the 2D space.

Next steps can include:

- Templates that describe the basic structure of a space but allow custom annotations/additions to it
- UIs that can render surfaces of spaces using other coordinate systems: 3D with OpenGL, low dimension tree and graph spaces, Lat.-Long. for geo-spacial maps, 4D spaces (for example 3D + time), and so on.
- Adding the ability to change the surface of spaces over time, not just add locations on them.
- More specific grammars for the meta-data of location entries as they emerge.
- Adding composability of spaces, i.e. locations on surfaces that lead to or render other spaces.

Here is an abstract grammar for Where:

- Nouns:
    - Space
        - Surface
        - Coordinate System
        - Meta-data
    - Location
    - Space
    - Coordinate Instance
    - Meta-data
- Verbs:
    - Add Space
    - Add Location
    - Update Location
    - Update Space Surface

Like all grammars, the component parts themselves have sub-grammars. For example **Coordinate Systems** are likely constructed out of a grammar that includes dimensionality, units, and some other rules of valid values. And note that this grammar also includes parts-of-speech, what I've labeled "Nouns" and "Verbs".  This is really kind of cheating, because what I've called "Nouns" are really Noun-Types, as I haven't shown any actual Nouns, which would be an actual example of a Space or Location. The "Verbs" really are the only "action-words" of this system, and they are fixed and pretty uninteresting. Kind of like how "conjunctions" are limited to a small set in English.

Though this kind of analysis may be interesting for the computer-scientist/coder/linguists among us, most of us are more interested in the various words, the "vocabulary" of the grammar, and then the conversations that might ensue from using them.

The early development of the ideas for **Where** came from conversations with [Jean Russell](https://thrivable.net) about increasing group awareness of typically hidden social landscapes.  Here's one example she offers for a surprisingly simple but really useful space:  

* * *

#### Case Study: The "Iron Triangle"

I have struggled, as many of us do, in teams where different people hold the values of the project or organization with different weights. To make this generic and familiar, let’s use the cost, quality, and time triangle. Note that the center is blacked out, since we can't have some perfect combination of the three. 

If the team is dominated by time and cost focused people, then they start resenting the person holding for quality. Or, if focus is on quality, then the resistance shows up to the person focused on delivering on time. Somehow this ends up getting personal rather than the person being regarded as a steward of that value. And the group struggles to come into alignment about priorities and actions. 

![iron triangle](/blog/images/5o2dLQB.png)

Note that I have also added, outside the hypotenuse of each angle, the list of consequences people may be trying to avoid by holding that value (at the point of the angle). I believe this too will help others be aware of the risks inherent in not holding to that value.

I am really looking forward to Where as an application I can use with teams to make visible to the group where we each feel the group or project is in the triangle. You could have one where each wants the project to be and another where they think it is now and notice the difference. 

I feel like this conversation about the map and placement will move the conversation from individual tension into shared awareness space. It will help us be more compassionate with the person (aka the value) being resisted. It may help people to be heard, better, in their concern and sense the group's alignment, particularly of the more quiet members. That's better collective intelligence!

![](/blog/images/zhjkYRo.png)

* * *

 

Putting maps like the one in Jean's example above into **Where** softens the "Iron" feeling of "pick-two" into a sense-making process where we can better understand how we use the intelligence of the team to collectively come to good answers, simply because we have an opportunity to see what we all see.  I feel quite excited to see what other similar maps emerge as really useful to groups, but frankly I'm even more excited to see the secondary grammars that will also emerge.  Just like the hashtag was grammatical element introduced to Twitter by one of it's users, I'm guessing that there are some other similar very simple additions to **Where** that will carry as much importance and value.

If you are the daring technical type, you can play with **Where** now by following instructions on the [github repo](https://github.com/lightningrodlabs/where)

Maybe next will be Who, What, How and Why!

#grammatics

<div class="historical-comments mt-8 pt-8 border-t border-neutral-200 dark:border-neutral-700">
<h2 class="text-xl font-bold mb-4">Historical Comments</h2>
<div class="comment mb-6 p-4 bg-neutral-100 dark:bg-neutral-700 rounded-lg">
<div class="comment-meta text-sm text-neutral-600 dark:text-neutral-400 mb-2">
<span class="font-semibold">Emaline</span>
 &mdash; September 20, 2021 at 03:18 PM
</div>
<div class="comment-content prose dark:prose-invert"><p>Eric, this was a great read. I&#x27;ve been really into the semi-forgotten term &quot;groupware&quot; lately, wanting it to come to the fore to describe priorities in the Holochain ecosystem. What you&#x27;ve got here, though, is &quot;group...where&quot; Ha! </p><p>I could also imagine maps like the one above (or other open source ones related to behavior in group settings) with stats computed over time to give rise to more qualitative reputation scores a la Neighbourhoods. More on this soon, hopefully...</p></div>
</div>
</div>
