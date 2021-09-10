def cleaner():
    from subprocess import run
    try:
        run('cls', shell=True)
    except:
        