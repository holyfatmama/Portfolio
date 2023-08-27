#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO

    string message = get_string("What is the message?\n")

    // Convert decimal to binary (8bit)

    for (int i = 0; i < strlen(message); i++)
        {
            if message[i] % 2 == 0
        }
        {
            else if message[i] % 2 == 1
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
