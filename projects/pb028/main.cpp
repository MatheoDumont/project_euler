#include <iostream>
#include <chrono>

/*

PB 28

last of layer n+1 is
last_n+1 = last_n + 8*n

sum of layer n+1 is
sum_n+1 = 4*last_n + 20*n

if we compute separately last_n from the sum we get
sum_n+1 = 3*last_n + 12*n + last_n+1

since we see the grid as a spiral of a "circle", its radius is the (diameter+1)/2

*/

int get_diag_sum(int grid_size)
{
    int nb_layer = (grid_size + 1) / 2;
    int sum = 1;
    // top right corner of previous layer
    int last_int_previous_layer = 1;
    for (int i = 1; i < nb_layer; ++i)
    {
        int tmp_last_int_current_layer = last_int_previous_layer + 8 * i;
        int current_layer_sum = 3 * last_int_previous_layer + 12 * i + tmp_last_int_current_layer;
        sum += current_layer_sum;
        last_int_previous_layer = tmp_last_int_current_layer;
        // std::cout << "layer " << i << ", somme " << current_layer_sum << ", last " << tmp_last_int_current_layer << std::endl; 
    }

    // std::cout << "Total sum for grid size " << grid_size << " is " << sum << std::endl;
}

int main() {
    int grid_size = 1001;
    auto now = std::chrono::high_resolution_clock::now();
    int sum = get_diag_sum(grid_size);
    auto elapsed = std::chrono::high_resolution_clock::now() - now;
    std::cout << "Elapsed time for grid " << grid_size << " is " << elapsed.count() / 10e3 << "microsec" << std::endl;
    std::cout << "Total sum for grid size " << grid_size << " is " << sum << std::endl;
}