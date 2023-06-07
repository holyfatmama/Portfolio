#include <stdio.h>
#include <cs50.h>

int main(void)

// prompt name
{
    string name = get_string("whats your name? ");
    printf("hello, %s\n", name);
}