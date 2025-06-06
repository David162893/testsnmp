# Copyright (c) 2025, David and contributors
# For license information, please see license.txt
 
import frappe
from frappe.model.document import Document
 
class CIRegistro(Document):
    def before_insert(self):
        self.fecha = frappe.utils.now_datetime()
        if frappe.request:
            self.ip = frappe.local.request_ip
        dispositivo_doc = frappe.get_doc("CI Dispositivo", self.dispositivo)
        dispositivo_doc.ultimo_envio = frappe.utils.now_datetime()
        for comprobacion in dispositivo_doc.comprobacion:
            for comprobacion_registro in self.comprobacion:
                if comprobacion.oid == comprobacion_registro.oid:
                    comprobacion.ultimo_envio = frappe.utils.now_datetime()
                    dispositivo_doc.save()
                    break
