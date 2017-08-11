#include <iostream>

using namespace std;

int main() {
    int x;
    cout << "Enter check number: ";
    cin >> x;
    if (x == 1e20) {
        cout << "uctf_boring_task" << endl;
    } else {
        cout << "Bad luck" << endl;
    }
    return 0;
}
