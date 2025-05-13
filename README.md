# 🔧 Cython Batch Builder

**Cython Batch Builder** is a command-line utility to compile one or many `.py` or `.pyx` files into optimized `.pyd` (Windows) or `.so` (Linux/macOS) extension modules using Cython. It's designed for developers who want to speed up execution and optionally obfuscate Python source code by compiling it to binary modules.

---

## 🚀 Features

- ✅ **Batch Compilation**: Compile multiple files at once using wildcards or direct filenames.
- 🧠 **Smart Conversion**: Automatically converts `.py` files to `.pyx` before compiling.
- 🛡️ **Clean Builds**: Each file is built in its own temporary directory to avoid conflicts.
- ⚡ **Performance Optimized**: Uses `-O3`, `-fomit-frame-pointer`, and `NDEBUG` for faster builds.
- 🧹 **Auto Cleanup**: Removes intermediate `.c`, `.html`, and `build/` directories post-build.
- 🌍 **Cross-Platform Support**: Compatible with Windows (`.pyd`) and Linux/macOS (`.so`).

---

## 📦 Requirements

- Python 3.6 or higher
- Cython
- setuptools
- Compiler (e.g., MSVC for Windows, gcc/clang for Linux/macOS)

### Install dependencies:
```bash
pip install cython setuptools
