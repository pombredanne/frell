#!/usr/bin/env python
import sys
import logging
from error import debugExceptHook

sys.excepthook = debugExceptHook

log = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)

from model4 import Action

test = Action({ "action" : "create", 
                "tag" : "symlink",
                "values" : [ {"path/to/file" : "path/to/symlink"},
                             {"path/to/next" : "path/to/symlink2"}
                        ]   
                })

print "Action type:", test.action
print "Tag type:", test.tag.tag
print "Values", test.values
test.action = 'delete'
test.tag = 'file'
test.values = [ { "file" : "path/to/symlink" } ]
print "Action type:", test.action
print "Tag type:", test.tag.tag
print "Values", test.values
