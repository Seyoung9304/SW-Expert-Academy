#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char arr1[8][8];
    char arr2[8][8];
    
    for (int TC = 1; TC<=10 ; TC++){
        int size;
        scanf("%d", &size);

        for (int i=0; i<8; i++){
            for (int j=0; j<8; j++){
                char temp;
                scanf(" %c", &temp); //개행 처리 위해 %c 앞 공백
                arr1[i][j] = temp;
                arr2[i][j] = temp;
            }
        }

        int cnt = 0;
        for (int i=0; i<8; i++){
            for (int j=0; j<8; j++){
                int flag1 = 1;
                int flag2 = 1;
                for (int k = 0;k < size / 2;k++) {
                    if (arr1[i][j + k] != arr1[i][j + size - 1 - k])
                        flag1 = 0;
                    if (arr2[i][j + k] != arr2[i][j + size - 1 - k])
                        flag2 = 0;
                }
                cnt += flag1 + flag2;
            }
            printf("#%d %d\n", TC+1, cnt);
        }
    }
}