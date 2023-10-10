#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *slow_ptr = *head, *fast_ptr = *head, *prev = *head;
listint_t *second_half, *midnode = NULL;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (fast_ptr != NULL && fast_ptr->next != NULL)
{
fast_ptr = fast_ptr->next->next;
prev = slow_ptr;
slow_ptr = slow_ptr->next;
}

if (fast_ptr != NULL)
{
midnode = slow_ptr;
slow_ptr = slow_ptr->next;
}

second_half = slow_ptr;
prev->next = NULL;
reverse_list(&second_half);

is_palindrome = compare_lists(*head, second_half);

reverse_list(&second_half);

if (midnode != NULL)
{
prev->next = midnode;
midnode->next = second_half;
}
else
{
prev->next = second_half;
}

return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list in-place
 * @head: pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
listint_t *prev = NULL, *current = *head, *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

/**
 * compare_lists - compares two linked lists for equality
 * @list1: first linked list
 * @list2: second linked list
 * Return: 1 if equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
while (list1 != NULL && list2 != NULL)
{
if (list1->n != list2->n)
return (0);
list1 = list1->next;
list2 = list2->next;
}

if (list1 == NULL && list2 == NULL)
return (1);

return (0);
}
