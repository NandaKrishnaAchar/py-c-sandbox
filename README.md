# Sandboxing in Python


## Project Structure

```
.
└── cpython-sandbox
    ├── hello.h             # C header file with hello_world() function
    ├── hello_wrapper.pyx   # Cython wrapper file
    ├── setup.py            # Build configuration script
    ├── main.py             # Python entry point

└── exploits
    ├── null_ptr_cpy/
    ├── crash.c            
    ├── crash.dylib        
    ├── crash.wasm         
    ├── exploit.py         
    ├── requirements       
    └── sandbox.py     
├── .gitignore              
└── README.md
```