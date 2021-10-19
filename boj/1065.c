#include <stdio.h>

int main()
{
    int num;
    int cnt = 0;
    int b, s, l;
    scanf("%d", &num);
    for (int i=1; i<=num; i++){
        if (i < 100) {
            cnt++;
        }
        else if (i == 1000) {
        }
        else{
            b = i / 100;
            s = (i - 100 * b) / 10;
            l = i % 10;
            if (s - b == l - s){
                cnt++;
            }
        }
    }
    printf("%d", cnt);
    return 0;
}
