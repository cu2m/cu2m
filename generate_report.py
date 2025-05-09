import copy
import os
import shutil
from pathlib import Path
from subprocess import call

from sphinx.util.osutil import make_filename_from_project

from docs import conf as config

BACKEND_DIR = "cu2m-backend"
FRONTEND_DIR = "cu2m-frontend"
CURRENT_PATH = Path(__file__).parent.resolve()
BACKEND_PATH = CURRENT_PATH / BACKEND_DIR
FRONTEND_PATH = CURRENT_PATH / FRONTEND_DIR

BACKEND_RESULT = CURRENT_PATH / "backend.xml"
FRONTEND_RESULT = CURRENT_PATH / "frontend.xml"

BUILD_DIR = CURRENT_PATH / "build"
DOC_DIR = CURRENT_PATH / "docs"
DEST_DIR = CURRENT_PATH / "cu2m-test-document.pdf"

ENV_VARS = copy.deepcopy(os.environ)
ENV_VARS.pop("VIRTUAL_ENV", None)


def run_backend_tests():
    """
    Run the backend tests using pytest.
    """

    call(
        [
            "poetry",
            "run",
            "pytest",
            f"--junit-xml={BACKEND_RESULT}",
        ],
        shell=True,
        cwd=BACKEND_PATH,
        env=ENV_VARS,
    )


def run_frontend_tests():
    """
    Run the frontend tests using cypress.
    """

    # TODO: Add cypress test command


def generate_latex_report():
    """
    Generate a LaTeX report from the XML files.
    """

    call(
        [
            "sphinx-build",
            "-M",
            "latex",
            str(DOC_DIR),
            str(BUILD_DIR),
        ],
        shell=True,
        cwd=BACKEND_PATH,
        env=ENV_VARS,
    )


def build_pdf():
    """
    Build the PDF from the LaTeX report.
    """

    call("make", cwd=BUILD_DIR / "latex", shell=True)

    # Move the PDF to the current directory
    pdf_file = BUILD_DIR / f"latex/{make_filename_from_project(config.project)}.pdf"
    pdf_file.rename(DEST_DIR)


def clean_up():
    """
    Clean up the generated files.
    """

    BACKEND_RESULT.unlink(missing_ok=True)
    FRONTEND_RESULT.unlink(missing_ok=True)
    DEST_DIR.unlink(missing_ok=True)
    shutil.rmtree(BUILD_DIR, ignore_errors=True)


def main():
    """
    Main function to run the tests and generate the report.
    """

    clean_up()
    run_backend_tests()
    run_frontend_tests()
    generate_latex_report()
    build_pdf()


if __name__ == "__main__":
    main()
