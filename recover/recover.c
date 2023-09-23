#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // check for two command line argument, else return an error
    if (argc != 2)
    {
        printf("Usage: ./recover Image\n");
        return 1;
    }

    // open memory card
    FILE *input_file = fopen (argv[1], "r");

    // check if input_file is valid
    if (input_file = NULL)
    {
        printf("no input file found\n");
    }

    // store blocks of 512 bytes in an array
    unsigned char buffer[512;

    // Track number of images generated
    int image_count = 0;

    // file pointer for recovered images
    

    // look for jpeg file
    if (buffer [0] == 0xff && buffer [1] == 0xd8 && buffer[2] == 0xff)

    // write 512 bytes into new file until new jpeg file is found



}