#define INPUT_FILE "data/day01_large.txt"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int get_next_item(FILE *fp) {
    char line[6];
    int calories; 
    fgets(line, 6, fp);
    if (feof(fp)){
        return -2;
    }
    if (strcmp(line, "\n")==0) {
        return -1;
    } else {
        calories = atoi(line);
    }
    return calories;
}

unsigned int argmin(unsigned int input[], unsigned int LENGTH) {
    unsigned int min_value = input[0];
    unsigned int min_index = 0;
    for (unsigned int i = 1; i<LENGTH; i++){
        if (input[i] < min_value){
            min_value = input[i];
            min_index = i;
        }
    }
    return min_index;
}

unsigned int arrmax(unsigned int input[], unsigned int LENGTH) {
    unsigned int max_value = input[0];
    for (unsigned int i = 1; i<LENGTH; i++){
        if (input[i] > max_value){
            max_value = input[i];
        }
    }
    return max_value;
}

unsigned int sum(unsigned int input[], unsigned int LENGTH) {
    unsigned int res = 0;
    for (unsigned int i = 0; i<LENGTH; i++){
        res += input[i];
    }
    return res;
}

int main(void) {
    enum {LENGTH = 3};
    FILE *fp;
    fp = fopen(INPUT_FILE, "r");
    unsigned int calories_richest[LENGTH] = {0};
    unsigned int calories_this = 0;
    bool active = true;
    unsigned int *third_richest;
    third_richest = &calories_richest[0];
    
    while (active) {
        int calories;
        calories = get_next_item(fp);
        if (calories < 0){
            active = (calories == -1);
            if (calories_this > *third_richest){
                *third_richest = calories_this;
                third_richest = &calories_richest[argmin(calories_richest, LENGTH)];
            }
            calories_this = 0;
        }else{
            calories_this += calories;
        }
    }

    printf("Part1:\t%d\n", arrmax(calories_richest, LENGTH));
    printf("Part2:\t%d\n", sum(calories_richest, LENGTH));

    return EXIT_SUCCESS;
}