# cpp-app-template

This is a simple template of C++ CLI application using C++17, Conan, and CMake.

## Dependencies
- Boost 1.85.0
- spdlog 1.14.1
- gtest 1.14.0

## Build and Run

### Prerequisites
- [Conan](https://conan.io/downloads.html)
- [CMake](https://cmake.org/download/)

### Steps

1. Create a build directory:
   ```sh
   mkdir build
   cd build
   ```

2. Install the dependencies using Conan:
   ```sh
   conan install .. --profile=default --build=missing
   ```

3. Run CMake to generate the build files, specifying the correct path to the Conan toolchain file and the build type:
   ```sh
   cmake .. -DCMAKE_TOOLCHAIN_FILE=Release/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
   ```

4. Build the project:
   ```sh
   cmake --build .
   ```

5. Run the application:
   ```sh
   ./bin/cpp-app
   ```

6. Run the tests:
   ```sh
   ctest
   ```

### Note
Ensure you are using macOS Sonoma 14.5 and have the necessary build tools installed.
