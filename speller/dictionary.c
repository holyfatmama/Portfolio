// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

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

// Returns true if word is in dictionary
//, else false
bool check(const char *word)
{
    // TODO

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    //, use some sort of for loop, A is a char (ascii)
    return toupper(word[0]) - 'A';
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
    
    fscanf(file, "%s", word);
    if (word == NULL)
    {
        return;
    }
    // create new node for each word using malloc
    node n* = malloc(sizeof(node));

    // hash word to obtain a hash value

    // insert node into hash table at that location
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
//(use printf and print number of words)
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
//(use free memory)
bool unload(void)
{
    // TODO
    return false;
}
