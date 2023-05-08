#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
 * struct listint_s - This is used if singly linked lists are presented
 * @k: This is an integer
 * mikias hailu
 * @nxt: This is a pointer that points to the next node
 * alx project
 */
typedef struct listint_s
{
	 struct listint_s *nxt;
	 int k;
} listint_t;

size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);
void free_listint(listint_t *head);
listint_t *add_nodeint(const int k, listint_t **head);

#endif 
