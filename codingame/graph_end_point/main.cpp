#include <assert.h>
#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <functional>

using namespace std;

//  g++ -w ascii.cpp && ./a.out
/*
* Handled Graphs are one oriented with only a single edge departing from a node but many can be arriving
* a Node cannot be directly linked to itself.
* Used object are array describing edges, one array for the departing nodes and one for the arriving nodes,
* a pair at the same indice in both arrays forming an edge connecting node fromIds[i] to toIds[i].

fromIds = {1, 2, 3, 4}
toids = {3, 3, 4, 5}
correspond to 

1->3
2->3
3->4
4->5

and no edges leave 5, so the algo in this case should return 5, 
whatever the startNodeId, the output should be 5 in this case.
*/
int find_edge(int node, vector<int> fromIds)
{
    /*
     * If return is -1, then the node doesnt exists, then its the last
     * otherwise returns the arg of the node in fromIds
     */
    for (int i = 0; i < fromIds.size(); i++)
        if (node == fromIds[i])
            return i;

    return -1;
}

int find_nextwork_endpoint(int startNodeId, vector<int> fromIds, vector<int> toIds)
{
    vector<int> edge_passage_counts(toIds.size(), 0);

    int id = find_edge(startNodeId, fromIds);
    int next_edge = startNodeId;
    edge_passage_counts[id] += 1;
    int previous_edge = -1;
    while (id != -1 && edge_passage_counts[id] < 2)
    {
        edge_passage_counts[id] += 1;
        previous_edge = next_edge;
        next_edge = toIds[id];
        id = find_edge(next_edge, fromIds);
    }

    if (edge_passage_counts[id] > 1)
        return previous_edge;
    else
        return next_edge;
}

/*
 * =========================== TEST ===========================
 */
int timing(int ids, vector<int> vec1, vector<int> vec2)
{
    auto tic = chrono::high_resolution_clock::now();
    int r = find_nextwork_endpoint(ids, vec1, vec2);
    auto tac = chrono::high_resolution_clock::now();
    auto int_ms = chrono::duration_cast<chrono::milliseconds>(tac - tic);
    
    float in_sec = (float) int_ms.count() / 10e3;
    cout << "Time: " << in_sec << " sec" << endl;
    return r;
}

void result(int actual, int expected, string name)
{
    if (actual != expected)
        cout << "Test " << name << ": ERROR" << endl
             << "expected: " << expected << endl
             << "received: " << actual << endl;
    else
        cout << "Test " << name << ": PASSED" << endl;
}

void test_simple()
{
    vector<int> fromIds({1, 2, 3, 4});
    vector<int> toIds({3, 3, 4, 5});
    int r = timing(1, fromIds, toIds);
    result(r, 5, "simple");
}

void test_ten_thousand_nodes()
{
    vector<int> fromIds;
    vector<int> toIds;

    for (int i = 1; i < 10001; i++)
    {
        fromIds.push_back(i);
        toIds.push_back(i + 1);
    }
    int r = timing(1, fromIds, toIds);
    result(r, 10001, "ten_thousand_nodes");
}

void test_loop()
{
    vector<int> fromIds({1, 2, 3, 4});
    vector<int> toIds({2, 3, 4, 2});

    int r = timing(1, fromIds, toIds);
    result(r, 4, "loop");
}

void test_cirle()
{
    vector<int> fromIds({1, 2, 3, 4});
    vector<int> toIds({2, 3, 4, 1});
    int r = timing(1, fromIds, toIds);
    result(r, 4, "circle");
}

void test_disconnected_graph()
{
    vector<int> fromIds({1, 2, 4, 5});
    vector<int> toIds({2, 3, 5, 6});
    int r = timing(4, fromIds, toIds);
    result(r, 6, "disconnected graph 1");

    r = timing(1, fromIds, toIds);
    result(r, 3, "disconnected graph 2");
}

int main()
{
    test_simple();
    test_ten_thousand_nodes();
    test_loop();
    test_cirle();
    test_disconnected_graph();
}