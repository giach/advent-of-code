#include<iostream>
#include<stdlib.h>
#include<vector>

using namespace std;

#define SMALL_INPUT "small_input_1.txt"
#define BIG_INPUT    "big_input_2.txt"

bool check_val(vector<int> v, int val) {
    int i;
    
    if(v.size() == 0)
        return false;

    for(i = 0; i < v.size(); i++) {
        if(v[i] == val)
            return true;
    }

    return false;
}

int find_freq(vector<int> changes)
{
    int i, freq = 0;
    vector<int> inter_freqs;

    while(1) {
        for(i = 0; i < changes.size(); i++) {
            freq += changes[i];
            if(check_val(inter_freqs, freq))
                return freq;

            inter_freqs.push_back(freq); 
        }
    }

}

int main() {
   
    FILE *fd;
    vector<int> changes;

    int freq = 0, ch = 0, res = 1;
#if 0
    fd = fopen(SMALL_INPUT, "r");
#else
    fd = fopen(BIG_INPUT, "r");
#endif

    while(1) {
        res = fscanf(fd, "%d", &ch);
        if(res != 1)
            break;
        changes.push_back(ch);
    }


    freq = find_freq(changes); 
    printf("The resulting requency is %d\n", freq);

    return 0;    

}
