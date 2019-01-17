# An indexed clipboard.
# If a keyword is included it will save as a clipping under that keyword,
# otherwise behaves as normal copy and paste.
from talon.voice import Key, press, Str, Context
from talon import clip
from .talon_community.utils import *

ctx = Context('clipboard')

def copy_selection(m):
    with clip.capture() as sel:
        press('cmd-c')
    if len(m._words) > 1:
        key = ' '.join(parse_words(m))
        value = sel.get()
        keymap['paste %s' % key] = value
        ctx.keymap(keymap)
        ctx.reload()
    else:
        clip.set(sel.get())

keymap = {
    'paste': Key('cmd-v'),
    'clip [<dgndictation>]': copy_selection,
}

ctx.keymap(keymap)
