#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *mid = NULL;
	int result = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		listint_t *next = slow->next;
		slow->next = prev_slow;
		prev_slow = slow;
		slow = next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	while (prev_slow != NULL && slow != NULL)
	{
		if (prev_slow->n != slow->n)
		{
			result = 0;
			break;
		}
		prev_slow = prev_slow->next;
		slow = slow->next;
	}

	fast = prev_slow;
	prev_slow = NULL;
	while (fast != NULL)
	{
		listint_t *next = fast->next;
		fast->next = prev_slow;
		prev_slow = fast;
		fast = next;
	}

	if (mid != NULL)
		mid->next = prev_slow;
	else
		*head = prev_slow;

	return result;
}

