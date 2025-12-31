---
title: "We: Social Spaces for Collaboration"
date: 2022-07-26
categories: 
  - "codingsoftware"
  - "collective-intelligence"
  - "cc"
  - "geeky"
slug: "we-social-spaces-for-collaboration"
---

Say that we agree to define collaboration as a group’s ability to coordinate effort to produce some work output.  I believe that the effectiveness of collaboration improves in direct proportion to:

- how easy it is to create social spaces in which to do that coordination, 
- the degree of composability of those social spaces (especially nesting)
- the variety and utility of the affordances provided in those spaces.

Together let’s call these the claims of **Collaborative Power**.

Let’s look at some examples:

#### Version control

Git enables easily creating a social space for coordinating work on a code base. It does this by providing affordances such as; committing, diffing, branching and merging, to assist in that coordination. The affordance of branching is itself an example of Collaborative Power. Within the social space of a code repository, a branch also creates a secondary, simple and secure, social space for further collaboration, or a sub-space. It’s a semantically separate and differentiated place for a sub-group (perhaps of one) to work on the code. This was Git’s “[Killer Feature](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)”, branching made trivially cheap.

#### Channel based messaging

Tools like Discord, Slack and Mattermost make it trivially easy to create the high-level social space of a “Team” or “Server”, and within that, semantically tagged sub-spaces of chat channels. This is analogous to the Repo and Branch levels of VCS systems but for messaging.  The ease and low cost of creating social spaces at both of these levels, and the affordances in those spaces (video/audio chat, screen-sharing, bots, etc) make these tools easy to adopt and continue to use. 

## Generalized Collaborative Power

Is it possible to generalize tooling for Collaborative Power? In other words, what technical affordances would be necessary for creating generalized sub-spaces within a high-level social context? 

Imagine being able to create a social space for collaborative work-groups, where what is made trivially easy to instantiate and assemble inside the space, is not one single secondary type of sub-space (i.e. a branch as in a VCS, or a channel in a messaging system) but the mini-apps of your choice, within a simple composible frame.

#### Enter We

_We_ is a new Holochain app we’re building over at [Lightningrod Labs](https://lightningrodlabs.org/) that provides this heightened Collaborative Power. _We_ makes it trivially easy for users to create high-level social spaces and add “applets” to them. These applets provide the functionality for the exact types of collaboration intended by the group.

The UI looks a little like Slack or Discord. There’s a left-hand bar showing your “_we_\-groups”, but instead of the right hand being the channel text stream, there is a secondary bar of “Applets” that have been instantiated into that social space, with the main right-hand window space displaying the UI of one or more of those applets.  Here’s a screenshot showing a social space with the Notebooks applet active, which provides a real-time collaborative markdown-editing:

![](/blog/images/we_2.png)

The power of _We_ comes from how easy it is from both a user's and a developer’s perspective to add new collaboration affordances.  End users simply pick them directly in the Applet Library:

![](/blog/images/we_1.png) For Holochain hApp developers, this addition makes it very simple to compile, build, and publish to the DevHub their existing hApps as “_we_\-applets”.  Then any such hApps become instantly available for composing into _We_ social spaces.

#### Distributed Groupware

In a way, _We_ might “just” look like another attempt at a [groupware](https://en.wikipedia.org/wiki/Collaborative_software) tool, but there are few things things that set it apart:

- **Generality and Openness**: _We_ makes no assumption about the content of collaboration. The affordances of the social spaces are entirely customizable by each group according to the group’s purpose.  If a group needs a new social tooling, it can just be added in.
- **Decentralization**: Although, as mentioned, cheap branching is a key feature of Git, its primary design goal was to make possible a fully distributed version control for the linux operating system, such that no central authority could possibly take ownership of its development. This design is arguably Git’s true super-power; and likewise, because _We_ is built on Holochain, it also provides generalized group-forming capability in the fully distributed context. No central servers or infrastructure is necessary. Simply install the [Holochain Launcher](https://github.com/holochain/launcher/releases/tag/v0.4.10) and then pick “_We_” from the App Library.
- **Agent-centricity**: As a consequence of being built on Holochain, _We_’s core intent of group collaboration happens from an architecture of empowered agency. Individuals can start groups on-the-fly without request from any authority. Within groups individuals must opt-in to any applet that other agents propose for the group.

#### Where “_We_” is going…

The initial release of _We_ demonstrates the key Collaborative Power functionality of adding new applets into social spaces on-the-fly. The next steps come from adding compositional grammatics to applets. These grammatics exist at a few levels:  

1. Visual: the ability to visually compose applet UIs into complex dashboards/layouts instead of just toggling between monolithic UIs.
2. Templating: the ability to create a preset menu of applets that work well together and are easily installable as a group, including their layouts.
3. Functional (the 4 “F”s); the ability to evolve social spaces over time:
    1. **Forge**: meaning the visual and templating for new group formation. 
    2. **Federate**: inter-group protocols and connections that allow groups membraned interactions
    3. **Fork**: easy spinning up of new groups from existing groups, including data transferability.
    4. **Fuse**: easy merging of groups together. 

Subsequent releases of _We_ will focus on adding in all these grammatical elements, listed above.

So, back to the claims of Collaborative Power:

Collaboration effectiveness improves in direct proportion to both how easy it is to create nested social spaces in which to do that coordination, and the power of the affordances in those spaces to be recomposed overtime

_We_ provides a significant upgrade to the ease of assembling affordances in social spaces.  And it does so while upholding the significant properties of Generality, Decentralization, Agent-Centricity along with providing explicit grammatics for visual assembly, templating and evolution of social spaces.  

We hope to see you in _We_! 

P.S: For the technically inclined, hop on over to our [github repo](https://github.com/lightningrodlabs/we) and check out the instructions on how to convert your regular hApp to be _We_ ready!

<div class="historical-comments mt-8 pt-8 border-t border-neutral-200 dark:border-neutral-700">
<h2 class="text-xl font-bold mb-4">Historical Comments</h2>
<div class="comment mb-6 p-4 bg-neutral-100 dark:bg-neutral-700 rounded-lg">
<div class="comment-meta text-sm text-neutral-600 dark:text-neutral-400 mb-2">
<span class="font-semibold">Terry</span>
 &mdash; July 26, 2022 at 09:33 PM
</div>
<div class="comment-content prose dark:prose-invert"><p>You need a 5th F which is for Filter. One of main issues with apps and apps talking to other apps is transactions that fall outside boundaries and would need to be blocked/edited<br>as per your membranes tech. I suggest a rules based engine that can oversee all tx and monitor them whereupon if they fall outside the defined parameters (within the engine) they are frozen and moving into a Workspace(s). Feedback can be given to the user/app that the tx is being held with reason/error. The management of these Workspace(s) can be then be coordinated with some manual intervention if required with full edit history.</p></div>
</div>
<div class="comment mb-6 p-4 bg-neutral-100 dark:bg-neutral-700 rounded-lg">
<div class="comment-meta text-sm text-neutral-600 dark:text-neutral-400 mb-2">
<span class="font-semibold">Moritz</span>
 &mdash; July 28, 2022 at 01:27 PM
</div>
<div class="comment-content prose dark:prose-invert"><p>That&#x27;s pretty much what Holochain already affords: validation.</p></div>
</div>
</div>
