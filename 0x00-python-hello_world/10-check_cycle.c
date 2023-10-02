#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it or not.
 * @list: points to the beginning of the node
 * Return: 0 if cycle is absent, 1 if cycle is present
 *
 * By: Sina Mathew
 */
int check_cycle(listint_t *list)
{
	listint_t *present, *checker;

	if (list == NULL || list->next == NULL)
		return (0);
	present = list;
	checker = present->next;

	while (present != NULL && checker->next != NULL
		&& checker->next->next != NULL)
	{
		if (present == checker)
			return (1);
		present = present->next;
		checker = checker->next->next;
	}
	return (0);
}
