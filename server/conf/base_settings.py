"""
Base settings that we'll inherit from
"""
from decouple import config
from evennia.settings_default import *
# see documentation on python-decouple. tldr: create a config.env file at repo root, config() draws from that.
# from decouple import config

######################################################################
# Evennia base server config
######################################################################

# CHANGES: replace ADDITIONAL ANSI MAPPINGS WITH the following:
from evennia.contrib import color_markups
COLOR_ANSI_EXTRA_MAP = color_markups.CURLY_COLOR_ANSI_EXTRA_MAP + color_markups.MUX_COLOR_ANSI_EXTRA_MAP
COLOR_XTERM256_EXTRA_FG = color_markups.CURLY_COLOR_XTERM256_EXTRA_FG + color_markups.MUX_COLOR_XTERM256_EXTRA_FG
COLOR_XTERM256_EXTRA_BG = color_markups.CURLY_COLOR_XTERM256_EXTRA_BG + color_markups.MUX_COLOR_XTERM256_EXTRA_BG
COLOR_XTERM256_EXTRA_GFG = color_markups.CURLY_COLOR_XTERM256_EXTRA_GFG + color_markups.MUX_COLOR_XTERM256_EXTRA_GFG
COLOR_XTERM256_EXTRA_GBG = color_markups.CURLY_COLOR_XTERM256_EXTRA_GBG + color_markups.MUX_COLOR_XTERM256_EXTRA_GBG
COLOR_ANSI_BRIGHT_BG_EXTRA_MAP = color_markups.CURLY_COLOR_ANSI_XTERM256_BRIGHT_BG_EXTRA_MAP + color_markups.MUX_COLOR_ANSI_XTERM256_BRIGHT_BG_EXTRA_MAP
PERMISSION_HIERARCHY = ["Guest",  # note-only used if GUEST_ENABLED=True
                        "Player",
                        "Helper",
                        "Builders",
                        "Builder",
                        "Wizards",
                        "Wizard",
                        "Admin",
                        "Immortals",
                        "Immortal",
                        "Developer",
                        ]
SERVERNAME = "Ithir"
GAME_SLOGAN = "Return to Glory"
TIME_ZONE = 'America/Los_Angeles'
USE_TZ = False
TELNET_PORTS = [3000]
IDMAPPER_CACHE_MAXSIZE = 2000
EVENNIA_ADMIN = False
EMAIL_USE_TLS = True
IN_GAME_ERRORS = False
IDLE_TIMEOUT = -1
MAX_CHAR_LIMIT = 8000
DEBUG = False
CHANNEL_COMMAND_CLASS = "commands.commands.channels.ArxChannelCommand"
BASE_ROOM_TYPECLASS = "typeclasses.rooms.ArxRoom"
DEFAULT_HOME = "#30"
MULTISESSION_MODE = 1
COMMAND_DEFAULT_MSG_ALL_SESSIONS = True
ADDITIONAL_ANSI_MAPPINGS = [(r'%r', "\r\n"),]
COMMAND_DEFAULT_ARG_REGEX = r'^[ /]+.*$|$'
LOCKWARNING_LOG_FILE = ""
DEFAULT_CHANNELS = [
    {"key": "Public",
     "aliases": "pub",
     "desc": "Public discussion",
     "locks": "control: perm(Wizards);listen:all();send:all()"},
    {"key": "MUDinfo",
     "aliases": "",
     "desc": "Connection log",
     "locks": "control:perm(Immortals);listen:perm(Wizards);send:false()"}
    ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(GAME_DIR, 'server', 'evennia.db3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {'timeout': 25},
        }}

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'web.character.context_processors.consts']
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Global and Evennia-specific apps. This ties everything together so we can
# refer to app models and perform DB syncs.
INSTALLED_APPS += ('world.dominion',
                   'world.msgs',
                   'world.conditions.apps.ConditionsConfig',
                   'world.fashion.apps.FashionConfig',
                   'world.petitions.apps.PetitionsConfig',
                   'web.character',
                   'web.news',
                   'web.helpdesk',
                   'web.help_topics',
                   'cloudinary',
                   'django.contrib.humanize',
                   'markdown_deux',
                   'bootstrapform',
                   'crispy_forms',
                   )

CRISPY_TEMPLATE_PACK = 'bootstrap3'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000

######################################################################
# Game Time setup
######################################################################
TIME_FACTOR = 3.0
INVESTIGATION_PROGRESS_RATE = 0.5
INVESTIGATION_DIFFICULTY_MOD = 5

######################################################################
# Helpdesk settings
######################################################################
HELPDESK_CREATE_TICKET_HIDE_ASSIGNED_TO = True

# Queue.id for our Requests. Should normally be 1, but can be changed if you move queues around
REQUEST_QUEUE_ID = 1
BUG_QUEUE_ID = 2

######################################################################
# Dominion settings
######################################################################
BATTLE_LOG = os.path.join(LOG_DIR, 'battle.log')
DOMINION_LOG = os.path.join(LOG_DIR, 'dominion.log')
LOG_FORMAT = "%(asctime)s: %(message)s"
DATE_FORMAT = "%m/%d/%Y %I:%M:%S"
GLOBAL_DOMAIN_INCOME_MOD = 0.75

# SECRET_KEY = config('gjhdsgvucyvb23iybwei3kj3hbiewub')
# HOST_BLOCKER_API_KEY = config('HOST_BLOCKER_API_KEY')
# import cloudinary
# cloudinary.config(cloud_name=config('ithirmush'),
#                 api_key=config('951554588875841'), api_secret=config('ZlnkSDzTw12Ms39M22Gwjj8anLE'))

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-relay.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'admin@ithirmush.org'
EMAIL_HOST_PASSWORD = 'XImmort@lElfX10'
DEFAULT_FROM_EMAIL = 'admin@ithirmush.org'
ADMINS = (config('Ithir Admin', default=''), config('admin@ithirmush.org', default=''))
SEND_GAME_INDEX = config('SEND_GAME_INDEX', cast=bool, default=False)
