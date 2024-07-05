cmake_minimum_required(VERSION 3.15)
project(my_cpp_project VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(my_cpp_project src/main.cpp)
target_link_libraries(my_cpp_project ${CONAN_LIBS})

# TODO: uncomment the following lines to enable testing
#enable_testing()
#add_executable(test_main tests/test_main.cpp)
#target_link_libraries(test_main ${CONAN_LIBS})
#add_test(NAME test_main COMMAND test_main)
