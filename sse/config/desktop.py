# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "SSE App",
			"color": "red",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("SSE App")
		},
		{
			"module_name": "Installation",
			"color": "red",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Installation")
		}
	]
