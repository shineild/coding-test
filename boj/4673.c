#include <stdio.h>

int main(int argc, const char * argv[]) {
    int def[9999];
    int a;
    int b;
    int c;
    int d;
    int e;
    for (int i = 0; i<10000; i++){
        a = i + 1;
        if (a < 10){
            def[i] =  a + a;
        }
        else if (9 < a && a<100){
            b = a / 10;
            c = a % 10;
            def[i] = a + b + c;
        }
        else if (100 <= a && a <1000){
            d = a / 100;
            b = (a - (100 * d)) / 10;
            c = a % 10;
            def[i] = a + b + c + d;
        }
        else if (1000 <= a && a <10000){
            e = a / 1000;
            d = (a - (1000 * e)) / 100;
            b = (a - (1000 * e) - (100 * d)) / 10;
            c = a % 10;
            def[i] = a + b + c + d + e;
        }
    }
    
    
    for (int i = 1; i<=10000; i++){
        int cnt = 0;
        for (int k = 0; k<10000; k++){
            if (i == def[k]){
                cnt++;
            }
        }
        if (cnt == 0){
            printf("%d\n", i);
        }
    }
    return 0;
}
