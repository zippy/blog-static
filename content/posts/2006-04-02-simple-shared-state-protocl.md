---
title: "simple shared state protocol"
date: 2006-04-02
categories: 
  - "codingsoftware"
slug: "simple-shared-state-protocl"
---

Recently it hit me that I knew of no generalized protocol for sharing the state of an abstract space among a group of computers. I did a quick google search to see if I could find anything, and after coming up dry (which doesn't mean it doesn't exist) I decided to slap one together to test out the many uses for this that were readily apparent to me (i.e. any application where multiple users must be able to collaboratively make changes, and become aware of changes made to that space in real time: chat, bulletin boards, network games, etc.) Of course there is similar stuff like [Croquet](http://opencroquet.org) that certainly does an even more complicated generalized version of this, and lots of single purpose applications, like [Subethaedit](http://www.codingmonkeys.de/subethaedit/) which must also do thisbut I haven't found other efforts that are quite as simplistic and generalized. So, I slapped together the beginings of a [protocol](/sssp) as well as a ruby based [server](/sssp/sssp.rb), and a RealBasic [based clients](/sssp/sssp_client.rbp) for [OS X](/sssp/sssp-client.dmg) and [Win](/sssp/sssp-client.exe) to test out the ideas, all of which are released under the [GPL](http://www.gnu.org/copyleft/gpl.html) license. \[tags\]collaboration,FLOSS,sharing\[/tags\]
