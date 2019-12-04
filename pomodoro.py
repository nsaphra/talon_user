from talon.voice import Key, press, Str, Context
# Commands for annotating pdfs.

ctx = Context('pomodoro')

keymap = {
    'pomodoro': Key('cmd-shift-r'),
}

ctx.keymap(keymap)
