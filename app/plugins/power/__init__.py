from app.commands import Command

class PowerCommand(Command):
    """Command to perform exponentiation."""

    def execute(self, base, exponent):
        """Calculate the power of a number."""
        return base ** exponent
