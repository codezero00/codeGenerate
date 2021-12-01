def str2Hump(text):
    """
    下划线转小驼峰 blood_detail -》 bloodDetail
    """
    arr = filter(None, text.lower().split('_'))
    res = ''
    j = 0
    for i in arr:
        if j == 0:
            res = i
        else:
            res = res + i[0].upper() + i[1:]
        j += 1
    return res


def str2BigHump(text):
    """
    下划线转大驼峰 blood_detail -》 BloodDetail
    """
    arr = filter(None, text.lower().split('_'))
    res = ''
    j = 0
    for i in arr:
        # print(1)
        # print(res)
        if j == 0:
            res = i[0].upper() + i[1:]
        else:
            res = res + i[0].upper() + i[1:]
        j += 1
    return res


def openapiType2pydanticType(text):
    """
    string -> str
    integer -> int
    boolean -> bool
    array   -> List
    object  -> Dict
    number  -> int
    any     -> Any

    :param text:
    :return:
    """
    type_map = {"string" : "str",
                "integer": "int",
                "boolean": "bool",
                "array"  : "List[Any]",
                "object" : "Dict[Any]",
                "number" : "int",
                "any"    : "Any"
                }
    return type_map[text]