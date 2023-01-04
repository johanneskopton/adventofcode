#define INPUT_FILE "data/day02_large.txt"

#include <stdio.h>

int main(void) {
    FILE *fp;
    fp = fopen(INPUT_FILE, "r");

    int score1 = 0;
    int score2 = 0;    
    while (1) {
        int a, b;
        char line[5];
        fgets(line, 5, fp);
        if (feof(fp)){break;}
        a = line[0] - 65;
        b = line[2] - 88;
        score1 += b + 1;
        score1 += (b - a + 4) % 3 * 3;
        score2 += (a + b + 2) % 3 + 1;
        score2 += b * 3;    
    }

    printf("Part1:\t%d\n", score1);
    printf("Part2:\t%d\n", score2);

    return 0;
}