
def qs_validator(qs, **kwargs):
    qs_type = kwargs['type']
    try:
        return qs_type(qs)
    except:
        raise Exception('{0} is not type {1}'.format(qs, str(qs_type)))


def qs_validate(qs,name='not provided', required=False, **kwargs):
    '''
    facade for validate if qs is the proper type
    :param qs:
    :param kwargs:
    :return:
    '''
    if not qs and not required:
        return qs
    if required and not qs:
        raise Exception('{0} is required and not provided'.format(name))

    try:
        qs_type = kwargs['type']
    except:
        raise Exception('Type to validate is missing! try : qs_validator(value, type=int)')

    if not isinstance(qs_type,type):
        raise Exception('{0} is not a valid python type (int, float, ..)'.format(qs_type))

    # handles is qs is list and its not empty
    if isinstance(qs,list):
        # if not qs:
        #     return qs_validator(None, type=qs_type)
        return [qs_validator(item, type=qs_type) for item in qs]

    return qs_validator(qs, type=qs_type)


def assign_method(method_name, id):
    '''
    assign property http_method to function if valid
    :type method_name: function
    :return: function
    '''
    def wrapper(func):
        if method_name.lower() not in DEFAULT_ROUTES:
            raise Exception('{0} not valid http method in method {1}'.format(method_name,func.__name__))
        func.http_method = method_name
        return func
    return wrapper


str_escape = lambda x: """$${}$$::text""".format(x)

