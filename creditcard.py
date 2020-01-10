class CreditCard:
    """A consumer credit card."""

    def init (self, customer, bank, acnt, limit, balance=0):
        """Create a new credit card instance.
        The initial balance is zero.

        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        start account balance (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance if balance else 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank s name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def _set_balance(self, balance):
        """Sets balance"""
        self._balance = balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

         Return True if charge was processed; False if charge was denied.
        """
        if not isinstance(price, int) or not isinstance(price, float):
            return False

        if price + self.get_balance() > self._limit: # if charge would exceed limit,
            return False # cannot accept charge
        else:
            self._set_balance(self.get_balance() + price)
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if not isinstance(amount, int) or not isinstance(amount, float)\
                or amount < 0:
            raise ValueError("amount should be a positive number")

        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    OVERLIMIT_FEE = 5 # this is a class-level member

    def __init__ (self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.
        The initial balance is zero.

        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit) # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied.
        """
        if not isinstance(price, int) or not isinstance(price, float):
            return False

        success = super().charge(price)
        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self.get_balance() > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._set_balance(monthly_factor)


