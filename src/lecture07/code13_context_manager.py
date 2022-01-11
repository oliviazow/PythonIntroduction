class MyContextManager:
    def __init__(self):
        print("MyContextManager init", id(self))
    def __enter__(self):
        print("Entering 'with' context")
        return self
    def __exit__(self, exception_type, exception_val, exception_traceback):
        print(f"{exception_type=} {exception_val=} {exception_traceback=}")
        print(exception_traceback)
        print("Exiting 'with' context")
        return True


ctx_mgr = MyContextManager()
print("About to enter 'with' context")
with ctx_mgr as mgr:
    print("Inside 'with' context")
    print(id(mgr))
    raise Exception("Exception inside 'with' context")
    print("This line will never be reached")
print("After 'with' context")
