#include <stdio.h>
int main(){

    char buf[20];
    scanf("%s", &(buf[0]));
    for (int i = 0; buf[i]; i++){
        printf("\'%c\'\n", buf[i]);
    }
    return 0;
}
