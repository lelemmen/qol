# &PROJECT_NAME& v0.1.0
[comment]: <> (Add the travis build status)

[comment]: <> (Give a short explanation of the project)



## Dependencies
[comment]: <> (Add dependencies through badges from https://img.shields.io)



## Installation

To install this library:
1. clone the master branch, which contains the latest release:

        git clone  --branch master --single-branch
        cd &PROJECT_NAME&

2. perform an out-of-source cmake build:

        mkdir build && cd build
        cmake -DINSTALLATION_PREFIX=prefix ..
        make && make test && sudo make install

    where
    * `prefix` is the installation prefix (defaulted to `/usr/local`) you want the library to be installed at:
        * the library `lib&PROJECT_NAME&.a` will be installed in `prefix/&PROJECT_NAME&/lib`
        * the header files (and cmake files, see Usage) will be installed in `prefix/&PROJECT_NAME&/include`



## Usage

Basic usage of this library can be found in the `tests` directory. If you use CMake in other projects, you can add the following CMake command to the CMakeLists.txt-file:

    find_package(&PROJECT_NAME& 1.2.2)

CMake then provides the commands `&PROJECT_NAME&_INCLUDE_DIRS` to be used in your `target_include_directories` and the library `&PROJECT_NAME&` to be used in your `target_link_libraries`.
