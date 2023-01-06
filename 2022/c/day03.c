#define INPUT_FILE "data/day03_large.txt"

#include <stdio.h>
#include <string.h>

unsigned char score(char c){return c >= 97 ? c - 96 : c -38;}

char intersect_halves(char line[50], unsigned char halflength){
    for (unsigned char i=0; i<halflength; i++){
        for (unsigned char j=0; j<halflength; j++){
            if (line[i] == line[halflength+j]){
                return line[i];
            }
        }
    }
}

char intersect_groups(char line_history[3][50], unsigned char length_history[3]){
    for (unsigned char i=0; i<length_history[0]; i++){
        for (unsigned char j=0; j<length_history[1]; j++){
            for (unsigned char k=0; k<length_history[2]; k++){
                if (line_history[0][i] == line_history[1][j] && line_history[0][i] == line_history[2][k]){
                    return line_history[0][i];
                }
            }
        }    
    }
}

int main(void) {
    FILE *fp;
    fp = fopen(INPUT_FILE, "r");

    unsigned int score1 = 0;
    unsigned int score2 = 0;    
    
    char line[50];
    unsigned char i = 0;
    char line_history[3][50];
    unsigned char length_history[3];
    while (fgets(line, 50, fp) != 0) {
        unsigned char length = strlen(line)-1;
        unsigned char halflength = length/2;
        score1 += score(intersect_halves(line, halflength));
        for (unsigned char j=0; j<length; j++){
            line_history[i][j] = line[j];
        }
        length_history[i] = length;
        if (i == 2){
            score2 += score(intersect_groups(line_history, length_history));
            i = 0;
        } else {
            i++;
        }
    }

    printf("Part1:\t%d\n", score1);
    printf("Part2:\t%d\n", score2);

    return 0;
}