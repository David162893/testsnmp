// Copyright (c) 2025, David and contributors
// For license information, please see license.txt

frappe.ui.form.on("CI Dispositivo", {

    refresh: function (frm) {
        // Agrega botón personalizado para reenvío de registros
        frm.add_custom_button(__('Reenviar Registro'), function () {
            frappe.call({
                method: "poc_snmp.poc_snmp.doctype.ci_dispositivo.ci_dispositivo.delete_last_sent",
                args: {
                    docname: frm.docname // Envía el nombre del documento actual
                },
                callback: function (r) {
                    frm.reload_doc();
                }
            });
        });
    },

    // Evento plantilla_mib - Se dispara al cambiar el campo plantilla_mib
    plantilla_mib: function (frm) {
        // Caso 1: Hay plantilla seleccionada
        if (frm.doc.plantilla_mib) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'CI Plantilla comprobacion',
                    name: frm.doc.plantilla_mib
                },
                callback: function (r) {
                    // Si la plantilla tiene comprobaciones
                    if (r.message && r.message.comprobaciones) {
                        // Limpia la tabla existente
                        frm.clear_table('comprobacion');

                        // Itera y añade cada comprobación
                        r.message.comprobaciones.forEach(function (comprobacion) {
                            let row = frm.add_child('comprobacion');
                            row.denominacion = comprobacion.denominacion;
                            row.frecuencia = comprobacion.frecuencia;
                            row.oid = comprobacion.oid;
                        });

                        frm.refresh_field('comprobacion');
                    }
                }
            });
        }
        // Caso 2: Se eliminó la plantilla
        else {
            // Limpia todas las comprobaciones
            frm.clear_table('comprobacion');
            frm.refresh_field('comprobacion');

            frappe.show_alert(__("Plantilla desvinculada - Comprobaciones eliminadas"), 3);
        }
    }
});