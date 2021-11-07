"""Classes for melon orders."""

class AbstractMelonOrder():

    def __init__(self, species, qty, order_type=None, tax=0, country_code=None):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.qty < 10 and self.order_type == "international":
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic", 0.08, "USA")
        
class GovernmentMelonOrder(DomesticMelonOrder, AbstractMelonOrder):
    """US only orders that have no sales tax"""
    
    def __init__(self, species, qty, passed_inspection=False):
        super().__init__(species, qty)
        self.tax = 0
        self.passed_inspection = passed_inspection

    def mark_inspection(self, passed):
        self.passed_inspection = passed




class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international", 0.17, country_code)


