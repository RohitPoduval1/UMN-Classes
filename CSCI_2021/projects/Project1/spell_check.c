#include <ctype.h>
#include <stdio.h>
#include <string.h>

#include "dictionary.h"

#define MAX_CMD_LEN 128
#define ERROR 1


/*
 * A helper function to spell check a specific file
 * @param file_name: Name of the file to spell check (no requirement on validity of file)
 * @param dict: A dictionary containing correct words
 * @return 0 if the file was checked successfully, 1 if something went
 * wrong reading the file
*/
int spell_check_file(const char* file_name, const dictionary_t* dict) {
    FILE* file = fopen(file_name, "r");
    if (file == NULL) {
        return ERROR;
    }

    char line[200];
    const char MISSPELL_MARKER[4] = "[X]";

    while (fgets(line, sizeof(line), file) != NULL) {
        // tokenize by either spaces (" "), tabs ('\t'), or newlines ('\n')
        char* word = strtok(line, " \t\n");
        while (word != NULL) {
            if (dict_find(dict, word) == 1) {
                printf("%s ", word);
            }
            else {
                printf("%s%s ", word, MISSPELL_MARKER);
            }

            // NULL so tokenization can continue where it left off to progress the loop
            word = strtok(NULL, " \t\n");
        }
        printf("\n");  // to preserve original formatting
    }

    fclose(file);
    return 0;
}

/*
 * This is in general *very* similar to the list_main file seen in lab 2
 */
int main(int argc, char **argv) {
    dictionary_t* dict = create_dictionary();
    if (dict == NULL) {  // not enough memory from malloc for dict
        return ERROR;
    }
    char cmd[MAX_CMD_LEN + 1];


    if (argc > 1) {
        const char* dict_file_name = argv[1];
        dictionary_t* newDict = read_dict_from_text_file(dict_file_name);
        if (newDict == NULL) {
            printf("Failed to read dictionary from text file\n");
            dict_free(dict);
            return ERROR;
        }
        printf("Dictionary successfully read from text file\n");
        dict_free(dict);
        dict = newDict;

        // ./spell_check <dictionary_file> <spell_check_file> then terminate the program
        if (argc == 3) {
            const char* spell_check_file_name = argv[2];

            int spell_check_status = spell_check_file(spell_check_file_name, dict);
            if (spell_check_status == ERROR) {
                printf("Spell check failed\n");
                dict_free(dict);
                return ERROR;
            }

            dict_free(dict);
            return 0;
        }
    }


    printf("CSCI 2021 Spell Check System\n");
    printf("Commands:\n");
    printf("  add <word>:              adds a new word to dictionary\n");
    printf("  lookup <word>:           searches for a word\n");
    printf("  print:                   shows all words currently in the dictionary\n");
    printf("  load <file_name>:        reads in dictionary from a file\n");
    printf("  save <file_name>:        writes dictionary to a file\n");
    printf("  check <file_name>: spell checks the specified file\n");
    printf("  exit:                    exits the program\n");

    while (1) {
        printf("spell_check> ");
        if (scanf("%s", cmd) == EOF) {
            break;
        }

        else if (strcmp("exit", cmd) == 0) {
            break;
        }

        else if (strcmp("add", cmd) == 0) {
            char word[MAX_WORD_LEN + 1];
            scanf("%s", word);
            dict_insert(dict, word);
		}

        else if (strcmp("lookup", cmd) == 0) {
            char word[MAX_WORD_LEN + 1];
            scanf("%s", word);
            int find_status = dict_find(dict, word);
            if (find_status == 1) {
                printf("'%s' present in dictionary\n", word);
            }
            else {
                printf("'%s' not found\n", word);
            }
		}

        else if (strcmp("print", cmd) == 0) {
			dict_print(dict);
		}

        else if (strcmp("load", cmd) == 0) {
            char file_name[MAX_CMD_LEN + 1];
            scanf("%s", file_name);
            dictionary_t* newDict = read_dict_from_text_file(file_name);
            if (newDict == NULL) {
                printf("Failed to read dictionary from text file\n");
                continue;
            }
            dict_free(dict);
            dict = newDict;
            printf("Dictionary successfully read from text file\n");
		}

        else if (strcmp("save", cmd) == 0) {
            char file_name[MAX_CMD_LEN + 1];
            scanf("%s", file_name);
            int write_status = write_dict_to_text_file(dict, file_name);
            if (write_status == ERROR) {
                printf("Failed to write dictionary to text file\n");
            }
            else {
                printf("Dictionary successfully written to text file\n");
            }
		}

        else if (strcmp("check", cmd) == 0) {
            char file_name[MAX_CMD_LEN + 1];
            scanf("%s", file_name);
            
            int spell_check_status = spell_check_file(file_name, dict);
            if (spell_check_status == ERROR) {
                printf("Spell check failed\n");
            }
		}

        else {
            printf("Unknown command %s\n", cmd);
        }
    }

    dict_free(dict);
    return 0;
}
