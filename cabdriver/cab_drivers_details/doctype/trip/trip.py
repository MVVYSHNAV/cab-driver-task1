# trip.py
import frappe
from frappe.model.document import Document
from frappe import _

class Trip(Document):
    def validate(self):
        self.check_existing_trips()

    def check_existing_trips(self):
        existing_trip = frappe.db.exists(
            "Trip",
            {
                "driver": self.driver,
                "docstatus": 0,
                "name": ["!=", self.name]
            }
        )

        if existing_trip:
            frappe.throw(
                _("Driver {0} already has another open trip: {1}").format(
                    self.driver, existing_trip
                )
            )
