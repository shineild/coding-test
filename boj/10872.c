int fa(int n, int sum){
    if (n == 0){
        printf("%d\n", sum);
        return 0;
    }
    sum *= n;
    return fa(n-1, sum);
}
int main(){
    int n, sum = 1;
    scanf("%d", &n);
    fa(n, sum);
    return 0;
}
