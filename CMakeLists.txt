cmake_minimum_required(VERSION 3.12)
project(
  NVR
  VERSION 1.0.0
  LANGUAGES CXX)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

include(GitVersion)

# Set C++17 standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(spdlog REQUIRED)
find_package(yaml-cpp REQUIRED)
find_package(argparse REQUIRED)
find_package(httplib REQUIRED)
find_package(nlohmann_json REQUIRED)

add_subdirectory(src)

# Add packaging subdirectory (only when building from source root)
#if(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_CURRENT_SOURCE_DIR})
#  add_subdirectory(cmake.packaging)
#endif()
