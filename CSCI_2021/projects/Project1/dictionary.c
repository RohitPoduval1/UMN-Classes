#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dictionary.h"

// Creates a dictionary struct and returns a pointer to it
dictionary_t* create_dictionary() {
    dictionary_t* dict = malloc(sizeof(dictionary_t));
    if (dict == NULL) {
        return NULL;
    }
    dict->root = NULL;
    dict->size = 0;
    return dict;
}

// Helper to prepare a new node. Notice the
// lack of a malloc() call in this function.
// Usage:
//   node_t *n = malloc(sizeof(node));
//   new_node(n, word);
// You don't need to use this function, but it is a nice helper.
// This code is correct and should not be modified.
void new_node(node_t* node, const char *key) {
    strcpy(node->word, key);
    node->left = NULL;
    node->right = NULL;
    node->height = 1;
}

// Helper: Returns the larger of two numbers
int max(int a, int b) {
    return (a > b) ? a : b;
}
// Helper to perform the "right" rotation.
// This code is correct and you should not modify it.
node_t *rotate_right(node_t *y)
{
    node_t *x = y->left;
    node_t *t = x->right;
    x->right = y;
    y->left = t;
    y->height = max((y->left != NULL) ? y->left->height : 0, 
                    (y->right != NULL) ? y->right->height : 0) + 1;
    x->height = max((x->left != NULL) ? x->left->height : 0, 
                    (x->right != NULL) ? x->right->height : 0) + 1;
    return x;
}

// Helper to perform the "left" rotation.
// This code is correct and you should not modify it.
node_t *rotate_left(node_t *x)
{
    node_t *y = x->right;
    node_t *t = y->left;
    y->left = x;
    x->right = t;
    x->height = max((x->left != NULL) ? x->left->height : 0, 
                    (x->right != NULL) ? x->right->height : 0) + 1;
    y->height = max((y->left != NULL) ? y->left->height : 0, 
                    (y->right != NULL) ? y->right->height : 0) + 1;
    return y;
}

int get_height(node_t* node) {
    if (node == NULL) {
        return 0;
    }

    // If the node has a child that is not null, use its height, otherwise use 0
    int heightOfLeftSubtree = (node->left != NULL) ? node->left->height : 0;
    int heightOfRightSubtree = (node->right != NULL) ? node->right->height : 0;

    return 1 + max(heightOfLeftSubtree, heightOfRightSubtree);
}

int get_balance_factor(node_t* node) {
    return get_height(node->left) - get_height(node->right);
}

/*
    * Insert a new node with word into the dictionary rooted at root
    * @param root: A node_t* that is the root of the dictionary to insert in
    * @param word: The word you want to insert in the dictionary
    * @return The new root of the dictionary with the word inserted.
    * NULL if something went wrong inserting.
*/
node_t* insert(node_t* root, const char* word) {
    if (root == NULL) {
        node_t* n = malloc(sizeof(node_t));
        if (n == NULL) {  // not enough space from malloc
            return NULL;
        }
        new_node(n, word);
        return n;
    }

    // Finding the correct place to insert the word.
    // we are smaller than the current word so go left
    if (strcmp(word, root->word) < 0) {
        root->left = insert(root->left, word);
    }
    // else go right
    else {
        root->right = insert(root->right, word);
    }

    root->height = get_height(root);

    int bf = get_balance_factor(root);

    // Conditions for which rotation to perform
    
    // Right Rotation
    if (bf > 1 && strcmp(word, root->left->word) < 0) {
        // the tree is left heavy and insertion in the left subtree
        return rotate_right(root);
    }
    // Left Rotation
    if (bf < -1 && strcmp(word, root->right->word) > 0) {
        // tree is right heavy and insertion in the right subtree
        return rotate_left(root);
    }
    // Left-Right Rotation
    if (bf > 1 && strcmp(word, root->left->word) > 0) {
        // left heavy and insertion in right subtree
        root->left = rotate_left(root->left);
        return rotate_right(root);
    }
    // Right-Left Rotation
    if (bf < -1 && strcmp(word, root->right->word) < 0) {
        // right heavy and insertion in left subtree
        root->right = rotate_right(root->right);
        return rotate_left(root);
    }

    return root;
}
// Returns 0 if word was inserted in dict, else 1
int dict_insert(dictionary_t* dict, const char* word) {
	// Assume no word is added to the dict more than once (no duplicates)
    node_t* new_root = insert(dict->root, word);
    if (new_root == NULL) {
        return 1;
    }
    dict->root = new_root;
    (dict->size)++;
    return 0;
}

// Returns 1 if query is found in dict, else 0
int dict_find(const dictionary_t* dict, const char* query) {
    // Approach: Use the property of BSTs to find query
    // (left subtree has elements less than curr)
    // (right subtree has elements greater than or equal to curr)
	node_t* curr = dict->root;
	while (curr != NULL) {
        // need to get smaller since query is smaller than the current word
        // so go left
		if (strcmp(query, curr->word) < 0) {
			curr = curr->left;
		}
        // need to get bigger since query is bigger than the current word
        // so go right
        else if (strcmp(query, curr->word) > 0) {
			curr = curr->right;
		}
        else {
            return 1;
        }
	}
    return 0;
}


// Helper for dict_print
void print_inorder(node_t* root) {
    // Use Inorder traversal to print the words in the dict in alphabetical order
    if (root == NULL) {
        return;
    }
    print_inorder(root->left);
    printf("%s\n", root->word);
    print_inorder(root->right);
}
// Displays all words stored in the dictionary on the screen in ascending alphabetical order.
void dict_print(const dictionary_t* dict) {
    print_inorder(dict->root);
}


// Helper for dict_free
void free_postorder(node_t* root) {
    // Use Postorder traversal to free the nodes starting with the bottom level
    // of the tree working up
    if (root == NULL) {
        return;
    }
    free_postorder(root->left);
    free_postorder(root->right);
    free(root);
}
// Frees all dictionary contents and the dictionary itself
void dict_free(dictionary_t* dict) {
    if (dict != NULL) {              // no need to free a NULL dict
        free_postorder(dict->root);  // free dict contents 
        free(dict);                  // free dict itself
    }
}


/*
    * Given a file_name, return a dictionary_t* that is the dictionary created from that file
    * @param file_name: The name of the file to read from (no requirement on validity)
    * @return A pointer to the newly created dictionary from that file. NULL if no dict could be created
*/
dictionary_t* read_dict_from_text_file(const char* file_name) {
    dictionary_t* new_dict = create_dictionary();
    if (new_dict == NULL) {
        return NULL;
    }

    FILE* file = fopen(file_name, "r");
    if (file == NULL) {
        dict_free(new_dict);  // new_dict is not NULL so it must be freed
        return NULL;
    }

    char word[MAX_WORD_LEN + 1];
    while(fscanf(file, "%s", word) != EOF) {
        dict_insert(new_dict, word);
    }

    fclose(file);
    return new_dict;
}


/*
    * Helper for write_dict_to_text_file that writes the contents of the dictionary rooted at root in
    * alphabetical order to file
    * @param root: The root of the dictionary that contains the words to be written
    * @param file: The file that should be written to (file should be valid)
    * @return void, writes the contents to file
*/
void fwrite_inorder(node_t* root, FILE* file) {
    if (root == NULL) {
        return;
    }
    fwrite_inorder(root->left, file);
    fprintf(file, "%s\n", root->word);
    fwrite_inorder(root->right, file);
}
/*
 * Writes the contents of a dictionary dict to a text file named file_name
 * @param dict: The dictionary to write
 * @param file_name: The name of the text file to write to
 * @return: 0 if the write was successful, 1 if it failed
 */
int write_dict_to_text_file(const dictionary_t* dict, const char* file_name) {
    if (dict == NULL) {
        return 1;
    }

    // Writes to file, if file does not exist, C will create a file named <fileName>.txt
    FILE* file = fopen(file_name, "w");
    if (file == NULL) {
        return 1;
    }
    
    fwrite_inorder(dict->root, file);
    fclose(file);
    return 0;
}
