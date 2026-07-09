def total(*args):
    return sum(args)

print(total(1, 2, 3))
print(total(1, 2, 3, 4, 5))

def build_stock(**kwargs):
    return kwargs

print(build_stock(ticker="AAA", price=10))

def log_call(action, *args, **kwargs):
    print(f"{action} called with args={args}, kwargs={kwargs}")

log_call("create_stock", "AAA", 10, active=True)

def create_stock(ticker, price):
    return {"ticker": ticker, "price": price}

args = ["AAA", 10]
print(create_stock(*args))

kwargs = {"ticker": "AAA", "price": 10}
print(create_stock(**kwargs))

def log_wrapper(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_wrapper
def add(a, b):
    return a + b

print(add(2, 3))
