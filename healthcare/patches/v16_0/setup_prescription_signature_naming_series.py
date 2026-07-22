import frappe


def execute():
	try:
		frappe.reload_doc("healthcare", "doctype", "prescription_signature")
	except Exception:
		frappe.log_error(frappe.get_traceback(), "Could not reload prescription_signature")

	frappe.clear_cache(doctype="Prescription Signature")
