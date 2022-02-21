#include<stdio.h>

int main(int argc, char **argv)
{
        int i, j, k, a, b;

        scanf("%d", &k);
        a = k/2;
        b = (k + 1)/2;
        printf("%d\n", a * b);
        for(i = 1; i <= a + 1; i++){
                for(j = a + 1; j <= k + 1; j++){
                        printf("%d %d\n",i, j);
                }
        } 
        return 0;
}