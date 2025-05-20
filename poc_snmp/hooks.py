app_name = "poc_snmp"
app_title = "Poc Snmp"
app_publisher = "David"
app_description = "Prueba de concepto control impresoras snmp"
app_email = "drodriguez@ctgalega.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "poc_snmp",
# 		"logo": "/assets/poc_snmp/logo.png",
# 		"title": "Poc Snmp",
# 		"route": "/poc_snmp",
# 		"has_permission": "poc_snmp.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/poc_snmp/css/poc_snmp.css"
# app_include_js = "/assets/poc_snmp/js/poc_snmp.js"

# include js, css files in header of web template
# web_include_css = "/assets/poc_snmp/css/poc_snmp.css"
# web_include_js = "/assets/poc_snmp/js/poc_snmp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "poc_snmp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "poc_snmp/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "poc_snmp.utils.jinja_methods",
# 	"filters": "poc_snmp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "poc_snmp.install.before_install"
# after_install = "poc_snmp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "poc_snmp.uninstall.before_uninstall"
# after_uninstall = "poc_snmp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "poc_snmp.utils.before_app_install"
# after_app_install = "poc_snmp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "poc_snmp.utils.before_app_uninstall"
# after_app_uninstall = "poc_snmp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "poc_snmp.notifications.get_notification_config"

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"poc_snmp.tasks.all"
# 	],
# 	"daily": [
# 		"poc_snmp.tasks.daily"
# 	],
# 	"hourly": [
# 		"poc_snmp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"poc_snmp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"poc_snmp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "poc_snmp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "poc_snmp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "poc_snmp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["poc_snmp.utils.before_request"]
# after_request = ["poc_snmp.utils.after_request"]

# Job Events
# ----------
# before_job = ["poc_snmp.utils.before_job"]
# after_job = ["poc_snmp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"poc_snmp.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

