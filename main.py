# Import the Cython module
import hello_wrapper

# Call the wrapped function
if __name__ == "__main__":
    print("Calling C function from Python through Cython:")
    hello_wrapper.py_hello_world()
    print("Done!")