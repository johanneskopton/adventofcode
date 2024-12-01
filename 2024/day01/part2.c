#define _GNU_SOURCE
#define INPUT_FILE "input.txt"
#define INPUT_SIZE 1000

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *fp;
    char* line=NULL;
    size_t len = 0;
    size_t read;
    fp = fopen(INPUT_FILE, "r");
    if (NULL == fp) {
        printf("file can't be opened \n");
          return EXIT_FAILURE;
    }
    unsigned int a_array[INPUT_SIZE];
    unsigned int b_array[INPUT_SIZE];
    size_t i = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        char str_first[6];
        char str_last[6];
        strncpy(str_first, line, 5);
        strncpy(str_last, line+8, 5);
        a_array[i] = atoi(str_first);
        b_array[i] = atoi(str_last);
        i++;
    }
    fclose(fp);

    unsigned int result = 0;
    for (size_t i = 0; i<INPUT_SIZE; i++){
        unsigned int amount = 0;
        for (size_t j = 0; j<INPUT_SIZE; j++){
            if (a_array[i] == b_array[j])
                amount++;
        }
        result += a_array[i] * amount;
    }
    printf("%i\n", result);

    return EXIT_SUCCESS;
}
