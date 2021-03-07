def wel():
    for i in 'Loading... ':
        for n in range(30):
            print((random.choice(string.ascii_letters + string.digits + '.') + '\x08'), end='', flush=True)
            time.sleep(0.03)

        print(i, end='', flush=True)

wel()