#include <queue>
#include <vector>
#include <iostream>
#include <chrono>

// g++ -std=c++17 -O2 main.cpp && ./a.out


static const std::vector coins{2.0f, 1.0f, 0.5f, 0.2f, 0.1f, 0.05f, 0.02f, 0.01f};
// mutliply by 100 to avoid float computation, like in chrono lib
static const std::vector coins_100{200, 100, 50, 20, 10, 5, 2, 1};

int denombre()
{
    // pair of rest value and index of hightest coin removed
    std::queue<std::pair<int, int>> queue;
    queue.push(std::make_pair(200, 0));

    int n = 0;
    while (!queue.empty())
    {
        auto e = queue.front();
        int value = e.first;
        int last_coin_index = e.second;
        queue.pop();
        if (last_coin_index == coins_100.size() - 1)
        {
            ++n;
            continue;
        }
        const auto &current_coin = coins_100[last_coin_index];

        for (int i = value / current_coin; i >= 0; --i)
        {
            int tmp = value - i * current_coin;
            if (tmp == 0)
                ++n;
            else
                queue.push(std::make_pair(tmp, last_coin_index + 1));
        }
    }
    return n;
}

int denombre_recursif(int value, int index_coin)
{
    if (value == 0 || index_coin == coins_100.size() - 1)
        return 1;

    int somme = 0;
    for (int i = value / coins_100[index_coin]; i >= 0; --i)
        somme += denombre_recursif(value - i * coins_100[index_coin], index_coin + 1);

    return somme;
}

int main()
{
    {
        auto t1 = std::chrono::high_resolution_clock::now();
        std::cout << denombre() << std::endl;
        auto elapsed = std::chrono::high_resolution_clock::now() - t1;
        std::cout << "[QUEUE] elapsed time: " << elapsed.count() / 10e6 << "ms" << std::endl;
    }
    {
        auto t1 = std::chrono::high_resolution_clock::now();
        std::cout << denombre_recursif(200, 0) << std::endl;
        auto elapsed = std::chrono::high_resolution_clock::now() - t1;
        std::cout << "[RECURSIF] elapsed time: " << elapsed.count() / 10e6 << "ms" << std::endl;
    }
}