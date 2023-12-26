#include <stdio.h>

int main()
{
    int var = 10;

    // declaring pointer variable to store address of var
    int *ptr = &var;

    printf("The address in decimal : %i \n", *ptr);
    printf("The address in hexadecimal : %p \n", &ptr);

    printf("%p\n", &var);
    return 0;
}
