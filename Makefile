
ROOT_DIR:=(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
REQUIREMENTS=requirements.txt
# Detects which OS is being used
# Only relevant for virtual environment creation
ifeq ($(OS), Windows_NT)
	SYSTEM_PYTHON=py
else
	SYSTEM_PYTHON=python3
endif

VENV_ROOT=venv
VENV_BIN=$(VENV_ROOT)/bin
VENV_PIP=$(VENV_BIN)/pip3
VENV_PYTHON=$(VENV_BIN)/python

all: virtualenv  uninstall install

virtualenv:
	@echo "Making virtual environment..."
	@$(SYSTEM_PYTHON) -m venv venv
	@echo "Installing all dependencies..."
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r $(REQUIREMENTS)

install:
	@echo "Installing sniffpy in the system"
	@$(VENV_PIP) install -e .
	@echo "  ________          ______        __  __             _____        " 
	@echo " |  ____\ \        / /  _ \      |  \/  |           |  __ \       "
	@echo " | |__   \ \  /\  / /| |_) |_____| \  / | __ _ _ __ | |__) |   _  "
	@echo " |  __|   \ \/  \/ / |  _ <______| |\/| |/ _  |  _ \|  ___/ | | | "
	@echo " | |____   \  /\  /  | |_) |     | |  | | (_| | |_) | |   | |_| | " 
	@echo " |______|   \/  \/   |____/      |_|  |_|\__,_| .__/|_|    \__, | "
	@echo "                                              | |           __/ | "
	@echo "                                              |_|          |___/  "
	@echo ""

uninstall:
	@echo "Uninstalling sniffpy in the system"
	$(VENV_PIP) uninstall sniffpy
	@echo "Succesfully uninstalled sniffpy"

test:
	$(VENV_BIN)/py.test
