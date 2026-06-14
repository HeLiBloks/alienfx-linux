from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout


class AlienFXLinuxConan(ConanFile):
    name = "alienfx-linux"
    version = "1.1.0"
    package_type = "application"

    settings = "os", "compiler", "build_type", "arch"
    options = {
        "build_cli": [True, False],
        "build_example": [True, False],
    }
    default_options = {
        "build_cli": True,
        "build_example": True,
        "loguru/*:enable_streams": True,
    }

    exports_sources = (
        "CMakeLists.txt",
        "AlienFX-SDK/*",
        "AlienFan-SDK/*",
        "Example-App/*",
        "alienfx-cli/*",
    )

    requires = (
        "hidapi/0.15.0",
        "libusb/1.0.26",
        "loguru/cci.20230406",
        "cli11/2.6.2",
        "nlohmann_json/3.12.0",
    )

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        tc = CMakeToolchain(self)
        tc.variables["ALIENFX_BUILD_CLI"] = self.options.build_cli
        tc.variables["ALIENFX_BUILD_EXAMPLE"] = self.options.build_example
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
