
__license__   = 'GPL v3'
__copyright__ = '2010, Kovid Goyal <kovid@kovidgoyal.net>'
__docformat__ = 'restructuredtext en'

import os
from collections import defaultdict
from functools import partial
from qt.core import QApplication, QDialog, QPixmap, QTimer

from calibre import as_unicode, guess_type
from calibre.constants import iswindows
from calibre.ebooks import BOOK_EXTENSIONS
from calibre.ebooks.metadata import MetaInformation
from calibre.gui2 import (
    choose_dir, choose_files, error_dialog, gprefs, info_dialog, question_dialog,
    warning_dialog
)
from calibre.gui2.actions import InterfaceAction
from calibre.gui2.dialogs.add_empty_book import AddEmptyBookDialog
from calibre.gui2.dialogs.confirm_delete import confirm
from calibre.gui2.dialogs.progress import ProgressDialog
from calibre.ptempfile import PersistentTemporaryFile
from calibre.utils.config_base import tweaks
from calibre.utils.filenames import ascii_filename, make_long_path_useable
from calibre.utils.icu import sort_key
from polyglot.builtins import iteritems, range, string_or_bytes

class SelectAllAction(InterfaceAction):

    name = 'Select All'
    action_spec = (_('Select All'), 'add_book.png',
            _('Select all files in the directory')
            , None)
    action_type = 'current'
    action_add_menu = True
    action_menu_clone_qaction = _('Add books from a single directory')

    def genesis(self):
        pm = self.qaction.menu()
        cm = partial(self.create_menu_action, pm)
        if ismacos:
            pm.addAction(QIcon(I('config.png')), _('Preferences'), self.do_config)
        cm('welcome wizard', _('Run Welcome wizard'),
                icon='wizard.png', triggered=self.gui.run_wizard)
        cm('plugin updater', _('Get plugins to enhance calibre'),
                icon='plugins/plugin_updater.png', triggered=self.get_plugins)
        if not DEBUG:
            pm.addSeparator()
            cm('restart', _('Restart in debug mode'), icon='debug.png',
                    triggered=self.debug_restart, shortcut='Ctrl+Shift+R')

        self.preferences_menu = pm
        for x in (self.gui.preferences_action, self.qaction):
            x.triggered.connect(self.do_config)

    def get_plugins(self):
        from calibre.gui2.dialogs.plugin_updater import (PluginUpdaterDialog,
                FILTER_NOT_INSTALLED)
        d = PluginUpdaterDialog(self.gui,
                initial_filter=FILTER_NOT_INSTALLED)
        d.exec_()
        if d.do_restart:
            self.gui.quit(restart=True)

    def do_config(self, checked=False, initial_plugin=None,
            close_after_initial=False):
        if self.gui.job_manager.has_jobs():
            d = error_dialog(self.gui, _('Cannot configure'),
                    _('Cannot configure while there are running jobs.'))
            d.exec_()
            return
        if self.gui.must_restart_before_config:
            do_restart = show_restart_warning(_('Cannot configure before calibre is restarted.'))
            if do_restart:
                self.gui.quit(restart=True)
            return
        d = Preferences(self.gui, initial_plugin=initial_plugin,
                close_after_initial=close_after_initial)
        d.run_wizard_requested.connect(self.gui.run_wizard,
                type=Qt.ConnectionType.QueuedConnection)
        d.exec_()
        if d.do_restart:
            self.gui.quit(restart=True)

    def debug_restart(self, *args):
        self.gui.quit(restart=True, debug_on_restart=True)
