#include <iostream>
using namespace std;

#define INF 9999  // large number representing infinity
#define MAX 10    // maximum number of vertices

int main() {
    int n; // number of vertices
    cout << "Enter number of departments (vertices): ";
    cin >> n;

    int cost[MAX][MAX];
    cout << "Enter adjacency matrix (use 0 if no direct path):\n";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            cin >> cost[i][j];
            if (cost[i][j] == 0)
                cost[i][j] = INF;
        }

    int visited[MAX] = {0};
    visited[0] = 1; // start from first node
    int edges = 0, mincost = 0;

    cout << "\nEdges in Minimum Spanning Tree:\n";
    while (edges < n - 1) {
        int min = INF, a = -1, b = -1;

        for (int i = 0; i < n; i++)
            if (visited[i])
                for (int j = 0; j < n; j++)
                    if (!visited[j] && cost[i][j] < min) {
                        min = cost[i][j];
                        a = i;
                        b = j;
                    }

        if (a != -1 && b != -1) {
            cout << "Department " << a + 1 << " --> Department " << b + 1
                 << "  Distance: " << min << endl;
            mincost += min;
            visited[b] = 1;
            edges++;
        }
    }

    cout << "\nMinimum cost of campus connection = " << mincost << endl;
    return 0;
}
