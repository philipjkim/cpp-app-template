from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout

class SimpleChatProjectConan(ConanFile):
    name = "simple-chat"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    requires = [
        "boost/1.85.0",
        "spdlog/1.14.1",
        "gtest/1.14.0"
    ]
    default_options = {}

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["simple_chat"]
