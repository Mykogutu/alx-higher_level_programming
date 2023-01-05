#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * check_cycle - checks if a singly-linked list contains a cycle
 * @list: A singly-linked list.
 *
 * Return: 0 If there is no cycle and 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *one, *two;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	one = list->next;
	two = list->next->next;
	while(one && two && two->next)
	{
		if (one == two)
		{
			return (1);
		}
		one = one->next;
		two = two->next->next;
	}
	return (0);
}
