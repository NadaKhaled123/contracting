# Copyright (c) 2025, contracting and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ContractDocument(Document):
	pass



@frappe.whitelist()
def create_sales_invoice(customer, project, name, item, tax):
    doc = frappe.new_doc("Sales Invoice")
    doc.customer = customer
    doc.project = project
    doc.contract_document = name

    for i in item:
        doc.append("items", {
            "item_code": i.get("item_code"),
            "qty": i.get("qty"),
            "rate": i.get("rate"),
            "description": i.get("description"),
        })
    for t in tax:
        doc.append("taxes", {
            "charge_type": t.get("charge_type"),
            "account_head": t.get("account_head"),
            "description": t.get("description"),
            "rate": t.get("rate"),
            "tax_amount": t.get("tax_amount"),
            "total": t.get("total"),
            "party_type": t.get("party_type"),
            "party": t.get("party"),
            "cost_center": t.get("cost_center"),
            "tax_amount_after_discount_amount": t.get("tax_amount_after_discount_amount"),
            "base_tax_amount_after_discount_amount": t.get("base_tax_amount_after_discount_amount"),
            "base_tax_amount": t.get("base_tax_amount"),
            "base_total": t.get("base_total"),
        })
    doc.insert()
    return doc



@frappe.whitelist()
def create_purchase_invoice(supplier, project, name, item, tax):
    doc = frappe.new_doc("Purchase Invoice")
    doc.supplier = supplier
    doc.project = project
    doc.contract_document = name

    for i in item:
        doc.append("items", {
            "item_code": i.get("item_code"),
            "qty": i.get("qty"),
            "rate": i.get("rate"),
            "description": i.get("description"),
        })
    for t in tax:
        doc.append("taxes", {
            "charge_type": t.get("charge_type"),
            "account_head": t.get("account_head"),
            "description": t.get("description"),
            "rate": t.get("rate"),
            "tax_amount": t.get("tax_amount"),
            "total": t.get("total"),
            "party_type": t.get("party_type"),
            "party": t.get("party"),
            "cost_center": t.get("cost_center"),
            "tax_amount_after_discount_amount": t.get("tax_amount_after_discount_amount"),
            "base_tax_amount_after_discount_amount": t.get("base_tax_amount_after_discount_amount"),
            "base_tax_amount": t.get("base_tax_amount"),
            "base_total": t.get("base_total"),
        })
    doc.insert()
    return doc

