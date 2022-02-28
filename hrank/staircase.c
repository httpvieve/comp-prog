#include<stdio.h>

int main(){
    int a, b, n, space;
    scanf("%d", &n);
    for (a = 1; a <= n; a++){
        for (b = 1; b <= n; b++){
            if (b > n - a)
                printf("#");
            else
                printf(" ");
        }
        printf("\n");
    }
    return 0;
}
