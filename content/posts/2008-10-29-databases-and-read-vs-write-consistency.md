---
title: "databases and read vs. write consistency"
date: 2008-10-29
categories: 
  - "codingsoftware"
  - "geeky"
slug: "databases-and-read-vs-write-consistency"
---

Have just read an excellent blog post on ["dumb databases"](http://blog.labnotes.org/2007/09/20/read-consistency-dumb-databases-smart-services/) and the issue of read vs. write consistency. My own [mesh & churn](http://openmoney.info/techne/overview.html) for open money comes out of the same realizations that in a distributed environment the way to handle many many issues is to put the responsibility on the reader to verify the validity of the data.
