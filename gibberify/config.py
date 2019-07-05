# Copyright 2019-2019 the gibberify authors. See copying.md for legal info.

"""
Configuration file
"""

# natural languages used for syllable generation and everything else
__real_langs__ = (
                      'en',     # english
                      'it',     # italian
                      'de',     # german
                      'fr',     # french
                      'ru',     # russian
                      'es',     # spanish
                      'nl',     # dutch
                      'ca',     # catalan
                      'el',     # greek
                      'et',     # estonian
                      'is',     # icelandic
                      'lt',     # lithuanian
                      'nb',     # norwegian
                      'pt',     # portuguese
                      'sk',     # slovak
                      )

# fake languages and their relative settings
__gib_langs__ = {
    'orc': {
        'pool': ['ru', 'de']
    },
    'elv': {
        'pool': ['fr', 'en']
    },
    'dwa': {
        'pool': ['it', 'de'],
    },
}
