import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real:.2f}{self.imaginary:.2f}i"
        else:
            return f"{self.real:.2f}+{self.imaginary:.2f}i"

    def add(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imaginary_sum)
    
    def subtract(self, other):
        real_diff = self.real - other.real
        imaginary_diff = self.imaginary - other.imaginary
        return ComplexNumber(real_diff, imaginary_diff)

    def multiply(self, other):
        real_product = self.real * other.real - self.imaginary * other.imaginary
        imaginary_product = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_product, imaginary_product)
    
    def divide(self, other):
        denominator = other.real**2 + other.imaginary**2
        if denominator == 0:
            raise ValueError("Division by zero is not allowed.")
        real_quotient = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_quotient = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_quotient, imaginary_quotient)
    
    def modulus(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

real_c, imaginary_c = map(float, input("Enter the real and imaginary parts of C: ").split())
real_d, imaginary_d = map(float, input("Enter the real and imaginary parts of D: ").split())

C = ComplexNumber(real_c, imaginary_c)
D = ComplexNumber(real_d, imaginary_d)

result_add = C.add(D)
result_sub = C.subtract(D)
result_mul = C.multiply(D)
result_div = C.divide(D)
mod_C = C.modulus()
mod_D = D.modulus()

print(f"C + D = {result_add}")
print(f"C - D = {result_sub}")
print(f"C * D = {result_mul}")
print(f"C / D = {result_div}")
print(f"mod(C) = {mod_C:.2f}")
print(f"mod(D) = {mod_D:.2f}")
