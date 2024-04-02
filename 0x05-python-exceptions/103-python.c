#include "<Python.h>"
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list - Prints basic info about Python lists
 * @p: Pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	setbuf(stdout, NULL);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	size = PyList_Size(p);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first 10 bytes:");
	for (i = 0; i < size && i < 10; i++)
	{
		printf(" %02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python floats
 * @p: Pointer to a Python object
 */
void print_python_float(PyObject *p)
{
	setbuf(stdout, NULL);

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %.17g\n", ((PyFloatObject *)p)->ob_fval);
}
