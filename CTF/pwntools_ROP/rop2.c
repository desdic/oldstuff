#include <string.h>
#include <stdio.h>
#include <stdlib.h>

char* not_used = "/bin/sh";

void not_called() {
    printf("Not quite a shell...\n");
    system("/bin/date");
}

void vulnerable_function(char* string) {
    char buffer[100];
    strcpy(buffer, string);
}

int main(int argc, char** argv) {
    (void)argc;
    vulnerable_function(argv[1]);
    return 0;
}
