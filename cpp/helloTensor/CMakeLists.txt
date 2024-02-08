cmake_minimum_required(VERSION 3.18 FATAL_ERROR)
project(helloTensor)

find_package(Torch REQUIRED)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")

add_executable(helloTensor helloTensor.cpp)
target_link_libraries(helloTensor "${TORCH_LIBRARIES}")
set_property(TARGET helloTensor PROPERTY CXX_STANDARD 17)