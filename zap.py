from aqt.editor import Editor



def change_value(cloze_hint):
    cloze_hint.append(NoteFieldsCheckResult.NOTETYPE_NOT_CLOZE)


def function():
    cloze_hint = []
    change_value(cloze_hint)
    print(cloze_hint["none"])

function()
