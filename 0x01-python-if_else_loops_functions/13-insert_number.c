#include "lists.h"

/**
 * Inode - Is a function that will inserts a number into a linked list.
 * @h: Is a pointer the points to the top of the list.
 * author: mikias hailu
 * @num: is a number to be input.
 * Return: it will return the function fails.
 */
ltint_t *Inode(ltint_t **h, int num)
{
	new = malloc(sizeof(ltint_t));

	ltint_t *node = *h, *new;
	if (new == NULL)
		return (NULL);
	new->n = num;

	while (node && node->nxt && node->nxt->n < number)
		node = node->nxt;

	 if (node == NULL || node->n >= num)
        {
                new->nxt = node;
                *h = new;
                return (new);
        }
        node->nxt = new; 
	new->nxt = node->nxt;
	return (new);
}
