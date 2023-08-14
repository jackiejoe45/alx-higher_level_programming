#include "lists.h"
/*
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int len = 0, i = 0, j = 0;
	int *array;

	if (!head)
		return (0);
	if (!*head)
		return (1);
	while (current)
	{
		len++;
		current = current->next;
	}
	array = malloc(sizeof(int) * len);
	if (!array)
		return (0);
	current = *head;
	while (current)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}
	while (j < len / 2)
	{
		if (array[j] != array[len - j - 1])
		{
			free(array);
			return (0);
		}
		j++;
	}
	free(array);
	return (1);
}
