#!/bin/sh

# if [ ! -e build/.conan/conan_toolchain.cmake ];then
#   conan install . -of=build/.conan -s build_type=Debug -s compiler.cppstd=17 --build=missing
# fi

conan install . -of=build/.conan -s build_type=Debug -s compiler.cppstd=17 --build=missing -g VirtualRunEnv -c tools.env:dotenv=True
cmake -B build -S . -DCMAKE_TOOLCHAIN_FILE="build/.conan/conan_toolchain.cmake" -DCMAKE_BUILD_TYPE=Debug
cmake --build build -j
