#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text);
int main (void)

{
    string text = get_string("Text: ");
    printf("%s\n", text);
    
    int letters = count_letters(text);
}

int count_letters(string text)
{
    int counter = 0;

    for (int i = 0; i< strlen(text); i++)
    {
        if (isalpha(text[i]) != 0)
        counter++;
    }
    printf("%i letters\n", counter);
    return counter;
}

