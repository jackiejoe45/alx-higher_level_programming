#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Define custom macros */
#define GET_PY_SIZE(obj) \
	(((PyVarObject *)obj)->ob_size)

#define GET_PY_TYPE(obj) \
	(((PyObject *)obj)->ob_type)

#define GET_PY_LIST_ITEM(list, index) \
	(((PyListObject *)(list))->ob_item[index])

#define GET_PY_BYTES_SIZE(bytes) \
	(GET_PY_SIZE(bytes))

#define GET_PY_BYTES_ITEM(bytes, index) \
	(((PyBytesObject *)(bytes))->ob_sval[index])

#define GET_PY_FLOAT_VALUE(float_obj) \
	(*((double *)((PyFloatObject *)(float_obj))->ob_fval))

/* Function prototypes */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/* Function implementations */
/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	if (GET_PY_TYPE(p) != &PyBytes_Type)
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = GET_PY_BYTES_SIZE(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);

	printf("  trying string: ");
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)GET_PY_BYTES_ITEM(p, i));
	}
	printf("\n");
}

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	if (GET_PY_TYPE(p) != &PyList_Type)
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = GET_PY_SIZE(p);

	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = GET_PY_LIST_ITEM(p, i);

		printf("Element %zd: ");

		if (GET_PY_TYPE(item) == &PyFloat_Type)
		{
			double value = GET_PY_FLOAT_VALUE(item);

			printf("[.] float object info\n");
			printf("  value: %f\n", value);
		} else if (GET_PY_TYPE(item) == &PyLong_Type)
		{
			long value = PyLong_AsLong(item);

			printf("[.] int object info\n");
			printf("  value: %ld\n", value);
		} else if (GET_PY_TYPE(item) == &PyBytes_Type)
		{
			Py_ssize_t bytes_size = GET_PY_BYTES_SIZE(item);

			printf("[.] bytes object info\n");
			printf("  size: %zd\n", bytes_size);
			printf("  trying string: ");
			for (Py_ssize_t j = 0; j < bytes_size && j < 10; j++)
			{
				printf("%02x ", (unsigned char)GET_PY_BYTES_ITEM(item, j));
			}
			printf("\n");
		} else if (GET_PY_TYPE(item) == &PyUnicode_Type)
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
	if (GET_PY_TYPE(p) != &PyFloat_Type)
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	double value = GET_PY_FLOAT_VALUE(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
