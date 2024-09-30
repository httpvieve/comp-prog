#include <stdio.h>

int main () {

        int a, b, n;

        scanf ("%d %d %d", &a, &b, &n);

        for (int i = 1; i <= n; i++) {
                if (i % a == 0 ) printf ("Fizz");
                if ( i % b == 0) printf ("Buzz");
                if (i % a != 0 && i % b != 0) printf ("%d", i);

                printf ("\n");
        }
        return 0;
}