"""File to run static code analysis for mypy and pylint"""
import subprocess

# MyPy
subprocess.run("mypy --install-types --non-interactive".split(), check=True)
subprocess.run("mypy ./ --exclude venv".split(), check=False)

# PyLint
subprocess.run("pylint -j 0 "
               "--load-plugins=pylint_django "
               "--max-parents=14 "
               "--django-settings-module=qr_web.settings "
               "--recursive=y "
               "--ignore=venv "
               "./".split(), check=False)
