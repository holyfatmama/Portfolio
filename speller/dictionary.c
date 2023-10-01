// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// declare word_count and hash_value;
unsigned int word_count;
unsigned int hash_value;

// Returns true if word is in dictionary
//, else false
bool check(const char *word)
{
    // TODO
    hash_value = hash(word);
    node *cursor = table[hash_value];
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        else cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long total = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        total += tolower(word[i]);
    }
    return (total % N);
}

// Loads dictionary into memory, returning true if successful, else false
//, use malloc
bool load(const char *dictionary)
{
    // TODO
    // open dictionary file
    FILE *file = fopen("dictionary", "r");
    if (*file == NULL)
    {
        printf("Unable to open %s\n", dictionary);
        return false;
    }

    // read strings from file, return null if theres nothing
    char *word[LENGTH + 1];

    // allocate memory and copy word into pointer while scanning the entire file for words
    while(fscanf(file, "%s", word) != EOF)
    {
        // allocate memory
        node n* = malloc(sizeof(node));

        // return false if no memory is allocated
        if (n == NUll)
        {
            return false;
        }

        //copy word into pointer n.word
        strcpy (n->word, word);

        // obtain hash value
        hash_value = hash(word);

        // insert node into hash value
        n->next = table[hash_value];
        table[hash_value] = n;
        word_count++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
//(use printf and print number of words)
unsigned int size(void)
{
    // TODO
    if (word_count > 0
    {
        return(word_count);
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
//(use free memory)
bool unload(void)
{
    // TODO
    // iterate through the linked list
    for (int i = 0; i < N; i++)
    {
        // set cursor to start of table
        node *cursor = table[i];

        while (cursor != NULL)
        {
            // create temporary cursor set to the cursor position
            node *tmp = cursor;
            // move cursor to next position
            cursor = cursor->next;
            // free memory
            free(tmp);
        }
        else
        {
            if (cursor == NULL)
        }
        return true;
    }
    return false;
}
