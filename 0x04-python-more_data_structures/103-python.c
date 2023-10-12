#include <Python.h>

/**
 * print_python_list - C is hard
 * @p: Fucking hard
 *
 * By: Sina Mathew
 */
void print_python_list(PyObject *p) {
	PyListObject *list;
	Py_ssize_t i, size, allocated;

	if (!PyList_Check(p)) {
		PyErr_Format(PyExc_TypeError, "Invalid List Object");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; ++i) {
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GET_ITEM(list, i))->tp_name);
	}
}

/**
 * print_python_bytes - C ain't fun
 * @p: Maybe not anymore
 *
 * By: Sina Mathew
 */
void print_python_bytes(PyObject *p) {
	PyBytesObject *bytes;
	Py_ssize_t size, i;
	char *string;

	if (!PyBytes_Check(p)) {
		PyErr_Format(PyExc_TypeError, "Invalid Bytes Object");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_GET_SIZE(p);
	string = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; ++i) {
		printf("%02hhx", string[i]);
		if (i < 9) {
			printf(" ");
		}
	}
	printf("\n");
}
