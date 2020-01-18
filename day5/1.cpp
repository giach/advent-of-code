#include<iostream>
#include<fstream>
#include<vector>

#define PART_2 1

using namespace std;

void print_v(vector<int> v) {
    for(int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }

    cout << endl;
}

int main() {
    fstream myfile("1_big.txt", ios_base::in);
    int a, steps = 0;

    vector<int> v;

    while (myfile >> a) {
        v.push_back(a);
    }

    for(int i = 0; i < v.size(); i++) {
        cout << v[i] << endl;
    }
    int size = v.size();
    int  k = 0;
    while(1) {
        if(v[k] == 0) {
            v[k]++;
            steps++;
            continue;
        }
        
        int old = k;
        k += v[k];
#ifdef PART_2
        if (v[old] >= 3)
            v[old]--;
        else
            v[old]++;
#else
        v[old]++;
#endif   

        if (k >= size)
            break;   
        steps++;
 
    }

    printf("%d\n", steps+1);
    
    return 0;
}
