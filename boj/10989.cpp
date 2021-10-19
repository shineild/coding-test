#include <bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    // 숫자를 기억할 배열 생성
    int arr[10001] = {0};
    int n;
    cin>>n;
    for(int i=0; i<n; i++){
        int num;
        cin>>num;
        arr[num]+=1;
        // 해당 숫자 입력 개수 저장
    }
    for(int i = 0; i<10001;i++){
        for(int j=0; j<arr[i]; j++){
            cout<<i<<"\n";
        }
    }
}
