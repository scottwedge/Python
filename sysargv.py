for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
           print 'no pude abrir', arg
    else:
        print arg, 'tiene', len(f.readlines()), 'lineas'
        f.close()
