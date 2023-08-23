#include <cs50.h>
#include <stdio.h>
#include <ctype.h>


int main (void)
int count_letters(string text)

{
    text = get_string("Text:");
    printf("%s\n", text);

    int letters = count_letters(text);
    printf("%i\n", letters);
}