#include <stddef.h>

/**
 * Definition for singly-linked list.
 * struct listint_s {
 *     int n;
 *     struct listint_s *next;
 * };
 * typedef struct listint_s listint_t;
 */

int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL) {
        return 1;  /* Empty list or a list with one element is considered a palindrome*/
    }
    
    listint_t *slow = *head;
    listint_t *fast = *head;
    
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    /* Reverse the second half of the list*/
    listint_t *prev = NULL;
    listint_t *current = slow;
    listint_t *next = NULL;
    
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    
    /* Compare the first half and reversed second half*/
    listint_t *first = *head;
    listint_t *second = prev;
    
    while (second != NULL) {
        if (first->n != second->n) {
            return 0;  /* Not a palindrome*/
        }
        first = first->next;
        second = second->next;
    }
    
    return 1;  /* It is a palindrome*/
}

