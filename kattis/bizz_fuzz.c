
#include <stdio.h>

long long int gcd (long long int a, long long int b) {
    return b == 0 ? a : gcd (b, a % b);
}
int main () {

    long long int a, b, c, d;
    long long int key, res;
    scanf ("%lli %lli %lli %lli", &a, &b, &c, &d);
    
    key = (c * d) / gcd (c, d);
    res = (b / key) - (a / key) + (a % key == 0 ? 1 :0);
    printf ("%lli", res);
    
    return 0;
}