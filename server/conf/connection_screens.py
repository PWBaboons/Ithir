# -*- coding: utf-8 -*-
"""
Connection screen

Texts in this module will be shown to the user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets.UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = \
"""{w=============================================================={n
             Welcome to {gIthirMUSH{n

 If you have an existing account, connect to it by typing:
      {wconnect <username> <password>{n
      
 {rWe are not currently ready for active characters. Please come
 back at the end of December when we will be opening for our alpha
 phase of development.
 
 Thanks!
 -Ithir Staff{n
 
 {gIf you are a member of our discord group and are here to create
 your roster or OC character, please log in using the command {wguest{n
 {gto begin the pre-alpha character creation process.{n
 
{w=============================================================={n"""

##"""{b=============================================================={n
## Welcome to {g%s{n, version %s!
##
## If you have an existing account, connect to it by typing:
##      {wconnect <username> <password>{n
## If you need to create an account, type (without the <>'s):
##      {wcreate <username> <password>{n
##
## If you have spaces in your username, enclose it in quotes.
## Enter {whelp{n for more info. {wlook{n will re-show this screen.
##{b=============================================================={n""" \
## % (settings.SERVERNAME, utils.get_evennia_version())
