import sys
# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.append('C:/Users/100707158/Atom Html Porjects/SQ Final/SOFE_QUAILTY_FINAL/Calibre/src/calibre/gui2/actions')

#from choose_library import select_all
from .calibre.gui2.actions.choose_library import select_all
import unittest

print("testing")
# def select_all(self):
#     self.gui.library_view.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
#     pick = self.gui.library_view.model().rowCount(None)
#     for i in range(pick):
#         self.gui.library_view.selectRow(i)
