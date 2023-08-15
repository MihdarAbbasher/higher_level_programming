#include "lists.h"

/**
 * get_node - get node at index idx
 * @head: the head of list
 * @idx: the head of list
 * Description: this function reverse list
 * section header: the header of this function is lists.h)*
 * Return: reversed list
 */
listint_t *get_node(listint_t **head, int idx)
{
	listint_t *tmp;

	if (*head == NULL)
		return (NULL);

	tmp = *head;
	i = 0;
	while (i < idx)
	{
		tmp = tmp->next;
		i++;
	}
	return (*tmp);
}

/**
 * listint_len - count the number of elements
(* a blank line
*@h: the list
* Description: count the number of elements)?
(* section header: the header of this function is lists.h)*
* Return: this return the num of the elements in the list
*/
size_t listint_len(const listint_t *h)
{
	size_t i;

	for (i = 0; h; i++)
	{
		h = h->next;
	}
	return (i);
}


/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev_curr, *curr;
	int len_half, i;

	
	lenn =  listint_len(*head);
	len_half = lenn / 2;
	curr = *head;
	rev_curr = get_node(head, lenn - 1);
	for (i = 0; i < len_half; i++)
	{
		rev_curr = get_node(head, len - 1 - i);
		if (curr->n != rev_curr->n)
			return (0);
		curr = curr->next;
	}
	return (1);
}
