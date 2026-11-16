from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout


class CompressorRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        if self.settings.os == "Windows":
            pass

        self.requires("spdlog/1.15.1")
        self.requires("yaml-cpp/0.8.0")
        self.requires("argparse/2.9")
        self.requires("cpp-httplib/0.30.1", options={"with_openssl": True})
        self.requires("nlohmann_json/3.11.3")

    def build_requirements(self):
        self.tool_requires("cmake/[>=3.12]")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
