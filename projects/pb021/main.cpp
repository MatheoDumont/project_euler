#include <iostream>
#include <math.h>

using namespace std;

int sum_proper_divisor(int n)
{
    int somme = 1;
    int div = 2;
    float upper_bound;
    float fractional;

    float s = sqrt(n);
    while (div < s)
    {
        upper_bound = modf(n / div, &fractional);
        if (fractional==0.0)
            somme += div + upper_bound;
        
        div += 1;
    }
    return somme;
}

int main()
{
    if (int s = sum_proper_divisor(220); s != 284)
    {
        cout << "sum_proper_divisor of 220 should be 284, " << s << " given !" << endl;
        exit(1);
    }
    if (int s = sum_proper_divisor(5); s != 1)
    {
        cout << "sum_proper_divisor of 5 should be 1, " << s << " given !" << endl;
        exit(1);
    }
}