# Copyright (c) 2025, David and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class CIDispositivo(Document):
	def validate(self):
		if self.plantilla_mib and not self._doc_before_save:
			plantilla = frappe.get_doc("CI Plantilla Comprobacion", self.plantilla_mib)
			for comprobacion in plantilla.ci_comprobacion:
				self.append("ci_comprobacion", {
					"denominacion": comprobacion.denominacion,
					"frecuencia": comprobacion.frecuencia,
					"oid": comprobacion.oid
				})

@frappe.whitelist()
def delete_last_sent(docname):
	dispositivo_doc = frappe.get_doc("CI Dispositivo", docname)
	for comprobacion in dispositivo_doc.comprobacion:
		comprobacion.ultimo_envio = None
	dispositivo_doc.save()