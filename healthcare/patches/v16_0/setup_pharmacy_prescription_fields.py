import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
	reload_pharmacy_doctypes()
	create_custom_fields(pharmacy_custom_fields(), update=True)
	for doctype in ["Drug Prescription", "Sales Invoice", "Medication Prescription"]:
		frappe.clear_cache(doctype=doctype)


def reload_pharmacy_doctypes():
	for doctype in ["drug_prescription", "medication_prescription"]:
		try:
			frappe.reload_doc("healthcare", "doctype", doctype)
		except Exception:
			frappe.log_error(frappe.get_traceback(), f"Could not reload {doctype}")


def pharmacy_custom_fields():
	return {
		"Drug Prescription": [
			{
				"fieldname": "frequency",
				"label": "Frequency",
				"fieldtype": "Data",
				"insert_after": "dosage",
				"in_list_view": 1,
			},
			{
				"fieldname": "route_of_admin",
				"label": "Route of Administration",
				"fieldtype": "Data",
				"insert_after": "frequency",
				"in_list_view": 1,
			},
			{
				"fieldname": "qty",
				"label": "Quantity",
				"fieldtype": "Float",
				"insert_after": "period",
				"in_list_view": 1,
				"default": "1",
			},
		],
		"Sales Invoice": [
			{
				"fieldname": "patient",
				"label": "Patient",
				"fieldtype": "Link",
				"options": "Patient",
				"insert_after": "naming_series",
			},
			{
				"fieldname": "patient_name",
				"label": "Patient Name",
				"fieldtype": "Data",
				"fetch_from": "patient.patient_name",
				"insert_after": "patient",
				"read_only": 1,
			},
			{
				"fieldname": "medication_prescription",
				"label": "Medication Prescription",
				"fieldtype": "Link",
				"options": "Medication Prescription",
				"insert_after": "patient_name",
				"read_only": 1,
			},
			{
				"fieldname": "machine_type",
				"label": "Machine Type",
				"fieldtype": "Data",
				"insert_after": "medication_prescription",
				"default": "pharmacy",
			},
			{
				"fieldname": "select_machine",
				"label": "Select Machine",
				"fieldtype": "Data",
				"insert_after": "machine_type",
			},
			{
				"fieldname": "tin",
				"label": "TIN",
				"fieldtype": "Data",
				"insert_after": "select_machine",
			},
			{
				"fieldname": "ref_practitioner",
				"label": "Referring Practitioner",
				"fieldtype": "Link",
				"options": "Healthcare Practitioner",
				"insert_after": "customer",
			},
		],
	}
