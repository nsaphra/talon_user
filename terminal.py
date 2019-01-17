from talon.voice import Word, Key, Context, Str, press
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

from .talon_community.utils import numerals, parse_words, text

# TODO: move application specific commands into their own files: apt-get, etc

terminals = ("com.apple.Terminal", "com.googlecode.iterm2")
ctx = Context("personal_terminal", func=lambda app, win: any(t in app.bundle for t in terminals))

mapping = {"semicolon": ";", r"new-line": "\n", r"new-paragraph": "\n\n"}

ctx.keymap({
    'run long job': 'longjob -28day -nobackground -c ',
    'shell screen attach': 'screen -dr ',
    'shell screen new': 'screen -S ',
    'shell jupiter notebook': 'jupyter notebook ',
})
