import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
	create_custom_fields(
		{
			"Item Price": [
				{
					"fieldname": "custom_pricing_charges_section",
					"label": "Pricing Charges",
					"fieldtype": "Section Break",
					"insert_after": "price_list_rate",
				},
				{
					"fieldname": "custom_vat_percentage",
					"label": "VAT Percentage",
					"fieldtype": "Percent",
					"insert_after": "custom_pricing_charges_section",
					"default": "0",
				},
				{
					"fieldname": "custom_vat_inclusive",
					"label": "VAT Inclusive",
					"fieldtype": "Check",
					"insert_after": "custom_vat_percentage",
					"default": "0",
				},
				{
					"fieldname": "custom_service_charge_percentage",
					"label": "Service Charge Percentage",
					"fieldtype": "Percent",
					"insert_after": "custom_vat_inclusive",
					"default": "0",
				},
			],
		},
		update=True,
	)
	frappe.clear_cache(doctype="Item Price")
