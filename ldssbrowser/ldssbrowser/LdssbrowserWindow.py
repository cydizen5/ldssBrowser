# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2015 Bruce Tarro <bruce.tarro@canonical.com>
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk, WebKit # pylint: disable=E0611
import logging
logger = logging.getLogger('ldssbrowser')

from ldssbrowser_lib import Window
from ldssbrowser.AboutLdssbrowserDialog import AboutLdssbrowserDialog
from ldssbrowser.PreferencesLdssbrowserDialog import PreferencesLdssbrowserDialog

# See ldssbrowser_lib.Window.py for more details about how this class works
class LdssbrowserWindow(Window):
    __gtype_name__ = "LdssbrowserWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(LdssbrowserWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutLdssbrowserDialog
        self.PreferencesDialog = PreferencesLdssbrowserDialog

        # Code for other initialization actions should be added here.

        self.refreshbutton = self.builder.get_object("refreshbutton")
        self.urlentry = self.builder.get_object("urlentry")
        self.scrolledwindow = self.builder.get_object("scrolledwindow")
        self.toolbar = self.builder.get_object("toolbar")

        context = self.toolbar.get_style_context()
        context.add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)
    
        self.webview = WebKit.WebView()

        self.scrolledwindow.add(self.webview)
        self.webview.show()

    def on_refreshbutton_clicked(self, widget):
        self.webview.reload()

    def on_urlentry_activate(self, widget):
        url = widget.get_text() 

        self.webview.open(url)



