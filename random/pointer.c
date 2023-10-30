#include <stdio.h>

int main (void)
{
    char * s = "HI!";
    printf("%p\n", s);
    printf("%p\n", &s[0]);
}
