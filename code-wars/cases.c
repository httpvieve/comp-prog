#include<stdio.h>

int same_case (char a, char b)
{
  char i, j, m, n; 
  int k = 0, l = 0;
  for(m = 'a'; m <= 'z'; m++){
    i = m;
  }
  for(n = 'A'; n <= 'Z'; n++){
     j = n;
  }
        if(a == i)
        k = 1;
    if(b == i)
        k = 2;
    if(b == i && a == i)
        k = 3;
        if(a == j)
        l = 1;
     if(b == j)
        l = 2;
      if(b == j && a == j)
        l == 3;
  if((k == 1 && l == 2)||(k == 2 && l == 1))
    return 0;
  else if(k == 3 || l == 3)
    return 1;
  else 
    return -1;
}
int main(){
        printf("%d", same_case('a','B'));
        return 0;
}