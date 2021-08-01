# -*- coding: utf-8 -*-
#
# basic2cloze v20.5.4i8
#
# Lots of code from "Quick note and deck buttons" written by Roland Sieker
#
# Provenance from original plugin.
#   The idea, original version and large parts of this code
#   written by Steve AW <steveawa@gmail.com>
#
# Copyright: trgk (phu54321@naver.com)
# License: GNU AGPL, version 3 or later;
# See http://www.gnu.org/licenses/agpl.html

from aqt.addcards import AddCards
from aqt.editor import Editor
from anki.hooks import wrap

from .modelFinder import modelExists
from .modelSelector import targetnote_typeSelector
from .modelChanger import changenote_typeTo
from .hideTooltip import _onClozeNew
from .zap import change_value
import re


def newAddCards(self, _old):
    note = self.editor.note
    oldnote_typeName = None
    targetnote_typeName = None

    def cb1():
        nonlocal oldnote_typeName, targetnote_typeName

        targetnote_typeName = targetnote_typeSelector(note)
        if not modelExists(targetnote_typeName):
            targetModelName = None

        if targetnote_typeName is None:
            return _old(self)

        oldnote_typeame = note.note_type()["name"]
        changenote_typeTo(self.modelChooser, targetnote_typeName)
        self.editor.saveNow(cb2)

    def cb2():
        nonlocal oldnote_typeName
        self._addCards()
        changenote_typeTo(self.modelChooser, oldnote_typeName)

    self.editor.saveNow(cb1)


AddCards.addCards = wrap(AddCards.addCards, newAddCards, "around")
Editor._onCloze = wrap(Editor._onCloze, _onClozeNew, "around")
Editor. _update_duplicate_display = wrap(Editor. _update_duplicate_display,function, "around")
