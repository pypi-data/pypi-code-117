# NEO4J CONFIG


# AST_TMP

TYPE_TMP_ROOT = "AST_TMP_ROOT"
TYPE_TMP_STMT = "AST_TMP_STMT"
TYPE_TMP_EXPRESSION = "AST_TMP_EXPRESSION_STMT"
TYPE_TMP_CONSTRAIN = "AST_TMP_CONSTRAIN_STMT"

# SOME FLAGS

EXTRACT_ALL_PARAM_FLAG = hex(0xffcbead)
SPECIAL_IDENTITY = 'special'

# BACKEND CODE

TAC_SRC_ENGINE = "TAC"
FILE_SRC_ENGINE = "FILE"

# Label Code

LABEL_ARTIFICIAL = "Artificial"
LABEL_AST = "AST"
LABEL_FILESYSTEM = "Filesystem"
LABEL_AST_TMP = "AST_TMP"

# Artificial node keys
ARTIFICIAL_INDEX = 'id'
ARTIFICIAL_TYPE = 'type'
ARTIFICIAL_NAME = 'name'
ARTIFICIAL_CLASSNAME = 'classname'

# Artificial node types
TYPE_CFG_FUNC_EXIT = "CFG_FUNC_EXIT"
TYPE_CFG_FUNC_ENTRY = "CFG_FUNC_ENTRY"

# AST node property keys

NODE_INDEX = 'id'
NODE_TYPE = 'type'
NODE_FLAGS = 'flags'
NODE_LINENO = 'lineno'
NODE_CODE = 'code'
NODE_FUNCID = 'funcid'
NODE_ENDLINENO = 'endlineno'
NODE_NAME = 'name'
NODE_DOCCOMMENT = 'doccomment'
NODE_FILEID = 'fileid'
NODE_CHILDNUM = 'childnum'
NODE_CLASSID = 'classid'
NODE_IS_SINK_TRACE = "is_sink_trace"
NODE_TRACE_ID = "trace_id"
NODE_TMP_ROOT_IDENTIFIER = "tmp_root_identity"

# AST node types
TYPE_USE = "AST_USE"  # use Yii/index
TYPE_NAMESPACE = "AST_NAMESPACE"  # namespace shaobaobaoer
TYPE_CONDITIONAL = 'AST_CONDITIONAL'
TYPE_TOPLEVEL = "AST_TOPLEVEL"
TYPE_STMT_LIST = 'AST_STMT_LIST'  # ...; ...; ...;
TYPE_CALL = 'AST_CALL'  # foo()
TYPE_NEW = 'AST_NEW'  # new shaobao()
TYPE_STATIC_CALL = 'AST_STATIC_CALL'  # bla::foo()
TYPE_METHOD_CALL = 'AST_METHOD_CALL'  # $bla->foo()
TYPE_PROP = 'AST_PROP'  # e.g., $bla->foo
TYPE_INSTANCEOF = 'AST_INSTANCEOF'  # e.g. , $a instance of b
TYPE_STATIC_PROP = 'AST_STATIC_PROP'  # e,g, shaobao::$cai
TYPE_FUNC_DECL = 'AST_FUNC_DECL'  # function foo() {}
TYPE_METHOD = 'AST_METHOD'  # class bla { ... function foo() {} ... }
TYPE_CLASS = "AST_CLASS"  # class defination node
TYPE_ARG_LIST = 'AST_ARG_LIST'  # foo( $a1, $a2, $a3)
TYPE_PARAM_LIST = 'AST_PARAM_LIST'  # function foo( $p1, $p2, $p3) {}
TYPE_UNPACK = 'AST_UNPACK'  # ...$array1
TYPE_ATTRIBUTE = 'AST_ATTRIBUTE'
TYPE_MATCH = 'AST_MATCH'
TYPE_NAMED_ARG = 'AST_NAMED_ARG'
TYPE_UNION = 'AST_TYPE_UNION'
TYPE_NULLABLE = 'AST_NULLABLE_TYPE'
TYPE_ARRAY = 'AST_ARRAY'
TYPE_ARRAY_ELEM = 'AST_ARRAY_ELEM'
TYPE_LIST = 'AST_LIST'
TYPE_PARAM = 'AST_PARAM'  # $p1
TYPE_TYPE = 'AST_TYPE'
TYPE_ASSIGN = 'AST_ASSIGN'  # $buzz = true
TYPE_THROW = 'AST_THROW'
TYPE_STATIC = 'AST_STATIC'
TYPE_ASSIGN_REF = 'AST_ASSIGN_REF'  # $b = &$a
TYPE_ASSIGN_OP = 'AST_ASSIGN_OP'  # $x += 3
TYPE_NAME = 'AST_NAME'  # names (e.g., name of a called function in call expressions)
TYPE_VAR = 'AST_VAR'  # $v
TYPE_MAGIC_CONST = "AST_MAGIC_CONST"  # __FILE__
TYPE_CONST = 'AST_CONST'  # SHAOBAO
TYPE_GLOBAL = 'AST_GLOBAL'
TYPE_CLASS_CONST = 'AST_CLASS_CONST'  # SBBR::SHAOBAO
TYPE_CLASS_CONST_GROUP = 'AST_CLASS_CONST_GROUP'
TYPE_BINARY_OP = 'AST_BINARY_OP'  # e.g., "foo"."bar" or 3+4
TYPE_UNARY_OP = 'AST_UNARY_OP'  # e.g. !$a   ,  ! $a
TYPE_CAST = 'AST_CAST'  # int(i)
TYPE_POST_INC, TYPE_POST_DEC, TYPE_PRE_INC, TYPE_PRE_DEC = 'AST_POST_INC', 'AST_POST_DEC', 'AST_PRE_INC', 'AST_PRE_DEC'
TYPE_ENCAPS_LIST = 'AST_ENCAPS_LIST'  # e.g., "blah{$var1}buzz $var2 beep"
TYPE_NULL = "NULL"
TYPE_MIXED = 'TYPE_MIXED'
TYPE_NULLSAFE_PROP = 'AST_NULLSAFE_PROP'
TYPE_REF = "AST_REF"  # e.g. &$a
TYPE_PROP_ELEM = 'AST_PROP_ELEM'
TYPE_ARRAY_FUNCTION = 'AST_ARROW_FUNC'
# Abeer
CLASS_TRAIT = 'CLASS_TRAIT'
TYPE_EXPR_LIST = "AST_EXPR_LIST"
TYPE_ITERABLE = 'TYPE_ITERABLE'
TYPE_CALLEE = 'Callee'
TYPE_FUNCTION = 'Function'
TYPE_ECHO = 'AST_ECHO'  # eecho
TYPE_PRINT = 'AST_PRINT'  # PRINT
TYPE_EMPTY = 'AST_EMPTY'
TYPE_INCLUDE_OR_EVAL = 'AST_INCLUDE_OR_EVAL'  # eval, include, require
TYPE_ISSET = 'AST_ISSET'  #
TYPE_UNSET = 'AST_UNSET'
TYPE_RETURN = 'AST_RETURN'  # return
TYPE_EXIT = "AST_EXIT"
TYPE_VOID = 'TYPE_VOID'
# ABEER
TYPE_IF = 'AST_IF'
TYPE_IF_ELEM = 'AST_IF_ELEM'  # HOLDES THE COND INSIDE IF
TYPE_FOR = 'AST_FOR'
TYPE_FOREACH = "AST_FOREACH"
TYPE_BREAK = "AST_BREAK"
TYPE_CONTINUE = "AST_CONTINUE"
TYPE_WHILE = "AST_WHILE"
TYPE_DO_WHILE = "AST_DO_WHILE"
TYPE_SWITCH = 'AST_SWITCH'
TYPE_SWITCH_CASE = 'AST_SWITCH_CASE'
TMP_PARAM_FOR_SWITCH = 'TMP_PARAM_0x131FF'  #
TYPE_TRY = "AST_TRY"
TYPE_CATCH = "AST_CATCH"
TYPE_CLOSURE = "AST_CLOSURE"
TYPE_DIM = 'AST_DIM'  # _POST[x]
TYPE_USE_TRAIT = 'AST_USE_TRAIT'

# AST node flags
# of AST_ASSIGN.*
FLAG_ASSIGN_CONCAT = 'ASSIGN_CONCAT'  # $v .= "foo"
FLAG_BINARY_SHIFT_LEFT, FLAG_BINARY_SHIFT_RIGHT = "BINARY_SHIFT_LEFT", "BINARY_SHIFT_RIGHT"  # >> <<
FLAG_BINARY_BITWISE_AND, FLAG_BINARY_BITWISE_OR, FLAG_BINARY_BITWISE_XOR, = \
    "BINARY_BITWISE_AND", "BINARY_BITWISE_OR", "BINARY_BITWISE_XOR",  # & , | , ^
# of AST_BINARY_OP
FLAG_BINARY_CONCAT = 'BINARY_CONCAT'  # "foo"."bar"
FLAG_BINARY_ADD, FLAG_BINARY_SUB, FLAG_BINARY_MUL, FLAG_BINARY_DIV, FLAG_BINARY_MOD, FLAG_BINARY_POW = \
    "BINARY_ADD", "BINARY_SUB", "BINARY_MUL", "BINARY_DIV", "BINARY_MOD", "BINARY_POW"
FLAG_BINARY_BOOL_AND, FLAG_BINARY_BOOL_OR, FLAG_BINARY_BOOL_XOR = \
    'BINARY_BOOL_AND', 'BINARY_BOOL_OR', 'BINARY_BOOL_XOR'  # && , || , xor
FLAG_TMP_CONSTRAIN_BINARY_BOOL_AND = "TMP_CONSTRAIN_BINARY_BOOL_AND"  # && -> LATEX_LAND
FLAG_BINARY_IS_SMALLER, FLAG_BINARY_IS_SMALLER_OR_EQUAL, FLAG_BINARY_IS_GREATER, FLAG_BINARY_IS_GREATER_OR_EQUAL = \
    'BINARY_IS_SMALLER', 'BINARY_IS_SMALLER_OR_EQUAL', 'BINARY_IS_GREATER', 'BINARY_IS_GREATER_OR_EQUAL'
FLAG_BINARY_EQUAL = 'BINARY_IS_EQUAL'  # x==y
FLAG_BINARY_NOT_EQUAL = 'BINARY_IS_NOT_EQUAL'  # !=
FLAG_BINARY_IS_IDENTICAL = 'BINARY_IS_IDENTICAL'  # ===
FLAG_BINARY_IS_NOT_IDENTICAL = 'BINARY_IS_NOT_IDENTICAL'  # !===
FLAG_UNARY_MINUS = 'UNARY_MINUS'  #
FLAG_UNARY_SILENCE = 'UNARY_SILENCE'  #
# FLAG of AST_INCLUDE_OR_EVAL
FLAG_EXEC_EVAL = 'EXEC_EVAL'  # eval("...")
FLAG_EXEC_INCLUDE = 'EXEC_INCLUDE'  # include "..."
FLAG_EXEC_INCLUDE_ONCE = 'EXEC_INCLUDE_ONCE'  # include_once "..."
FLAG_EXEC_REQUIRE = 'EXEC_REQUIRE'  # require "..."
FLAG_EXEC_REQUIRE_ONCE = 'EXEC_REQUIRE_ONCE'  # require_once "..."
# FLAG of AST_CAST (int)$a (array)$a
FLAG_TYPE_LONG, FLAG_TYPE_DOUBLE, FLAG_TYPE_STRING, FLAG_TYPE_BOOL, FLAG_TYPE_ARRAY, FLAG_TYPE_OBJECT = \
    "TYPE_LONG", "TYPE_DOUBLE", "TYPE_STRING", "TYPE_BOOL", "TYPE_ARRAY", "TYPE_OBJECT"
# FLAG of MAGIC CONST
FLAG_MAGIC_LINE, FLAG_MAGIC_FILE, FLAG_MAGIC_DIR, FLAG_MAGIC_NAMESPACE, \
FLAG_MAGIC_FUNCTION, FLAG_MAGIC_METHOD, FLAG_MAGIC_CLASS, FLAG_MAGIC_TRAIT = \
    "MAGIC_LINE", "MAGIC_FILE", "MAGIC_DIR", "MAGIC_NAMESPACE", \
    "MAGIC_FUNCTION", "MAGIC_METHOD", "MAGIC_CLASS", "MAGIC_TRAIT"
MAGIC_CONST_CONVERT_DICT = {
    FLAG_MAGIC_LINE: "__LINE__", FLAG_MAGIC_FILE: "__FILE__", FLAG_MAGIC_DIR: "__DIR__",
    FLAG_MAGIC_NAMESPACE: "__NAMESPACE__",
    FLAG_MAGIC_FUNCTION: "__FUNCTION__", FLAG_MAGIC_METHOD: "__METHOD__", FLAG_MAGIC_CLASS: "__CLASS__",
    FLAG_MAGIC_TRAIT: "__TRAIT__"
}
# Other (non-AST) node types
FLAG_TOPLEVEL_FILE = "TOPLEVEL_FILE"

TYPE_DIRECTORY = 'Directory'
TYPE_FILE = 'File'

TYPE_STRING = 'string'
TYPE_DOUBLE = 'double'
TYPE_INTEGER = 'integer'
TYPE_BOOL = 'bool'

# Edge types

DIRECTORY_EDGE = 'DIRECTORY_OF'
FILE_EDGE = 'FILE_OF'
AST_EDGE = 'PARENT_OF'

TYPE_IDENTIFIER_DECL_STMT = 'IdentifierDeclStatement'
TYPE_PARAMETER = 'Parameter'
CALLS_EDGE = 'CALLS'
CFG_EDGE = 'FLOWS_TO'
CFG_EDGE_FLOW_LABEL = 'flowLabel'
DATA_FLOW_EDGE = 'REACHES'
IMPLEMENT_EDGE = 'IMPLEMENTS'
EXTENDS_EDGE = 'EXTENDS'
TRAIT_EDGE = 'TRAIT'
INCLUDE_EDGE = 'INCLUDE'
# extends、implements、trait
FUNCTION_TO_AST_EDGE = 'IS_FUNCTION_OF_AST'
FILE_TO_FUNCTION_EDGE = 'IS_FILE_OF'
MODIFIER_PROTECTED = 'MODIFIER_PROTECTED'
ARRAY_SYNTAX_SHORT = 'ARRAY_SYNTAX_SHORT'
ARRAY_SYNTAX_LIST = 'ARRAY_SYNTAX_LIST'
BINARY_COALESCE = 'BINARY_COALESCE'
# Edge keys

DATA_FLOW_SYMBOL = 'var'

# Abeer
DATA_FLOW_TAINT_SRC = 'taint_src'
DATA_FLOW_TAINT_DST = 'taint_dst'

# EXEC TYPES
SYMBOLIC_EXECUTABLE_TYPES = {
    TYPE_CALL, TYPE_BINARY_OP, TYPE_UNARY_OP
}

HAS_STMT_LIST_TYPES = {
    TYPE_TOPLEVEL, TYPE_IF_ELEM, TYPE_FOREACH, TYPE_FUNC_DECL,
    TYPE_TRY, TYPE_CATCH, TYPE_CLOSURE, TYPE_SWITCH_CASE,
    TYPE_METHOD, TYPE_FOR, TYPE_WHILE, TYPE_DO_WHILE,
}

CHILD_HAS_STMT_LIST_TYPES = {
    TYPE_IF, TYPE_SWITCH
}

DIRECT_CALL_TYPES = {TYPE_INCLUDE_OR_EVAL, TYPE_ECHO, TYPE_PRINT, TYPE_EXIT, TYPE_RETURN, TYPE_EMPTY, TYPE_UNSET}

VAR_TYPES = {TYPE_DIM, TYPE_VAR, TYPE_CLASS_CONST, TYPE_CONST, TYPE_PROP, TYPE_STATIC_PROP}
VAR_TYPES_EXCLUDE_CONST_VAR = {TYPE_DIM, TYPE_VAR, TYPE_PROP, TYPE_STATIC_PROP}

# 函数调用集合
SET_FUNCTION_CALL = {
    TYPE_METHOD_CALL, TYPE_CALL, TYPE_STATIC_CALL, TYPE_NEW
}

FUNCTION_DECLARE_TYPES = {
    TYPE_METHOD, TYPE_FUNC_DECL,
}

FUNCTION_CALL_TYPES = SET_FUNCTION_CALL

SET_NO_TUPLE_FUNCTION = {
    TYPE_ECHO, TYPE_INCLUDE_OR_EVAL
}

ONLY_ROOT_NODE_CODE_EXTRACTION_SET = {TYPE_VAR, TYPE_CLASS_CONST,
                                      TYPE_CONST,
                                      TYPE_PROP,
                                      TYPE_STATIC_PROP}

AST_ROOT = {TYPE_ASSIGN, TYPE_ASSIGN_OP, TYPE_ASSIGN_REF, TYPE_CALL, }
