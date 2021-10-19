#include <stdio.h>
int main(int argc, const char * argv[]) {
    int a, b;
    scanf("%d %d", &a, &b);
    int bx = b / 100;
    int by = (b - (bx*100)) / 10;
    int bz = b % 10;
    printf("%d\n", a * bz);
    printf("%d\n", a * by);
    printf("%d\n", a * bx);
    printf("%d", a * b);
    return 0;
}
