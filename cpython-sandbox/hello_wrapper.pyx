# hello_wrapper.pyx

# Include the C header file
cdef extern from "hello.h":
    void hello_world()

# Python wrapper function
def py_hello_world():
    """Python wrapper for the C hello_world function"""
    hello_world()