<h1 align="center">⚙️ Cython Batch Builder</h1>
<p align="center">
  <b>Speed up Python. Secure your logic. Deploy compiled modules in one line.</b>
</p>
<p align="center">
  Batch compile .py/.pyx files into blazing-fast .pyd/.so binaries using Cython
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6+-blue" alt="Python 3.6+">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey">
  <img src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## ✨ Why This Project Matters

Python is elegant, but performance and code security are often concerns in production environments.  
**Cython Batch Builder** is my original solution to solve these pain points:

- **Performance**: Compiles Python to C-extension binaries with aggressive optimization (`-O3`).
- **Security**: Hides logic and obfuscates source code through C-level transformation.
- **Scalability**: Compiles many scripts in one go, with automated cleanup and zero conflict.
- **Portability**: Output modules (`.pyd` / `.so`) are easy to distribute and reuse.

> Built to solve real-world deployment bottlenecks in high-speed, production-grade Python systems.

---

## 🚀 Features

- ✅ Batch compilation of `.py` or `.pyx` files
- 🔄 Converts `.py` → `.pyx` on-the-fly if needed
- 🔒 Security-enhanced build with stripped signatures
- ⚡ Performance-tuned with `-O3`, `-fomit-frame-pointer`, `NDEBUG`
- 🧹 Auto-cleans all intermediate files (like `.c`, `.html`, `build/`)
- 🧠 Fully self-contained, no external configs needed
- 🧪 Cross-platform output: `.pyd` (Windows) and `.so` (Linux/macOS)

---

## 📦 Requirements

- Python ≥ 3.6
- [Cython](https://cython.org/)
- setuptools
- C++ compiler:
  - 🪟 Windows: MSVC
  - 🐧 Linux: GCC / Clang
  - 🍎 macOS: Clang (Xcode)

Install dependencies:

```bash
pip install cython setuptools
