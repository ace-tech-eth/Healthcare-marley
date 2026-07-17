import frappe
from frappe.model.document import Document
from frappe.utils import today


class MedicationPrescription(Document):
	def validate(self):
		if not self.date_pres:
			self.date_pres = today()
		if not self.prescription_type:
			self.prescription_type = "Internal"
		if not self.status:
			self.status = "Incoming"
