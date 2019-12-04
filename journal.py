from talon.voice import Key, press, Str, Context, Rule, ContextGroup
from .talon_community.utils import (
    parse_words_as_integer,
    parse_words,
    numeral_map,
    numerals,
    optional_numerals,
    text,
    m_to_number,
)
import datetime

from .talon_community.misc.speech_toggle import journal

# context = Context('journal')#, group=ContextGroup('dictation'))#, func=lambda app, win: win.doc.endswith('.md'))

atom_hotkey = "cmd-shift-ctrl-alt-t"

def new_entry(m):
    press('cmd-down') # Go to end of first line of the file
    press('return')
    press('return')
    press('return')

    # Return to just after the date entry
    press('up')

    Str('# ')(None)
    Str(datetime.date.today().isoformat())(None) # Add the current date

    # Create spacing from any previous entries
    press('return')
    # Enter start of new list item
    Str('* ')(None)

def new_to_do(m):
    press('return')
    Str('- [ ] ')(None)

def execute_atom_command(command, parameters=None):
    press(atom_hotkey)
    press(command)
    if parameters:
        Str(parameters)(None)
        press("enter")

def get_first_word(m):
    return str(m.dgndictation[0]._words[0])

def mark_as_done(m):
    Key("cmd-left")
    Key("right")
    Key("right")
    Key("right")
    Key("right")
    Key("delete")
    Key("x")

def bullet(m):
    press('return')
    Str('* ')(None)

journal.keymap({
    'new log': new_entry,
    'to do new': new_to_do,
    'bullet': bullet,
    'to do done': mark_as_done,
})
