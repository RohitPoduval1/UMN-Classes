#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "dictionary.h"


int main(int argc, char **argv) {
    dictionary_t* dict = create_dictionary();
    dict = read_dict_from_text_file("test_cases/resources/dictionary_large.txt");
    dict_free(dict);

    dict = read_dict_from_text_file("test_cases/resources/dictionary_large.txt");
    dict_print(dict);
}
