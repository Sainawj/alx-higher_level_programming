#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int length;
	const char *type;

	fflush(stdout);

	printf("[.] string object info\n");

	type = PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object";
	length = ((PyASCIIObject *)(p))->length;

	printf("  type: %s\n", type);
	printf("  length: %ld\n", length);

	printf("  value: %.*ls\n", (int) length, ((PyASCIIObject *) p)->wstr);
}
