from anki.hooks import runHook


def changenote_typeTo(modelChooser, targetnote_typeName, zap):
    """Change to note_type with name targetModelName"""
    # Mostly just a copy and paste from the bottom of onModelChange()
    m = modelChooser.deck.models.by_name(targetnote_typeName)
    modelChooser.deck.conf["curModel"] = m["id"]
    cdeck = modelChooser.deck.decks.current()
    cdeck["mid"] = m["id"]
    modelChooser.deck.decks.save(cdeck)
    runHook("currentModelChanged")
    modelChooser.mw.reset()
