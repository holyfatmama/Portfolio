#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("how high is the tower?\n");
    }
    while (height < 1 || height >  8);

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column <= row; column++)
        {
            printf("#");
        }
        printf("\n");
    }
}
