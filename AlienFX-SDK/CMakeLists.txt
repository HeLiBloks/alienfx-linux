cmake_minimum_required(VERSION 3.16)
project(AlienFX_SDK LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_C_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(hidapi REQUIRED)
find_package(libusb REQUIRED)
find_package(loguru REQUIRED)
find_package(nlohmann_json REQUIRED)

set(ALIENFX_HIDAPI_TARGET hidapi::hidapi)
if(TARGET hidapi::libusb)
  set(ALIENFX_HIDAPI_TARGET hidapi::libusb)
endif()

# ----------- SDK SOURCES ------------

file(GLOB_RECURSE SDK_SOURCES CONFIGURE_DEPENDS src/*.cpp)

add_library(AlienFX_SDK STATIC ${SDK_SOURCES})

target_include_directories(AlienFX_SDK
                           PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

target_link_libraries(
  AlienFX_SDK
  PUBLIC libusb::libusb
         ${ALIENFX_HIDAPI_TARGET}
         loguru::loguru
         nlohmann_json::nlohmann_json)
