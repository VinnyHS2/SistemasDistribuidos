#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

void lsh_loop() {
    char *line;
    char **args;
    int status;

    do {
        printf(">> ");
        line = lsh_read_line();
        args = lsh_split_line(line);
        status = lsh_execute(args);

        free(line);
        free(args);
    } while (status);
}

int main(int argc, char **argv) {

    lsh_loop(); // loop principal

    return EXIT_SUCCESS;
}