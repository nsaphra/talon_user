from talon.voice import Context, press, Str
import datetime

context = Context('Journal', func=lambda app, win: win.doc.endswith('.md'))

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

context.keymap({
    'new log': new_entry,
})
