#include <stdio.h>
int main(){
    int hex;
    scanf("%X", &hex);
    for (int i = 0x1; i<=0xF; i++){
        printf("%X*%X=%X\n", hex, i, (hex*i));
    }
    return 0;
}
