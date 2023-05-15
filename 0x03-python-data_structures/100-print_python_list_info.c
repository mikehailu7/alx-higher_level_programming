#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info: This function Print information regarding python list.
 * @p: This is a python Object.
 * Author: mikias Hailu.
 * Return: This will return nothing.
 */
void print_python_list_info(PyObject *p)
{
PyObject *item;
PyListObject *list = (PyListObject *)p;
int m, length, position;
position = list->allocated;
length = Py_SIZE(p);
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);
for (m = 0; m < size; m++)
{
item =  PyList_GetItem(p, m);
printf("Element %d: %s\n", m, Py_TYPE(item)->tp_name);
}
}
