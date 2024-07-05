cmake_minimum_required(VERSION 3.15)
project(cpp-app VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Check if the toolchain file exists and include it
if(EXISTS "${CMAKE_BINARY_DIR}/Release/generators/conan_toolchain.cmake")
    include("${CMAKE_BINARY_DIR}/Release/generators/conan_toolchain.cmake")
else()
    message(FATAL_ERROR "Could not find conan_toolchain.cmake")
endif()

find_package(Boost REQUIRED)
find_package(spdlog REQUIRED)
find_package(GTest REQUIRED)

add_executable(cpp-app src/main.cpp)
target_link_libraries(cpp-app Boost::headers spdlog::spdlog)

# TODO: Uncomment the following lines to enable testing
#enable_testing()
#add_executable(test_main tests/test_main.cpp)
#target_link_libraries(test_main GTest::gtest GTest::gtest_main)
#add_test(NAME test_main COMMAND test_main)
