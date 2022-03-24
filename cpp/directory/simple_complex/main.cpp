#include <iostream>

class Complex
{
private:
    double real, img;

public:
    Complex(double real, double img) : real(real), img(img) {}
    Complex(const Complex &c) : real(c.real), img(c.img) {}

    Complex operator+(const Complex &c) const;
    Complex operator-(const Complex &c) const;
    Complex operator/(const Complex &c) const;
    Complex operator*(const Complex &c) const;
    Complex &operator=(const Complex &c);
};

Complex Complex::operator+(const Complex &c) const
{
    Complex result(real + c.real, img + c.img);

    return result;
}
Complex Complex::operator-(const Complex &c) const
{
    Complex result(real - c.real, img - c.img);

    return result;
}
Complex Complex::operator*(const Complex &c) const
{
    Complex result(real * c.real - img * c.img, real * c.img + img * c.real);
    return result;
}
Complex Complex::operator/(const Complex &c) const
{
    Complex result(
        (real * c.real + img * c.img) / (c.real * c.real + c.img * c.img),
        (img * c.real - real * c.img) / (c.real * c.real + c.img * c.img));
    return result;
}

Complex &Complex::operator=(const Complex &c)
{
    real = c.real;
    img = c.img;
    return *this;
}

int main()
{
    Complex a(1, 3);
    Complex b(2, 5);

    a + b;

    return 0;
}