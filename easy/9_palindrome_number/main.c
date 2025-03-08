#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(int argc, char** argv)
{
	char * string = argv[1];
	size_t string_size = strlen(string);

	bool is_palindrome = true;

	for (size_t i=0; i < string_size; i++){
		printf("first char %c - ", string[i]);
		printf("second char %c\n", string[string_size-i-1]);
		if (string[i] != string[string_size-i-1])
			is_palindrome = false;
	}

	printf("Is string %s a palindrome : %d", string, is_palindrome);

	return 0;
}


