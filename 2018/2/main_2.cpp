#include<stdio.h>
#include<iostream>
#include<vector>
#include<tuple>
#include<string>
#define MAX_SIZE 26

using namespace std;

void print_vector(vector<int> v) {
    for(int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }

    cout << endl;
}

int compare_strings(string s1, string s2) {
    
    int count = 0;
    for(int i = 0; i < s1.size(); i++) {
        if(s1[i] - s2[i] != 0)
            count += 1;
    }

    return count;
}

pair<int, int> find_alike_arrs(vector<string> text)
{
    
    int i, j;
    int count;
 
    for(i = 0; i < text.size(); i++) {
        for(j = i + 1; j < text.size(); j++) {
            count = compare_strings(text[i], text[j]);
            if(count < 2)
                return make_pair(i,j); 
        }
    }
    return make_pair(-1,-1);
}

int main() {

    FILE *fd;
    fd = fopen("big_input.txt", "r");
    if(fd == NULL) {
        cout << "Couldn't open the file" << endl;
        return -1;
    }

    int res, i, j;
    vector<string> text;
    int lindex = 0;
    pair<int, int> t;
    while(1) {

        vector<int> freq(MAX_SIZE, 0);
        char s[30];

        res = fscanf(fd, "%s", s);
        if (res != 1)
            break;

        text.push_back(s);

    }

    t = find_alike_arrs(text);
    if(t.first == -1)
        exit(-1); 
    string fst = text[t.first];
    string snd = text[t.second];
    
    for(i = 0; i < fst.size(); i++) {
        
        if(fst[i] == snd[i]) {
            cout << fst[i];
        }
    }

    cout << endl;
    fclose(fd);

    return 0;
}
