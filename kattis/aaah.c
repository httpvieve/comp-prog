#include <stdio.h>
#include <string.h>
int main () {

    char* jm__line, d__line;
    scanf ("%s %s", &jm__line, &d__line);
    if (strlen (jm__line) < strlen (d__line)) printf ("no");
    else printf("go");
    return 0;
     
}