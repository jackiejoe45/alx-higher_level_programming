#include <Python.h>
#include <object.h>
#include <listobject.h>
/*
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *p);
	int size = PyList_Size(p);
	int i = 0;
	PyObject *item;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)list->allocated);
	while (i < size)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		i++;
	}
}
