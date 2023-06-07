#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("how high is the tower?\n");
    }
    while (n <1);
}