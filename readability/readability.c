#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
float L;
float S;


int main (void)
{
    string text = get_string("Text: ");
    printf("%s\n", text);

    int letters = count_letters(text);

    int words = count_words(text);

    int sentences = count_sentences(text);

    int index = 0.0588 * L - 0.296 * S - 15.8;

    L = letters/100;
    S = sentences/100;

    printf("%i grade\n", index);
}

int count_letters(string text)
{
    int letters = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]) != 0)
        letters++;
    }
    printf("%i letters\n", letters);
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
    printf("%i word(s)\n", words);
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
    printf("%i sentence(s)\n", sentences);
    return sentences;
}

