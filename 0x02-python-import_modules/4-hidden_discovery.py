#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    items = dir(hidden_4)
    for name in items:
        if not name.startswith('__'):
            print(name)
