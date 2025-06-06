# Copyright (c) 2025, David and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CIDispositivo(Document):
	pass

@frappe.whitelist()
def delete_last_sent(docname):
	dispositivo_doc = frappe.get_doc("CI Dispositivo", docname)
	for comprobacion in dispositivo_doc.comprobacion:
		comprobacion.ultimo_envio = None
	dispositivo_doc.save()