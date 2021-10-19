#include<stdio.h>
#include<string.h>

int main(void){
    char buf[101];
    while(gets(buf)){
        if (buf[0] == "\0"){
            break;
        }
        puts(buf);
    }
}
