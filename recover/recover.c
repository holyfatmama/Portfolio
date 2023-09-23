#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // if more than one argument, ask for another one
    if (argc != 2)
    {
        printf("Usage: ./recover Image\n");
        return 1;
    }
    // open memory card
    FILE *input_file = fopen (argv[1], "r");

    // look for jpeg file

    // write 512 bytes until new jpeg file is found

    // fread(data, size, number, inputr)

}