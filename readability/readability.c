#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);


int main (void)
{
    string text = get_string("Text: ");

    int letters = count_letters(text);

    int words = count_words(text);

    int sentences = count_sentences(text);


    float L = letters / words * 100;
    float S = sentences / words * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before grade one\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("grade %i\n", index);
    }

}

int count_letters(string text)
{
    int letters = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]) != 0)
        letters++;
    }
    return letters;
}

int count_words(string text)
{
    int words = 1;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]) !=0)
        {
            words++;
        }
    }
    return words;
}

int count_sentences(string text)
{
    int sentences = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i]) == '.' || (text[i]) == '!' || (text[i]) == '?')
        {
            sentences++;
        }
    }
    return sentences;
}

