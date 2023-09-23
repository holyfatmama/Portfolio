#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint_8 BYTE;

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
    unsigned char buffer[512];

    // Track number of images generated
    int image_count = 0;

    // file pointer for recovered images
    FILE *output_file = NULL;

    // allocate memory for name of file, char filename[8]
    char *filename = malloc(8* sizeof(char))

    // open file
    while (fread(buffer, sizeof(char), 512, argv[1]))
    {
        // check if bytes are the start of a jpeg file
        if (buffer [0] == 0xff && buffer [1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xef)
        {
            sprintf(output_file, "%3i.jpg", image_count);
            FILE *filename = fopen(output_file, "w");
            fwrite(buffer, sizeof(char), 512,)
        }

    }




    // write 512 bytes into new file until new jpeg file is found



}