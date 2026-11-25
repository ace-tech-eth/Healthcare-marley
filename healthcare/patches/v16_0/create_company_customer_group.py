import frappe


GROUP_NAME = "Companies"
FALLBACK_GROUP_NAME = "Company Customers"
ROOT_GROUP = "All Customer Groups"


def execute():
	if not frappe.db.exists("Customer Group", ROOT_GROUP):
		frappe.throw(f"Required root Customer Group {ROOT_GROUP} does not exist")

	existing = frappe.db.get_value(
		"Customer Group",
		{"customer_group_name": GROUP_NAME},
		"name",
	)
	if not existing:
		_create_leaf(GROUP_NAME, ROOT_GROUP)
		return

	doc = frappe.get_doc("Customer Group", existing)
	if not doc.get("is_group"):
		return

	child_count = frappe.db.count(
		"Customer Group",
		{"parent_customer_group": doc.name},
	)
	if not child_count:
		doc.is_group = 0
		doc.save(ignore_permissions=True)
		frappe.clear_cache(doctype="Customer Group")
		return

	if not frappe.db.exists(
		"Customer Group",
		{"customer_group_name": FALLBACK_GROUP_NAME},
	):
		_create_leaf(FALLBACK_GROUP_NAME, doc.name)


def _create_leaf(group_name, parent):
	doc = frappe.get_doc(
		{
			"doctype": "Customer Group",
			"customer_group_name": group_name,
			"parent_customer_group": parent,
			"is_group": 0,
		}
	)
	doc.insert(ignore_permissions=True)
	frappe.clear_cache(doctype="Customer Group")
