#include <stdlib.h>
#include "linked_list.h"

int list_find_student(list_t *list, int value) {
    node_t* curr = list->head;
	int count = 0;

	while (curr) {
		if (curr->value == value) {
			return count;
		}

		curr = curr->next;
		count++;
	}

    return -1;
}
