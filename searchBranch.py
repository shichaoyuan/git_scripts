#!/usr/bin/env python
#python 2

import commands
import sys, os

master = 'xxx'

def search_repos(name, dir_name):
    for repo in os.listdir(dir_name):
        if os.path.isdir(repo):
            search_branch(name, repo)

def search_branch(name, repo):
    status, output = \
      commands.getstatusoutput("cd " + repo + " && git branch -a")
    if status == 0:
        if output.find(name + "\n") != -1:
            print "[" + repo + "] has branch <" + name + ">"
            commands.getstatusoutput("cd " + repo + \
                                     " && git pull && git checkout " \
                                     + name + " && git checkout " + master)
            status, output = commands.getstatusoutput(\
              "cd " + repo + " && (git diff --name-only " + name + \
              " `git merge-base " + name + " " + master + "`)")
            print output
            print "=" * 80

if __name__ == '__main__':
    if len(sys.argv) == 2:
        search_repos(sys.argv[1], ".")
