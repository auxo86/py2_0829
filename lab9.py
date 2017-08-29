def sample_variable_arguments(fix1, fix2, **kargs):
    print "fix part:", fix1, fix2
    print [key + '/' + str(kargs[key]) for key in kargs]


sample_variable_arguments('Hello World', True,
                          name='Mark', age=42, weight=72.5)
dict1 = {'name': 'Mark', 'age': 42, 'weight': 72.5}
sample_variable_arguments('Hello World', True, **dict1)
