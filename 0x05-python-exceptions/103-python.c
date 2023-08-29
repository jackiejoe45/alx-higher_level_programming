#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);


/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: ");
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
	printf("\n");
}


/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %zd: ", i);

		if (PyFloat_Check(item))
		{
			double value = PyFloat_AsDouble(item);

			printf("[.] float object info\n");
			printf("  value: %f\n", value);
		} else if (PyLong_Check(item))
		{
			long value = PyLong_AsLong(item);

			printf("[.] int object info\n");
			printf("  value: %ld\n", value);
		} else if (PyBytes_Check(item))
		{
			Py_ssize_t bytes_size = PyBytes_Size(item);

			printf("[.] bytes object info\n");
			printf("  size: %zd\n", bytes_size);
			printf("  trying string: ");
			for (Py_ssize_t j = 0; j < bytes_size && j < 10; j++)
				printf("%02x ", (unsigned char)PyBytes_AS_STRING(item)[j]);
			printf("\n");
		} else if (PyUnicode_Check(item))
		{
			Py_ssize_t unicode_size = PyUnicode_GET_LENGTH(item);

			printf("[.] string object info\n");
			printf("  length: %zd\n", unicode_size);
		} else
		{
			printf("Unknown object type\n");
		}
		Py_XINCREF(item);
		Py_XDECREF(item);
	}
}


/**
 * print_python_float - prints some basic info about Python float
 * @p: pointer to PyObject
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}


