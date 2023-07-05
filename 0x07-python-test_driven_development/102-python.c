#include "Python.h"

/**
 * print_python_string: This function will Prints information about Python strings.
 * @p: A PyObject string object.
 * Author: MikiasHailu
 * project: pythonstrings
 */

void print_python_string(PyObject *p)
{
	long int leng;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	leng = ((PyASCIIObject *)(p))->leng;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  leng: %ld\n", leng);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &leng));
}
