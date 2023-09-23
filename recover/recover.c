#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // check for two command line argument, else return an error
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // open memory card
    FILE *input_file = fopen(argv[1], "r");

    // check if input_file is valid
    if (input_file == NULL)
    {
        printf("Could not open file\n");
        return 2;
    }

    // store blocks of 512 bytes in an array
    unsigned char buffer[512];

    // Track number of images generated
    int count_image = 0;

    // file pointer for recovered images
    FILE *output_file = NULL;

    // allocate memory for name of file, char filename[8]
    char *filename = malloc(8 * sizeof(char));

    // open file
    while (fread(buffer, sizeof(char), 512, input_file))
    {
        // check if bytes are the start of a jpeg file
        if (buffer [0] == 0xff && buffer [1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // write the jpeg filenames
            sprintf(filename, "%03i.jpg", count_image);

            // open output file
            output_file = fopen(filename, "w");

            // count number of images found;
            count_image++;
        }
        // check if output has been used for valid input;
        if (output_file != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output_file);
        }
    }
    free(filename);
    fclose(output_file);
    fclose(input_file);

    return 0;
}