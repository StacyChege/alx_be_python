class Calculator:
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        """Static method: doesn't use self or cls, just does a task"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: uses the class (cls) to access class attributes"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
