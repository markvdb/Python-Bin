#!/usr/bin/env python
# send file to evernote - 
from applescript import asrun


# hard coding evernote e-mail address
envadd="xxxxx.yyyyy@m.evernote.com" #enter you evernote mail address

fname=raw_input("Enter file name to send: ")
subject=raw_input("Enter note title: ")
title=subject


# open and reads file as string

ffile=open(fname, "r")
body=ffile.read()
ffile.close()

# composing mail -applescript
mScript = '''
  tell application "Mail"
    activate
    set newMsg to make new outgoing message with properties {{subject:"{0}", content:"{1}", visible:true}}
    tell the content of newMsg
      make new attachment with properties {{file name:"{4}"}} at after last paragraph
    end tell
    tell newMsg
      make new to recipient at end of to recipients with properties {{name:"{2}", address:"{3}"}}
    end tell
  end tell
'''

# create mail message
asrun(mScript.format(subject, body, title, envadd, 1))

