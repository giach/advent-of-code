#include<stdio.h>
#include<stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>

#define DIE(condition, message) if (condition) \
					printf("We have a %s problem\n", message); \
					exit(EXIT_FAILURE);

#define MIN2(A, B)	((A) < (B) ? (A) : (B))
#define MIN3(A, B, C)	((A) < (B) ? MIN2(A,C) : MIN2(B,C))

#define SECOND 1
int main() {
	int i;
	FILE *fp = NULL;
	char line[80];
	size_t len = 0;
	int a, b, c;
	char x;
	int result = 0;
	int wrapping_paper = 0;
	fp = fopen("input.txt", "r");
//	DIE(fp == NULL, "open");

	while (1) {
		result = fscanf(fp, "%s", line);
		if (result <= 0)
			break;
		char *token = strtok(line, "x");
		a = atoi(token);
		token = strtok(NULL, "x"); 
		b = atoi(token);
		token = strtok(NULL, "x");
		c = atoi(token);

		printf("%d %d %d\n", a, b, c);
#ifndef SECOND
		wrapping_paper = wrapping_paper + 2*a*b + 2*b*c + 2*c*a;
		wrapping_paper += MIN3(a*b, b*c, c*a);
#endif
		wrapping_paper += 2 * MIN3(a+b, b+c, a+c);
		wrapping_paper += a*b*c;
	}

	printf("The size of the wrapping paper is %d\n", wrapping_paper);
	fclose(fp);

	return 0;
}

