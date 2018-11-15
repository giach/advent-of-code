#include<stdio.h>
#include<stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

#define DIE(condition, message) if (condition) \
					printf("We have a %s problem\n", message);
#define BASE 1
int main() {
	int i, fd, size, counter;

	fd = open("input.txt", O_RDONLY);
	DIE(fd < 0, "open");

	size = lseek(fd, 0, SEEK_END);
	int curr = lseek(fd, 0, SEEK_SET);
	printf("Current position is %d", curr);
	char buffer[size + 1];
	
	read(fd, buffer, size);

	buffer[size] = 0;
	counter = 0;
	for(i = 0; i < size; i++) {
	printf("%c ", buffer[i]);
		if(buffer[i] == '(')
			counter++;
		if(buffer[i] == ')')
			counter--;
#ifdef BASE
		if(counter == -1)
			break;
#endif
	}

#ifdef BASE
	printf("The floor is -1 because of index %d", i + 1);
#endif

#ifndef BASE
	printf("The floor is %d\n", counter);
#endif

	return 0;
}

