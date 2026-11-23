import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
	if not frappe.db.exists("DocType", "Inpatient Deposit Settings"):
		return
	create_custom_fields(
		{
			"Inpatient Deposit Settings": [
				{
					"fieldname": "custom_inpatient_services_section",
					"label": "Inpatient Service Catalog",
					"fieldtype": "Section Break",
					"insert_after": "daily_inpatient_charge_amount",
				},
				{
					"fieldname": "daily_services",
					"label": "Recurring Inpatient Services",
					"fieldtype": "Table",
					"options": "Inpatient Service Configuration",
					"insert_after": "custom_inpatient_services_section",
				},
				{
					"fieldname": "misc_services",
					"label": "Miscellaneous Inpatient Services",
					"fieldtype": "Table",
					"options": "Inpatient Service Configuration",
					"insert_after": "daily_services",
				},
			],
		},
		update=True,
	)
	frappe.clear_cache(doctype="Inpatient Deposit Settings")
