---
title: "Upgrading postgres on Snow Leopard (Mac OS X 10.6)"
date: 2009-11-10
categories: 
  - "codingsoftware"
  - "geeky"
  - "solutions"
tags: 
  - "10-6"
  - "gem"
  - "mac-os-x"
  - "postgres"
  - "postgresql"
  - "rails"
  - "snow-leopard"
slug: "upgrading-postgres-to-snow-leopard"
---

Well, I too have gone down the rabbit hole of having to upgrade compiled-from-source apps to 64bit architecture after moving to Snow Leopard.  The hardest by far was postgres.  The sad thing is that 32bit version works just fine, but the adapter gems for rails don't, hence the need for the recompile.

Mostly I followed this [blog post](http://devoh.com/posts/2009/08/postgresql-snow-leopard), but it assumes that you had previously installed postgres using [his instructions for Leopard](http://devoh.com/posts/2008/10/installing-postgresql-on-mac-os-x-10.5-leopard) which I hadn't.

My previous installation was at /usr/local/postgres and these instructions end up installing it at /usr/local/pgsql, so my task also includes getting the data from my previous installation to the new on.

I also took some some hints from [this post](http://community.invisionpower.com/topic/292849-installing-postgresql-server-on-mac-os-x-snow-leopard/  ).

Here's the blow by blow:

Make a backup of all my data from the 32bit version:

```
pg_dumpall > /tmp/32-bit-dump.sql

```

Switch to super user, make a directory for the source (if you haven't already), download and extract it:

```
sudo su
mkdir /usr/local/src
cd /usr/local/src
curl -O http://ftp9.us.postgresql.org/pub/mirrors/postgresql/source/v8.3.8/postgresql-8.3.8.tar.gz
tar -zvxf postgresql-8.3.8.tar.gz
rm postgresql-8.3.8.tar.gz

```

Now configure, make and install it:

```
cd postgresql-8.3.8
./configure --enable-thread-safety --with-bonjour
make
make install

```

Then I followed the instructions from the above mentioned blog on how to make a postgres user, but I did them in a different terminal window because remember the other one we were logged in as root:

"First, you'll need to find an unused user and group ID. Use the following commands to list the IDs for the users and groups on your system."

```
dscl . -list /Groups PrimaryGroupID | awk '{print $2}' | sort -n
dscl . -list /Users UniqueID | awk '{print $2}' | sort -n

```

"For the purposes of this tutorial, let's assume an ID of 113 for both the user and the group. Since the convention is to prefix system accounts with an underscore, use the following commands to create a user called \_postgres:"

```
sudo dscl . create /Users/_postgres UniqueID 113
sudo dscl . create /Users/_postgres PrimaryGroupID 113
sudo dscl . create /Users/_postgres NFSHomeDirectory /usr/local/pgsql/
sudo dscl . create /Users/_postgres RealName "PostgreSQL Server"
sudo dscl . create /Users/_postgres Password "*"
sudo dscl . append /Users/_postgres RecordName postgres

```

"Then, create the \_postgres group:"

```
sudo dscl . create /Groups/_postgres
sudo dscl . create /Groups/_postgres PrimaryGroupID 113
sudo dscl . append /Groups/_postgres RecordName postgres
sudo dscl . create /Groups/_postgres RealName "PostgreSQL Users"

```

So at this point the binaries are installed and there's a user to run it under, but I needed to initialize a new database and copy back in my saved data. First create the data and log directories and set perms:

```
sudo mkdir /usr/local/pgsql/data
sudo chown postgres:postgres /usr/local/pgsql/data
sudo mkdir /usr/local/pgsql/log
sudo chown postgres:postgres /usr/local/pgsql/log

```

Then I logged in as the \_postgres user:

```
sudo su
su - _postgres

```

And initialize database files and start up the database:

```
/usr/local/pgsql/bin/initdb -E UTF8 -D /usr/local/pgsql/data/
/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data/ -l /usr/local/pgsql/log/postgresql.log start

```

Finally I restored the data from my initial pg\_dumpall

```
/usr/local/pgsql/bin/psql -U postgres  -f /tmp/32-bit-dump.sql

```

I've also added these lines into my .profile to add the commands to my path and to simplify starting and stopping the database:

```
export PATH=$PATH:/usr/local/pgsql/bin
export MANPATH=$MANPATH:/usr/local/pgsql/man
alias pg_stop='sudo -u postgres pg_ctl -D /usr/local/pgsql/data stop'
alias pg_start='sudo -u postgres pg_ctl -D /usr/local/pgsql/data -l /usr/local/pgsql/log/posgtres.log start'

```

And then finally I could install the postgres rails gem (which was the whole point of this silly excercise):

```
sudo env ARCHFLAGS="-arch x86_64" gem install pg

```
