// Copyright (c) 2025, David and contributors
// For license information, please see license.txt

frappe.ui.form.on("CI Dispositivo", {
    refresh: function(frm) {
        frm.add_custom_button(__('Reenviar Registro'), function() {
            frappe.call({
                method: "poc_snmp.poc_snmp.doctype.ci_dispositivo.ci_dispositivo.delete_last_sent",
                args: {
                    docname: frm.docname
                },
                callback: function(r) {
                    frm.reload_doc();
                }
            });
        });
    }
});