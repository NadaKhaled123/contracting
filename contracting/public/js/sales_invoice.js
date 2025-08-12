frappe.ui.form.on("Sales Invoice", {
    refresh: function(frm){
  
        frm.set_query("party_type", "taxes", function(doc, cdt, cdn) {
            const row = locals[cdt][cdn];
        
            return {
                filters: {
                    'name': ["in",["Customer","Supplier"]]
                }
            }
        });

    }
})


