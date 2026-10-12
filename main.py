import storage
from cli import run_cli

def main():
    storage.init_db()
    run_cli()

if __name__ == "__main__":
    main()