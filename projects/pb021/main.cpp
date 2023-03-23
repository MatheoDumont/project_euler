#include <iostream>
#include <math.h>

using namespace std;

/*
* Sum of all proper divisor of n (starting from 1, without n).
* if n is one, should return 0
*/
int sum_proper_divisor(int n)
{
    
    float n_f = (float)n;
    int somme = 1;
    float div = 2;
    float whole, fractional;
    float s = sqrt(n);


    while (div <= s)
    {
        fractional = modf(n_f / div, &whole);

        if (fractional == 0.0) {
            if (div == whole) 
                somme += div;
            else
                somme += div + whole;
        }

        div++;
    }
    return somme;
}

int test_sum_proper_divisor()
{   
    cout << "sum_proper_divisor(220)" << endl;
    if (int s = sum_proper_divisor(220); s != 284)
    {
        cout << "sum_proper_divisor of 220 should be 284, " << s << " given !" << endl;
        exit(1);
    }
    cout << "sum_proper_divisor(284)" << endl;

    if (int s = sum_proper_divisor(284); s != 220)
    {
        cout << "sum_proper_divisor of 284 should be 220, " << s << " given !" << endl;
        exit(1);
    }
    cout << "sum_proper_divisor(5)" << endl;
    if (int s = sum_proper_divisor(5); s != 1)
    {
        cout << "sum_proper_divisor of 5 should be 1, " << s << " given !" << endl;
        exit(1);
    }
}

int main()
{
    test_sum_proper_divisor();
    for (int i = 2; i < 100; i++) {
        cout << i << " == " << sum_proper_divisor(i) << endl;
    }
}