#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO

    string message = get_string("What is the message?\n");

    // Convert decimal to binary (8bit)

    for (int i = 0, n = strlen(message); i < n; i++);

    int decimal = message[i];

    int binary[] = {0, 0, 0, 0, 0, 0, 0, 0};
    {
        binary[j] = decimal % 2;
        decimal / 2;
        j++;
    }

    for (int k = )

    while decimal > 0
    {

    }

    // print bulbs

    message[i]
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
