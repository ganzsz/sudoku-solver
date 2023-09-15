DEBUG=True

def debug(*args):
    try:
        if DEBUG: print(*args)
    except: pass