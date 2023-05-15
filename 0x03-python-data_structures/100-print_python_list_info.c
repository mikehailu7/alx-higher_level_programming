#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - This function wil display about lists in python.
 * @p: p is used to declear pythonobject.
 * MikiasHailu.
 * Return: Will return the correct size if it is true.
 * @m: m is an integer.
 * @length: used to contain the length. 
 * @position:used to contain the position.
*/
void print_python_list_info(PyObject *p)
{
PyObject *item;
PyListObject *list = (PyListObject *)p;
int m, length, position;
length = Py_SIZE(p);
position = list->allocated;
printf("[*] Size of the Python List = %d\n", length);
printf("[*] Allocated = %d\n", position);
for (m = 0; m < size; m++)
{
item =  PyList_GetItem(p, m);
printf("Element %d: %s\n", m, Py_TYPE(item)->tp_name);
}
}
