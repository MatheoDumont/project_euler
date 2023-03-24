#include <iostream>
#include <math.h>
#include <vector>
#include <unordered_map>
#include <chrono>

using namespace std;
// g++ -w main.cpp && ./a.out
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
    // si un nombre est odd, alors il n'a pas de diviseur pair donc on les skip,
    // mais un nombre even peut avoir des diviseurs pair
    int step = n % 2 == 0 ? 1 : 2;

    // si s est entier, alors s*s = n, au lieu d'avoir un if dans la boucle
    // on peut en tenir compte maintenant
    if ((s - (int)s) == 0)
    {
        somme += s;
        s -= 1;
    }
    while (div <= s)
    {
        fractional = modf(n_f / div, &whole);

        if (fractional == 0)
            somme += div + whole;

        div += step;
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

int pb021()
{
    int n = 10000;
    int somme = 0;
    vector<int> sums(n, 0);
    sums[0] = 1;

    for (int i = 1; i < n; i++)
    {
        int number = i + 1;
        sums[i] = sum_proper_divisor(number);
        int idx_number = sums[i] - 1;

        // continue because i haven't computed sum_proper_divisor of sums[i] or he points to himself
        if (sums[i] > n || number == sums[i])
            continue;

        // if already computed, just check
        if (sums[idx_number] == number)
        {
            somme += number + sums[i];
            cout << "number: " << number << " sum: " << sums[i] << endl;
        }
    }

    return somme;
}

int main()
{
    test_sum_proper_divisor();

    auto tic = chrono::high_resolution_clock::now();
    int r = pb021();
    auto tac = chrono::high_resolution_clock::now();
    auto int_ms = chrono::duration_cast<chrono::milliseconds>(tac - tic);

    float in_sec = (float)int_ms.count() / 10e3;
    cout << "Time: " << in_sec << " sec" << endl;
    cout << r << endl;
}