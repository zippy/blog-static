---
title: "rails capistrano deploy script OS X to Ubuntu"
date: 2007-04-19
categories: 
  - "codingsoftware"
  - "solutions"
tags: 
  - "capistrano"
  - "deploy"
  - "os-x"
  - "rails"
  - "ubuntu"
slug: "rails-capistrano-deploy-script-os-x-to-ubuntu"
---

Ok, so in a previous post I described the rabit-hole which is switching to rails. Below's my capistrano deploy script which solves a number of problems:

1. The production server needs a mongrel cluster configuration file added.
2. Deployment requires restarting the mongrel cluster.
3. On Ubuntu the database.yaml spec has to be modified to because you need to specify a mysql socket path differently from OS X.

So here's what I added to make it work:

```
desc "Restart the web server and mongrel cluster"

task :restart, :roles => :app do
  sudo "echo 'fish'" #bogus command to make sudo work in the run command
  run "cd #{current_path} && sudo mongrel_rails cluster::restart"
  sudo "/usr/local/apache/bin/apachectl graceful"
end

desc <<-DESC
configure the mongrel cluster
DESC

task :configure_mongrel do
  run "cd #{current_path} && mongrel_rails cluster::configure -e
  development -p 9000 -a 127.0.0.1 -P #{shared_path}/pids/mongrel.pid
    -c #{current_path} -N 2 --user om --group om"
end

desc <<-DESC
configure the mongrel cluster
DESC

task :configure_database do
  db_config = "#{shared_path}/config/database.yml"
  run "cp #{db_config} #{current_path}/config/database.yml"
end

desc <<-DESC
after updating we need to add back in the mongrel configuration file so that when restart is called
it will be appropriatly launched.  We also need to update the database config file
DESC

task :after_update, :roles => :app do
  configure_mongrel
  configure_database
end
```
