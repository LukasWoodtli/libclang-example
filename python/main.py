from typing import Optional

import clang
from clang.cindex import Cursor, CursorKind, TranslationUnit

clang.cindex.Config.set_library_file('/Library/Developer/CommandLineTools/usr/lib/libclang.dylib')


def find_child(parent: Cursor, kind: CursorKind, spelling: str) -> Optional[Cursor]:
    for node in parent.get_children():
        if kind == node.kind and spelling == node.spelling:
            return node


def get_hello_function(translation_unit: TranslationUnit) -> Cursor:
    return find_child(translation_unit.cursor, CursorKind.FUNCTION_DECL, 'hello')


def dump(cursor: Cursor):
    for t in cursor.get_tokens():
        print(t.spelling)


def get_translation_unit(compilation_database_dir: str, cpp_path: str) -> TranslationUnit:
    compilation_database = clang.cindex.CompilationDatabase.fromDirectory(compilation_database_dir)
    compilation_commands = compilation_database.getCompileCommands(cpp_path)
    index = clang.cindex.Index.create()
    translation_unit = index.parse(cpp_path) #, args=compilation_commands)
    return translation_unit


if __name__ == "__main__":
    compilation_commands_file = "/Users/lukaswoodtli/Development/libclang_example/cpp/cmake-build-debug/"
    tu = get_translation_unit(compilation_commands_file, "/Users/lukaswoodtli/Development/libclang_example/cpp/library.cpp")
    hello_fn = get_hello_function(tu)
    dump(hello_fn)
