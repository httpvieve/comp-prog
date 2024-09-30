


#include <stdio.h>

int main () {

        long long int base, height;

        scanf ("%lli %lli", &base, &height);
        if ((base % 2 == 0) && (height % 2 == 0)) printf ("%d", (base * height)/2);
        else printf ("%f", (base * height)/2.0);
        return 0;
}