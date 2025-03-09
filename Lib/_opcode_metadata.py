# This file is generated by Tools/cases_generator/py_metadata_generator.py
# from:
#   Python/bytecodes.c
# Do not edit!
_specializations = {
    "RESUME": [
        "RESUME_CHECK",
    ],
    "LOAD_CONST": [
        "LOAD_CONST_MORTAL",
        "LOAD_CONST_IMMORTAL",
    ],
    "TO_BOOL": [
        "TO_BOOL_ALWAYS_TRUE",
        "TO_BOOL_BOOL",
        "TO_BOOL_INT",
        "TO_BOOL_LIST",
        "TO_BOOL_NONE",
        "TO_BOOL_STR",
    ],
    "BINARY_OP": [
        "BINARY_OP_MULTIPLY_INT",
        "BINARY_OP_ADD_INT",
        "BINARY_OP_SUBTRACT_INT",
        "BINARY_OP_MULTIPLY_FLOAT",
        "BINARY_OP_ADD_FLOAT",
        "BINARY_OP_SUBTRACT_FLOAT",
        "BINARY_OP_ADD_UNICODE",
        "BINARY_OP_SUBSCR_LIST_INT",
        "BINARY_OP_SUBSCR_TUPLE_INT",
        "BINARY_OP_SUBSCR_STR_INT",
        "BINARY_OP_SUBSCR_DICT",
        "BINARY_OP_SUBSCR_GETITEM",
        "BINARY_OP_EXTEND",
        "BINARY_OP_INPLACE_ADD_UNICODE",
    ],
    "STORE_SUBSCR": [
        "STORE_SUBSCR_DICT",
        "STORE_SUBSCR_LIST_INT",
    ],
    "SEND": [
        "SEND_GEN",
    ],
    "UNPACK_SEQUENCE": [
        "UNPACK_SEQUENCE_TWO_TUPLE",
        "UNPACK_SEQUENCE_TUPLE",
        "UNPACK_SEQUENCE_LIST",
    ],
    "STORE_ATTR": [
        "STORE_ATTR_INSTANCE_VALUE",
        "STORE_ATTR_SLOT",
        "STORE_ATTR_WITH_HINT",
    ],
    "LOAD_GLOBAL": [
        "LOAD_GLOBAL_MODULE",
        "LOAD_GLOBAL_BUILTIN",
    ],
    "LOAD_SUPER_ATTR": [
        "LOAD_SUPER_ATTR_ATTR",
        "LOAD_SUPER_ATTR_METHOD",
    ],
    "LOAD_ATTR": [
        "LOAD_ATTR_INSTANCE_VALUE",
        "LOAD_ATTR_MODULE",
        "LOAD_ATTR_WITH_HINT",
        "LOAD_ATTR_SLOT",
        "LOAD_ATTR_CLASS",
        "LOAD_ATTR_CLASS_WITH_METACLASS_CHECK",
        "LOAD_ATTR_PROPERTY",
        "LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN",
        "LOAD_ATTR_METHOD_WITH_VALUES",
        "LOAD_ATTR_METHOD_NO_DICT",
        "LOAD_ATTR_METHOD_LAZY_DICT",
        "LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES",
        "LOAD_ATTR_NONDESCRIPTOR_NO_DICT",
    ],
    "COMPARE_OP": [
        "COMPARE_OP_FLOAT",
        "COMPARE_OP_INT",
        "COMPARE_OP_STR",
    ],
    "CONTAINS_OP": [
        "CONTAINS_OP_SET",
        "CONTAINS_OP_DICT",
    ],
    "JUMP_BACKWARD": [
        "JUMP_BACKWARD_NO_JIT",
        "JUMP_BACKWARD_JIT",
    ],
    "FOR_ITER": [
        "FOR_ITER_LIST",
        "FOR_ITER_TUPLE",
        "FOR_ITER_RANGE",
        "FOR_ITER_GEN",
    ],
    "CALL": [
        "CALL_BOUND_METHOD_EXACT_ARGS",
        "CALL_PY_EXACT_ARGS",
        "CALL_TYPE_1",
        "CALL_STR_1",
        "CALL_TUPLE_1",
        "CALL_BUILTIN_CLASS",
        "CALL_BUILTIN_O",
        "CALL_BUILTIN_FAST",
        "CALL_BUILTIN_FAST_WITH_KEYWORDS",
        "CALL_LEN",
        "CALL_ISINSTANCE",
        "CALL_LIST_APPEND",
        "CALL_METHOD_DESCRIPTOR_O",
        "CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS",
        "CALL_METHOD_DESCRIPTOR_NOARGS",
        "CALL_METHOD_DESCRIPTOR_FAST",
        "CALL_ALLOC_AND_ENTER_INIT",
        "CALL_PY_GENERAL",
        "CALL_BOUND_METHOD_GENERAL",
        "CALL_NON_PY_GENERAL",
    ],
    "CALL_KW": [
        "CALL_KW_BOUND_METHOD",
        "CALL_KW_PY",
        "CALL_KW_NON_PY",
    ],
}

_specialized_opmap = {
    'BINARY_OP_ADD_FLOAT': 129,
    'BINARY_OP_ADD_INT': 130,
    'BINARY_OP_ADD_UNICODE': 131,
    'BINARY_OP_EXTEND': 132,
    'BINARY_OP_INPLACE_ADD_UNICODE': 3,
    'BINARY_OP_MULTIPLY_FLOAT': 133,
    'BINARY_OP_MULTIPLY_INT': 134,
    'BINARY_OP_SUBSCR_DICT': 135,
    'BINARY_OP_SUBSCR_GETITEM': 136,
    'BINARY_OP_SUBSCR_LIST_INT': 137,
    'BINARY_OP_SUBSCR_STR_INT': 138,
    'BINARY_OP_SUBSCR_TUPLE_INT': 139,
    'BINARY_OP_SUBTRACT_FLOAT': 140,
    'BINARY_OP_SUBTRACT_INT': 141,
    'CALL_ALLOC_AND_ENTER_INIT': 142,
    'CALL_BOUND_METHOD_EXACT_ARGS': 143,
    'CALL_BOUND_METHOD_GENERAL': 144,
    'CALL_BUILTIN_CLASS': 145,
    'CALL_BUILTIN_FAST': 146,
    'CALL_BUILTIN_FAST_WITH_KEYWORDS': 147,
    'CALL_BUILTIN_O': 148,
    'CALL_ISINSTANCE': 149,
    'CALL_KW_BOUND_METHOD': 150,
    'CALL_KW_NON_PY': 151,
    'CALL_KW_PY': 152,
    'CALL_LEN': 153,
    'CALL_LIST_APPEND': 154,
    'CALL_METHOD_DESCRIPTOR_FAST': 155,
    'CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS': 156,
    'CALL_METHOD_DESCRIPTOR_NOARGS': 157,
    'CALL_METHOD_DESCRIPTOR_O': 158,
    'CALL_NON_PY_GENERAL': 159,
    'CALL_PY_EXACT_ARGS': 160,
    'CALL_PY_GENERAL': 161,
    'CALL_STR_1': 162,
    'CALL_TUPLE_1': 163,
    'CALL_TYPE_1': 164,
    'COMPARE_OP_FLOAT': 165,
    'COMPARE_OP_INT': 166,
    'COMPARE_OP_STR': 167,
    'CONTAINS_OP_DICT': 168,
    'CONTAINS_OP_SET': 169,
    'FOR_ITER_GEN': 170,
    'FOR_ITER_LIST': 171,
    'FOR_ITER_RANGE': 172,
    'FOR_ITER_TUPLE': 173,
    'JUMP_BACKWARD_JIT': 174,
    'JUMP_BACKWARD_NO_JIT': 175,
    'LOAD_ATTR_CLASS': 176,
    'LOAD_ATTR_CLASS_WITH_METACLASS_CHECK': 177,
    'LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN': 178,
    'LOAD_ATTR_INSTANCE_VALUE': 179,
    'LOAD_ATTR_METHOD_LAZY_DICT': 180,
    'LOAD_ATTR_METHOD_NO_DICT': 181,
    'LOAD_ATTR_METHOD_WITH_VALUES': 182,
    'LOAD_ATTR_MODULE': 183,
    'LOAD_ATTR_NONDESCRIPTOR_NO_DICT': 184,
    'LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES': 185,
    'LOAD_ATTR_PROPERTY': 186,
    'LOAD_ATTR_SLOT': 187,
    'LOAD_ATTR_WITH_HINT': 188,
    'LOAD_CONST_IMMORTAL': 189,
    'LOAD_CONST_MORTAL': 190,
    'LOAD_GLOBAL_BUILTIN': 191,
    'LOAD_GLOBAL_MODULE': 192,
    'LOAD_SUPER_ATTR_ATTR': 193,
    'LOAD_SUPER_ATTR_METHOD': 194,
    'RESUME_CHECK': 195,
    'SEND_GEN': 196,
    'STORE_ATTR_INSTANCE_VALUE': 197,
    'STORE_ATTR_SLOT': 198,
    'STORE_ATTR_WITH_HINT': 199,
    'STORE_SUBSCR_DICT': 200,
    'STORE_SUBSCR_LIST_INT': 201,
    'TO_BOOL_ALWAYS_TRUE': 202,
    'TO_BOOL_BOOL': 203,
    'TO_BOOL_INT': 204,
    'TO_BOOL_LIST': 205,
    'TO_BOOL_NONE': 206,
    'TO_BOOL_STR': 207,
    'UNPACK_SEQUENCE_LIST': 208,
    'UNPACK_SEQUENCE_TUPLE': 209,
    'UNPACK_SEQUENCE_TWO_TUPLE': 210,
}

opmap = {
    'CACHE': 0,
    'RESERVED': 17,
    'RESUME': 128,
    'INSTRUMENTED_LINE': 254,
    'ENTER_EXECUTOR': 255,
    'BINARY_SLICE': 1,
    'CALL_FUNCTION_EX': 2,
    'CHECK_EG_MATCH': 4,
    'CHECK_EXC_MATCH': 5,
    'CLEANUP_THROW': 6,
    'DELETE_SUBSCR': 7,
    'END_FOR': 8,
    'END_SEND': 9,
    'EXIT_INIT_CHECK': 10,
    'FORMAT_SIMPLE': 11,
    'FORMAT_WITH_SPEC': 12,
    'GET_AITER': 13,
    'GET_ANEXT': 14,
    'GET_ITER': 15,
    'GET_LEN': 16,
    'GET_YIELD_FROM_ITER': 18,
    'INTERPRETER_EXIT': 19,
    'LOAD_BUILD_CLASS': 20,
    'LOAD_LOCALS': 21,
    'MAKE_FUNCTION': 22,
    'MATCH_KEYS': 23,
    'MATCH_MAPPING': 24,
    'MATCH_SEQUENCE': 25,
    'NOP': 26,
    'NOT_TAKEN': 27,
    'POP_EXCEPT': 28,
    'POP_ITER': 29,
    'POP_TOP': 30,
    'PUSH_EXC_INFO': 31,
    'PUSH_NULL': 32,
    'RETURN_GENERATOR': 33,
    'RETURN_VALUE': 34,
    'SETUP_ANNOTATIONS': 35,
    'STORE_SLICE': 36,
    'STORE_SUBSCR': 37,
    'TO_BOOL': 38,
    'UNARY_INVERT': 39,
    'UNARY_NEGATIVE': 40,
    'UNARY_NOT': 41,
    'WITH_EXCEPT_START': 42,
    'BINARY_OP': 43,
    'BUILD_LIST': 44,
    'BUILD_MAP': 45,
    'BUILD_SET': 46,
    'BUILD_SLICE': 47,
    'BUILD_STRING': 48,
    'BUILD_TUPLE': 49,
    'CALL': 50,
    'CALL_INTRINSIC_1': 51,
    'CALL_INTRINSIC_2': 52,
    'CALL_KW': 53,
    'COMPARE_OP': 54,
    'CONTAINS_OP': 55,
    'CONVERT_VALUE': 56,
    'COPY': 57,
    'COPY_FREE_VARS': 58,
    'DELETE_ATTR': 59,
    'DELETE_DEREF': 60,
    'DELETE_FAST': 61,
    'DELETE_GLOBAL': 62,
    'DELETE_NAME': 63,
    'DICT_MERGE': 64,
    'DICT_UPDATE': 65,
    'END_ASYNC_FOR': 66,
    'EXTENDED_ARG': 67,
    'FOR_ITER': 68,
    'GET_AWAITABLE': 69,
    'IMPORT_FROM': 70,
    'IMPORT_NAME': 71,
    'IS_OP': 72,
    'JUMP_BACKWARD': 73,
    'JUMP_BACKWARD_NO_INTERRUPT': 74,
    'JUMP_FORWARD': 75,
    'LIST_APPEND': 76,
    'LIST_EXTEND': 77,
    'LOAD_ATTR': 78,
    'LOAD_COMMON_CONSTANT': 79,
    'LOAD_CONST': 80,
    'LOAD_DEREF': 81,
    'LOAD_FAST': 82,
    'LOAD_FAST_AND_CLEAR': 83,
    'LOAD_FAST_CHECK': 84,
    'LOAD_FAST_LOAD_FAST': 85,
    'LOAD_FROM_DICT_OR_DEREF': 86,
    'LOAD_FROM_DICT_OR_GLOBALS': 87,
    'LOAD_GLOBAL': 88,
    'LOAD_NAME': 89,
    'LOAD_SMALL_INT': 90,
    'LOAD_SPECIAL': 91,
    'LOAD_SUPER_ATTR': 92,
    'MAKE_CELL': 93,
    'MAP_ADD': 94,
    'MATCH_CLASS': 95,
    'POP_JUMP_IF_FALSE': 96,
    'POP_JUMP_IF_NONE': 97,
    'POP_JUMP_IF_NOT_NONE': 98,
    'POP_JUMP_IF_TRUE': 99,
    'RAISE_VARARGS': 100,
    'RERAISE': 101,
    'SEND': 102,
    'SET_ADD': 103,
    'SET_FUNCTION_ATTRIBUTE': 104,
    'SET_UPDATE': 105,
    'STORE_ATTR': 106,
    'STORE_DEREF': 107,
    'STORE_FAST': 108,
    'STORE_FAST_LOAD_FAST': 109,
    'STORE_FAST_STORE_FAST': 110,
    'STORE_GLOBAL': 111,
    'STORE_NAME': 112,
    'SWAP': 113,
    'UNPACK_EX': 114,
    'UNPACK_SEQUENCE': 115,
    'YIELD_VALUE': 116,
    'INSTRUMENTED_END_FOR': 234,
    'INSTRUMENTED_POP_ITER': 235,
    'INSTRUMENTED_END_SEND': 236,
    'INSTRUMENTED_FOR_ITER': 237,
    'INSTRUMENTED_INSTRUCTION': 238,
    'INSTRUMENTED_JUMP_FORWARD': 239,
    'INSTRUMENTED_NOT_TAKEN': 240,
    'INSTRUMENTED_POP_JUMP_IF_TRUE': 241,
    'INSTRUMENTED_POP_JUMP_IF_FALSE': 242,
    'INSTRUMENTED_POP_JUMP_IF_NONE': 243,
    'INSTRUMENTED_POP_JUMP_IF_NOT_NONE': 244,
    'INSTRUMENTED_RESUME': 245,
    'INSTRUMENTED_RETURN_VALUE': 246,
    'INSTRUMENTED_YIELD_VALUE': 247,
    'INSTRUMENTED_END_ASYNC_FOR': 248,
    'INSTRUMENTED_LOAD_SUPER_ATTR': 249,
    'INSTRUMENTED_CALL': 250,
    'INSTRUMENTED_CALL_KW': 251,
    'INSTRUMENTED_CALL_FUNCTION_EX': 252,
    'INSTRUMENTED_JUMP_BACKWARD': 253,
    'JUMP': 256,
    'JUMP_IF_FALSE': 257,
    'JUMP_IF_TRUE': 258,
    'JUMP_NO_INTERRUPT': 259,
    'LOAD_CLOSURE': 260,
    'POP_BLOCK': 261,
    'SETUP_CLEANUP': 262,
    'SETUP_FINALLY': 263,
    'SETUP_WITH': 264,
    'STORE_FAST_MAYBE_NULL': 265,
}

HAVE_ARGUMENT = 42
MIN_INSTRUMENTED_OPCODE = 234
