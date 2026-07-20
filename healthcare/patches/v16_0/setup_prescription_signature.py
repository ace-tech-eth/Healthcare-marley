import frappe


def execute():
	for doctype in ["healthcare_practitioner", "prescription_signature", "medication_prescription"]:
		try:
			frappe.reload_doc("healthcare", "doctype", doctype)
		except Exception:
			frappe.log_error(frappe.get_traceback(), f"Could not reload {doctype}")

	for doctype in ["Healthcare Practitioner", "Prescription Signature", "Medication Prescription"]:
		frappe.clear_cache(doctype=doctype)
