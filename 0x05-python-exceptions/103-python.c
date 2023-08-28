#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *obj;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		if (strcmp(Py_TYPE(obj)->tp_name, "bytes") == 0)
			print_python_bytes(obj);
	}

}

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");
	if (strcmp(Py_TYPE(p)->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size > 10)
		size = 10;
	else
		size++;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size - 1; i++)
		printf("%02hhx ", string[i]);
	printf("%02hhx\n", string[i]);
}

/**
 * print_python_float - prints some basic info about Python float
 * @p: pointer to PyObject
 */
void print_python_float(PyObject *p)
{
	char *buffer;

	printf("[.] float object info\n");
	if (strcmp(Py_TYPE(p)->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(((PyFloatObject *)p)->ob_fval,
			'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	free(buffer);
}


