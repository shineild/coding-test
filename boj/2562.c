#include <stdio.h>
int main(){
    int k, n, d = 1;
    scanf("%d", &k);
    for(int i = 2; i<10; i++){
        scanf("%d", &n);
        if (n > k){
            k = n;
            d = i;
        }
    }
    printf("%d\n%d\n\n", k, d);
    return 0;
}
