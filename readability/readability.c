#include <cs50.h>
#include <stdio.h>
#include <ctype.h>


int main (void)

{
    string text = get_string("Text:");
    printf("%s\n", text);

    letters = int count_letters(text);
    printf("%i\n", letters);
}