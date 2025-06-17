# Copyright (c) 2025, David and contributors
# For license information, please see license.txt
 
import frappe
from frappe.model.document import Document

class CIRegistro(Document):

    def before_insert(self):
        # 1. Establece marca de tiempo y dirección IP
        self.fecha = frappe.utils.now_datetime() 
        if frappe.request:
            self.ip = frappe.local.request_ip
            
        # 2. Obtiene el dispositivo relacionado
        dispositivo_doc = frappe.get_doc("CI Dispositivo", self.dispositivo)
        
        # 3. Actualiza último envío en el dispositivo padre
        dispositivo_doc.ultimo_envio = self.fecha
        
        # 4. Sincroniza timestamps para comprobaciones coincidentes
        # Crea diccionario para búsqueda eficiente
        oids_registro = {c.oid: c for c in self.comprobacion}

        for comprobacion in dispositivo_doc.comprobacion:
            if comprobacion.oid in oids_registro:
                comprobacion.ultimo_envio = self.fecha
                comprobacion.ultimo_valor = oids_registro[comprobacion.oid].valor

        dispositivo_doc.save()