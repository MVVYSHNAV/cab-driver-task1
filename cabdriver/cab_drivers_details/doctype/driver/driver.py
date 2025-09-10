import frappe
from frappe.model.document import Document

class Driver(Document):
    def validate(self):
        if self.driver_name.lower() == "sulaiman":
            frappe.throw("Sulaiman cannot be a valid driver")



