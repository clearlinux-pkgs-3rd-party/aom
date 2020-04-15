#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aom
Version  : 1.0.0
Release  : 3
URL      : https://aomedia.googlesource.com/aom/+archive/refs/heads/master.tar.gz
Source0  : https://aomedia.googlesource.com/aom/+archive/refs/heads/master.tar.gz
Summary  : GoogleTest (with main() function)
Group    : Development/Tools
License  : BSD-2-Clause
Requires: aom-bin = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : nasm
BuildRequires : perl
BuildRequires : python3
BuildRequires : yasm

%description
# AV1 Codec Library
## Contents
1. [Building the lib and applications](#building-the-library-and-applications)
- [Prerequisites](#prerequisites)
- [Get the code](#get-the-code)
- [Basics](#basic-build)
- [Configuration options](#configuration-options)
- [Dylib builds](#dylib-builds)
- [Debugging](#debugging)
- [Cross compiling](#cross-compiling)
- [Sanitizer support](#sanitizers)
- [MSVC builds](#microsoft-visual-studio-builds)
- [Xcode builds](#xcode-builds)
- [Emscripten builds](#emscripten-builds)
- [Extra Build Flags](#extra-build-flags)
- [Build with VMAF support](#build-with-vmaf)
2. [Testing the library](#testing-the-av1-codec)
- [Basics](#testing-basics)
- [Unit tests](#1_unit-tests)
- [Example tests](#2_example-tests)
- [Encoder tests](#3_encoder-tests)
- [IDE hosted tests](#ide-hosted-tests)
- [Downloading test data](#downloading-the-test-data)
- [Adding a new test data file](#adding-a-new-test-data-file)
- [Additional test data](#additional-test-data)
- [Sharded testing](#sharded-testing)
- [Running tests directly](#1_running-test_libaom-directly)
- [Running tests via CMake](#2_running-the-tests-via-the-cmake-build)
3. [Coding style](#coding-style)
4. [Submitting patches](#submitting-patches)
- [Login cookie](#login-cookie)
- [Contributor agreement](#contributor-agreement)
- [Testing your code](#testing-your-code)
- [Commit message hook](#commit-message-hook)
- [Upload your change](#upload-your-change)
- [Incorporating Reviewer Comments](#incorporating-reviewer-comments)
- [Submitting your change](#submitting-your-change)
- [Viewing change status](#viewing-the-status-of-uploaded-changes)
5. [Support](#support)
6. [Bug reports](#bug-reports)

%package bin
Summary: bin components for the aom package.
Group: Binaries

%description bin
bin components for the aom package.


%package dev
Summary: dev components for the aom package.
Group: Development
Requires: aom-bin = %{version}-%{release}
Provides: aom-devel = %{version}-%{release}
Requires: aom = %{version}-%{release}

%description dev
dev components for the aom package.


%prep
%setup -q -c -n master.tar
cd %{_builddir}/master.tar

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586984033
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DBUILD_SHARED_LIBS=1 \
-DENABLE_NASM=on
make  %{?_smp_mflags}  VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
export FFLAGS="$FFLAGS -march=haswell -m64"
export FCFLAGS="$FCFLAGS -march=haswell -m64"
%cmake .. -DBUILD_SHARED_LIBS=1 \
-DENABLE_NASM=on
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1586984033
rm -rf %{buildroot}
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/usr/lib64/libaom.so
/usr/usr/lib64/libaom.so.0
/usr/usr/lib64/libaom.so.1.0.0
/usr/usr/lib64/pkgconfig/aom.pc

%files bin
%defattr(-,root,root,-)
/usr/bin/aomdec
/usr/bin/aomenc
/usr/bin/haswell/aomdec
/usr/bin/haswell/aomenc

%files dev
%defattr(-,root,root,-)
/usr/include/aom/aom.h
/usr/include/aom/aom_codec.h
/usr/include/aom/aom_decoder.h
/usr/include/aom/aom_encoder.h
/usr/include/aom/aom_frame_buffer.h
/usr/include/aom/aom_image.h
/usr/include/aom/aom_integer.h
/usr/include/aom/aomcx.h
/usr/include/aom/aomdx.h
