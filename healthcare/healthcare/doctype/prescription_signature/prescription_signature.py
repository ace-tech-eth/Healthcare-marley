import frappe
from frappe.model.document import Document
from frappe.utils import now


class PrescriptionSignature(Document):
	def validate(self):
		if not self.signed_at:
			self.signed_at = now()
		if not self.user:
			self.user = frappe.session.user
		if not self.signed_by:
			self.signed_by = frappe.db.get_value("User", self.user, "full_name") or self.user
