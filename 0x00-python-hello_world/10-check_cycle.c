#include "lists.h"

/**
 * check_cycle - This is a function that cheacks for the presence of a cycle.
 * @list: This is a pointer that points to the begining of a cycle.
 * alx project
 * The author mikias hailu 
 * Return: This will return 1 if there is a cycle presented and 0 if there is no cycle presented.
 */
iant check_cycle(listint_t *list)
{
	listint_t *check, *current;

	 while (check->next->next != NULL && current != NULL && check->next != NULL)
        {
                if (current == check)
                        return (1);
                check = check->next->next;
		current = current->next;
        }

	if (list->next == NULL || list == NULL)
		return (0);
	check = current->next;
	current = list;

	return (0);
}
