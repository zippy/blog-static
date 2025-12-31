---
title: "Gnucash & Tiger"
date: 2006-03-23
categories: 
  - "solutions"
slug: "gnucash-tiger"
---

Another installment in the collective tech-support arena: [Gnucash](http://www.gnucash.org/) wasn't working under OS X Tiger (10.4.5); whenever I tried to run a report I kept getting the following cryptic error message in my terminal: `dyld: Symbol not found: _program_invocation_short_name Referenced from: /sw/lib/libgnome.32.dylib Expected in: flat namespace` A google search didn't reveal anything with those error messages as keywords, so it was up to me to find the answer. Fourtunately my first stab in the dark worked! I did a `fink selfupdate` and then `fink update-all` (I'm using [FinkCommander](http://finkcommander.sourceforge.net/) so I did those fink commands from the **Source** menu). I'm guessing that when I reinstalled gnucash after updating to Tiger, there were still some bugs in several of the libraries that were fixed by the fink update. Be forewarned that this take a loooong time to complete (overnight for me on my G4 powerbook). \[tags\]gnucash,fink,FinkCommander\[/tags\]
