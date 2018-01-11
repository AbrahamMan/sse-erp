# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sse"
app_title = "SSE App"
app_publisher = "Terry Zhuo"
app_description = "SSE Custom App"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "terryzhuo@skysolarenergy.com.au"
app_license = "MIT"

fixtures = ["Custom Field", "Custom Script", "Property Setter", "Print Format"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sse/css/sse.css"
# app_include_js = "/assets/sse/js/sse.js"

# include js, css files in header of web template
# web_include_css = "/assets/sse/css/sse.css"
# web_include_js = "/assets/sse/js/sse.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sse.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sse.install.before_install"
# after_install = "sse.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sse.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sse.tasks.all"
# 	],
# 	"daily": [
# 		"sse.tasks.daily"
# 	],
# 	"hourly": [
# 		"sse.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sse.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sse.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sse.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sse.event.get_events"
# }

