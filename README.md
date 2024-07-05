# simple-chat

This is a simple chat application template using C++17, Conan, and CMake.

## Dependencies
- Boost 1.85.0
- spdlog 1.14.1
- gtest 1.14.0

## Build and Run

### Prerequisites
- [Conan](https://conan.io/downloads.html)
- [CMake](https://cmake.org/download/)

### Steps

1. Install the dependencies using Conan:
   ```sh
   conan install . --build=missing
   ```

2. Create a build directory and run CMake:
   ```sh
   mkdir build
   cd build
   cmake ..
   ```

3. Build the project:
   ```sh
   cmake --build .
   ```

4. Run the application:
   ```sh
   ./bin/my_cpp_project
   ```

5. Run the tests:
   ```sh
   ctest
   ```

### Note
Ensure you are using macOS Sonoma 14.5 and have the necessary build tools installed.
