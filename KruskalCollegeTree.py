#include <iostream>
using namespace std;

int find(int parent[], int i) {
    while (parent[i] != i) i = parent[i];
    return i;
}

void uni(int parent[], int i, int j) {
    int a = find(parent, i);
    int b = find(parent, j);
    parent[a] = b;
}

int main() {
    int n;
    cout << "Enter number of nodes: ";
    cin >> n;

    int cost[10][10];
    cout << "Enter adjacency matrix (0 for no edge):\n";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            cin >> cost[i][j];
            if (cost[i][j] == 0) cost[i][j] = 999;
        }

    int parent[10];
    for (int i = 0; i < n; i++) parent[i] = i;

    int ne = 1, mincost = 0;
    cout << "\nEdges in MST:\n";
    while (ne < n) {
        int a = -1, b = -1, min = 999;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (find(parent, i) != find(parent, j) && cost[i][j] < min) {
                    min = cost[i][j];
                    a = i; b = j;
                }
        uni(parent, a, b);
        cout << ne++ << ") " << a+1 << " - " << b+1 << " : " << min << endl;
        mincost += min;
        cost[a][b] = cost[b][a] = 999;
    }
    cout << "Min cost = " << mincost;
}
