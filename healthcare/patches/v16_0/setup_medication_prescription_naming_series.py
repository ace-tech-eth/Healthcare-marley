import frappe


def execute():
	try:
		frappe.reload_doc("healthcare", "doctype", "medication_prescription")
	except Exception:
		frappe.log_error(frappe.get_traceback(), "Could not reload medication_prescription")

	frappe.clear_cache(doctype="Medication Prescription")
