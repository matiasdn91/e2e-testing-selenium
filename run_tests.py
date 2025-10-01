import os
import subprocess
import sys
from datetime import datetime

# Carpeta para guardar reportes
REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

# Timestamp para diferenciar los reportes
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

def run_tests(browser_name):
    report_file = os.path.join(REPORT_DIR, f"report_{browser_name}_{timestamp}.html")
    env = os.environ.copy()
    env["BROWSER"] = browser_name

    print(f"\nEjecutando tests en {browser_name}...")
    print(f"Reporte generado en: {report_file}\n")

    # Ejecuta pytest en un subproceso
    result = subprocess.run(
        ["pytest", "tests", "-v", f"--html={report_file}", "--self-contained-html"],
        env=env
    )

    return result.returncode

def main():
    if len(sys.argv) > 1:
        browser_arg = sys.argv[1].lower()
    else:
        browser_arg = "chrome"  # default

    exit_code = 0

    if browser_arg == "chrome":
        exit_code = run_tests("chrome")
    elif browser_arg == "firefox":
        exit_code = run_tests("firefox")
    elif browser_arg == "all":
        code_chrome = run_tests("chrome")
        code_firefox = run_tests("firefox")
        # Si alguno falla, retornamos 1
        exit_code = 1 if code_chrome != 0 or code_firefox != 0 else 0
    else:
        print("Argumento inválido. Usar: python run_tests.py [chrome|firefox|all]")
        sys.exit(1)

    sys.exit(exit_code)

if __name__ == "__main__":
    main()
