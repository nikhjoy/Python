def check_scope():
    def do_local():
        test = "local test"

    def do_non_local():
        test = "non local test"

    def do_global():
        test = "global test"

    test = "default"
    do_local()
    print("test value after do local: "+test)

check_scope()