#define _GNU_SOURCE
#define INPUT_FILE "input.txt"
#define INPUT_SIZE 1000

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(unsigned int*a, size_t index1, size_t index2){
    unsigned int interim = a[index1];
    a[index1] = a[index2];
    a[index2] = interim;
}

void bubble_sort(unsigned int* a, size_t length){
    unsigned short swapped = 1;
    while (swapped == 1){
        swapped = 0;
        for (size_t i = 0; i<length-1; i++){
            if (a[i] > a[i+1]){
                swap(a, i, i+1);
                swapped = 1;
            }
        }
    }
}

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
    bubble_sort(a_array, INPUT_SIZE);
    bubble_sort(b_array, INPUT_SIZE);

    unsigned int sum = 0;
    for (size_t i = 0; i<INPUT_SIZE; i++){
        if (a_array[i] > b_array[i]){
            sum += a_array[i] - b_array[i];
        } else {
            sum += b_array[i] - a_array[i];
        }
    }
    printf("%i\n", sum);

    return EXIT_SUCCESS;
}
