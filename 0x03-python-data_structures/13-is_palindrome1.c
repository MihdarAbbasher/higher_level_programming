#include "lists.h"

/**
 * reverse_listint - thsi reverse a list
 * @head: the head of list
 * Description: this function reverse list
 * section header: the header of this function is lists.h)*
 * Return: reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *tmp, *actual;

	if (*head == NULL)
		return (NULL);

	actual = *head;

	while (actual->next)
	{
		tmp = actual->next;
		actual->next = tmp->next;
		tmp->next = *head;
		*head = tmp;
	}
	return (*head);
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
 * cp_list - copy list
 * @head: pointer to head of list
 * Return: ptr to new list
 */
listint_t *cp_list(listint_t **head)
{
	listint_t *my_list, *current;

	my_list = malloc(sizeof(listint_t) * listint_len(*head));
	current = *head;
	while (current != NULL)
	{
		add_nodeint_end(&my_list, current->n);
		current = current->next;
	}
	return (my_list);
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
	listint_t *list_copy, *curr;
	int len_half, len, i;

	curr = *head;
	len =  listint_len(*head);
	len_half =  len / 2;

	if (len < 2)
		return (1);
	
	for (i = 0; i < len_half; i++)
		curr = curr->next;
	if (len % 2 == 1)
		curr = curr->next;
	list_copy = cp_list(&curr);
	reverse_listint(&list_copy);
	
	for (i = 0; i < len_half; i++)
	{
		if (curr->n != list_copy->n)
		{
			free(list_copy);
			return (0);
		}
		curr = curr->next;
		list_copy = list_copy->next;
	}
	return (1);
}
