#include <stdio.h>
#include <stdlib.h>

#define MAX(a, b) (((a)>(b))?(a):(b))
#define MIN(a, b) (((a)<(b))?(a):(b))

int main(){
    int n, left, right, sum = 0;
    for(int TC=0 ; TC<10 ; TC++){
        scanf("%d", &n);
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
        printf("#%d %d\n", TC+1, sum);
        sum=0;
        free(in);
    }
    return 0
}