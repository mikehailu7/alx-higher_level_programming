#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct ltint_s - This right herer represents single linked list.
 * @k: This is an integer.
 * c program
 * @nxt: This is a pointer that points to the nxt node
 * mikias hailu
 * Description: singly linked list node structure
 */
typedef struct ltint_s
{
	struct ltint_s *nxt;
	int k;
} ltint_t;

size_t print_ltint(const ltint_t *h);
ltint_t *Inode(ltint_t **h, int number);
ltint_t *add_nodeint_end(listint_t **h, const int k);
void free_ltint(ltint_t *h);

#endif

