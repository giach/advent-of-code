#include<stdio.h>
#include<iostream>

#define MAX_SIZE 26

using namespace std;

bool check_letters(int freq[], int x) {
    for(int i = 0; i < MAX_SIZE; i++) {
        if(freq[i] == x)
            return true;
    }

    return false;
}

bool compare_arrs(int v1[], int v2[]) {
    
    int diffs = 0;
    for(int i = 0; i < MAX_SIZE; i++) {
        if(v1[i] != v2[i])
            diffs += 1;

        if (diffs > 1)
            return false;  
    }

    return true;
}

int main() {

    FILE *fd;
    fd = fopen("big_input.txt", "r");
    if(fd == NULL) {
        cout << "Couldn't open the file" << endl;
        return -1;
    }

    int res, i;
    int two = 0, three = 0;

    while(1) {

        int freq[26] = {0};
        char s[30];

        res = fscanf(fd, "%s", s);
        if (res != 1)
            break;

        for(i = 0; s[i]; i++) {
            int index = s[i] - 97;
            freq[index]++;
        }
    
        if(check_letters(freq, 2))
            two += 1;

        if(check_letters(freq, 3))
            three += 1;
         
    }

    cout << two << " " << three << endl;
    cout << two * three << endl;

    fclose(fd);

    return 0;
}
