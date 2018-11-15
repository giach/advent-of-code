#include<stdio.h>
#include<stdlib.h>
#include<errno.h>

#define DIE(condition, message) if (condition) \
					printf("We have a %s problem\n", message); \
					exit(EXIT_FAILURE);

#define MIN2(A, B)	((A) < (B) ? (A) : (B))
#define MIN3(A, B, C)	((A) < (B) ? MIN2(A,C) : MIN2(B,C))

#define SECOND 1
#define MAX 10000

int main() {
	int i;
	FILE *fp = NULL;
	char c;
	int result = 0;
	fp = fopen("input.txt", "r");
	int x = 0, y = 0;
	int counter = 1;
	long xys[MAX];
	long pos = 0;	
	for(i = 0; i < MAX; i++) {
		xys[i] = -1;
	}
	xys[0] = 1;
	while (1) {

		result = fscanf(fp, "%c", &c);
		switch(c) {
		case 94:
			y++; break;
		case 62: 
			x++; break;
		case 118:
			y--; break;
		case 60:
			x--; break;
		default:
			printf("\n");
		}
		
		pos = (x << 1) | y;
		if(xys[pos] == -1) {
			counter++;
			xys[pos] = 1;
		}
		printf("%d %d %d %ld\n", c, x, y, pos);
		if (c == 10)
			break;
		
	}

	printf("The result is %d\n", counter);
	fclose(fp);

	return 0;
}

