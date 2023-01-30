import frappe
from frappe.model.document import Document
from frappe.utils import flt


def validate(doc, method=None):
	if doc.variant_of:
		doc.length = frappe.db.get_value("Item", doc.variant_of, "length")
		for row in doc.attributes:
			if row.attribute=="Width":
				doc.width = flt(row.attribute_value)
			elif row.attribute=="Height":
				doc.height = flt(row.attribute_value)
			else:
				doc.yield_ = flt(row.attribute_value)

	for row in doc.uoms:
		if row.formula:
			row.conversion_factor = eval(row.formula)
				
			
			
