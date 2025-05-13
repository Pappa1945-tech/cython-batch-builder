# build_to_pyd.py
import os
import shutil
import sys
from Cython.Build import cythonize
from setuptools import Extension, setup
import glob

def build(file_paths):
    original_dir = os.getcwd()
    
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        base_name, ext = os.path.splitext(file_name)

        if ext not in [".py", ".pyx"]:
            print(f"Skipping {file_name}: Only .py or .pyx files are supported.")
            continue

        # Create unique temp directory for each file
        temp_dir = f"temp_build_dir_{base_name}"
        os.makedirs(temp_dir, exist_ok=True)
        
        try:
            # Copy source file to temp directory
            temp_file_path = os.path.join(temp_dir, file_name)
            shutil.copy(os.path.join(original_dir, file_path), temp_file_path)

            # Rename .py to .pyx if needed
            if ext == ".py":
                pyx_file = os.path.join(temp_dir, base_name + ".pyx")
                os.rename(temp_file_path, pyx_file)
                temp_file = pyx_file
            else:
                temp_file = temp_file_path

            # Security-hardened compilation
            os.chdir(temp_dir)  # Work in temp directory
            
            compiler_directives = {
                "language_level": "3",
                "binding": False,
                "embedsignature": False,
            }
            
            ext = Extension(
                name=base_name,
                sources=[os.path.basename(temp_file)],
                language="c++",
                define_macros=[("NDEBUG", "1")],
                extra_compile_args=["-O3", "-fomit-frame-pointer"],
            )

            ext_modules = cythonize(
                ext,
                compiler_directives=compiler_directives,
                annotate=False,
            )

            setup(
                script_args=["build_ext", "--inplace"],
                ext_modules=ext_modules,
                name=base_name,
            )

            # Move compiled files back to original directory
            os.chdir(original_dir)
            for ext_type in ["*.pyd", "*.so"]:
                for file in glob.glob(os.path.join(temp_dir, f"{base_name}{ext_type}")):
                    shutil.move(file, original_dir)

        finally:
            # Cleanup
            os.chdir(original_dir)
            shutil.rmtree(temp_dir, ignore_errors=True)
            
            # Remove intermediate files in original directory
            for pattern in [f"{base_name}.c", f"{base_name}*.html"]:
                for file in glob.glob(pattern):
                    os.remove(file)
            
            print(f"Successfully compiled: {file_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python build_to_pyd.py file1.py [file2.py ...]")
        print("       python build_to_pyd.py *.py")
    else:
        build(sys.argv[1:])