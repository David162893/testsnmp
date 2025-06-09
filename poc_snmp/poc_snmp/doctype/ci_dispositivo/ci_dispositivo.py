# Copyright (c) 2025, David and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CIDispositivo(Document):
    pass

@frappe.whitelist()
def delete_last_sent(docname):
    # Resetea el campo ultimo_envio en todas las comprobaciones
    doc = frappe.get_doc("CI Dispositivo", docname)
    
    # Actualiza cada comprobación
    for comp in doc.comprobacion:
        comp.ultimo_envio = None

    doc.save() 

@frappe.whitelist()
def cargar_comprobaciones(plantilla_name):
    # Obtiene comprobaciones desde plantilla
    if not plantilla_name:
        return None
        
    plantilla = frappe.get_doc("CI Plantilla comprobacion", plantilla_name)
    return plantilla.comprobaciones if plantilla else None