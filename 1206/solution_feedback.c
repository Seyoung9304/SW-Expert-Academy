#include <stdio.h>
#include <stdlib.h>

#define MAX(a, b) (((a)>(b))?(a):(b))
#define MIN(a, b) (((a)<(b))?(a):(b))

int main(){
    int n, left, right, sum = 0;
    // 아래 TC+1로 출력해야함 - 연산 발생. 
    // 그냥 TC=1로 시작하자. 
    for(int TC=1 ; TC<=10 ; TC++){
        scanf("%d", &n);
        /*
        동적할당이 언제 효율적인가?를 생각해보아야 함. 
        데이터 크기가 적당할 때는 그냥 배열을 통째로 할당해두는게 이득일 때가 있음. 
        */
        int *in = (int*)malloc(sizeof(int)*n);
        for(int i=0;i<n;i++){
            scanf("%d", &in[i]);
        }
        for(int i=2;i<n-2;i++){
            left = in[i]-MAX(in[i-1], in[i-2]);
            right = in[i]-MIN(in[i+1], in[i+2]);
            if(left>0 && right>0)
                sum += MIN(left, right);
        }
        printf("#%d %d\n", TC, sum);
        sum=0;
        free(in);
    }
    return 0;
}