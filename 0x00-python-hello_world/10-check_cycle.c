#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
*/

int check_cycle(listint_t *list)
{
	listint_t *list1 = list;
	listint_t *list2 = list;

	while (list1 && list2 && list2->next)
	{
		list1 = list1->next;
		list2 = list2->next->next;

		if (list1 == list2)
			return (1);
	}
	return (0);
}
