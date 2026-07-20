import frappe
from frappe.model.document import Document


class PractitionerSignature(Document):
	def validate(self):
		if self.practitioner and not self.practitioner_name:
			self.practitioner_name = frappe.db.get_value(
				"Healthcare Practitioner",
				self.practitioner,
				"practitioner_name",
			)
		if self.user and not self.practitioner:
			practitioner = frappe.db.get_value("Healthcare Practitioner", {"user_id": self.user}, "name")
			if practitioner:
				self.practitioner = practitioner
				if not self.practitioner_name:
					self.practitioner_name = frappe.db.get_value(
						"Healthcare Practitioner",
						practitioner,
						"practitioner_name",
					)
