import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
	create_custom_fields(
		{
			"Item": [
				{
					"fieldname": "custom_pharmacy_configuration_section",
					"label": "Pharmacy Configuration",
					"fieldtype": "Section Break",
					"insert_after": "item_group",
				},
				{
					"fieldname": "custom_available_in_pharmacy",
					"label": "Available in Pharmacy Mapping",
					"fieldtype": "Check",
					"insert_after": "custom_pharmacy_configuration_section",
					"default": "0",
				},
			],
		},
		update=True,
	)
	ensure_drug_item_group()
	frappe.clear_cache(doctype="Item")
	frappe.clear_cache(doctype="Item Group")


def ensure_drug_item_group():
	if frappe.db.exists("Item Group", "Drug"):
		return
	root = frappe.db.get_value("Item Group", {"is_group": 1, "parent_item_group": ""}, "name")
	if not root:
		root = frappe.db.get_value("Item Group", {"is_group": 1}, "name") or "All Item Groups"
	frappe.get_doc(
		{
			"doctype": "Item Group",
			"item_group_name": "Drug",
			"parent_item_group": root,
			"is_group": 0,
		}
	).insert(ignore_permissions=True)
