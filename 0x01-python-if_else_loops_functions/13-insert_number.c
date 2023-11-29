#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - inserts node in here postion in sorted linked list
 * @head: pointer to the first node
 * @number: integer to be included in new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	node = *head;
	while (node->next->n < number)
	{
		node = node->next;
	}
	newnode->n = number;
	newnode->next = node->next;
	node->next = newnode;
	return (newnode);
}
