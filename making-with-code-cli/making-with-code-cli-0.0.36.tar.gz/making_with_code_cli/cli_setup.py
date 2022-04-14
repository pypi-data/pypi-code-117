from pathlib import Path
from enum import Flag, auto
from stat import *
import sys
from making_with_code_cli.styles import (
    address,
    question,
    confirm,
    info,
    success,
    warn,
    error,
)
import click
import requests
from subprocess import run
import yaml

INTRO_MESSAGE = (
    "Welcome to Making with Code setup. This program will ask you for some settings "
    "and make sure all the required software is installed on your computer. "
    "Some of the steps may take a while to complete. "
    "A few notes:"
)
INTRO_NOTES = [
    "You can re-run this script if you want to make any changes.",
    "You can quit this program by pressing Control + C at the same time.",
    "Many questions have default values, shown in [brackets]. Press enter to accept the default.",
    "The setup may ask for your password. As a security measure, you won't see any characters when you type it in.",
    "If you get stuck or have any questions, ask a teacher.",
]
WORK_DIR_PERMISSIONS = S_IRWXU | S_IXGRP | S_IXOTH

class Platform(Flag):
    MAC = auto()
    LINUX = auto()
    WSL = auto()
    SUPPORTED = MAC | LINUX | WSL
    UNSUPPORTED = 0

    @classmethod
    def detect(self):
        if Path("/proc/version").exists() and "WSL" in Path("/proc/version").read_text():
            return self.WSL
        if sys.platform.startswith("darwin"):
            return self.MAC
        if sys.platform.startswith("linux"):
            return self.LINUX
        return self.UNSUPPORTED

def default_work_dir():
    if (Path.home() / "Desktop").exists():
        return Path.home() / "Desktop" / "making_with_code"
    else:
        return Path.home() / "making_with_code"

def choose_mwc_username(default=None):
    """Asks the user to choose their MWC username."""
    return click.prompt(
        question("What is your MWC username?"),
        default=default
    )

def choose_work_dir(default=None):
    """Asks the user to choose where to save their work. 
    Loops until a valid choice is made, prompts if the directory is to be created, 
    and sets file permissions to 755 (u+rwx, g+x, o+x).
    """
    while True:
        work_dir = click.prompt(
            question("Where do you want to save your MWC work?"),
            default=default or default_work_dir(),
            type=click.Path(path_type=Path),
        )
        if work_dir.is_file():
            click.echo(error("There's already a file at that location."))
        elif work_dir.exists():
            work_dir.chmod(WORK_DIR_PERMISSIONS)
            return work_dir
        elif click.confirm(confirm("This directory doesn't exist. Create it?")):
            work_dir.mkdir(mode=WORK_DIR_PERMISSIONS, parents=True)
            return work_dir

def choose_mwc_site_url(default=None):
    """Asks the user for the Making With Code site URL
    """
    while True:
        url = click.prompt(
            question("What's the URL of your Making With Code website?"),
            default=default,
        )
        if url.endswith('/'):
            url = url[:-1]
        try:
            if not requests.get(url).ok:
                click.echo(error("Hmm, couldn't reach that site..."))
            else:
                if not requests.get(url + "/index.json"):
                    click.echo(error("Found the site, but it's not responding properly. " + 
                            "Please ask your teacher for help."))
                else:
                    return url
        except requests.exceptions.MissingSchema as e:
            click.echo(error(str(e)))

def choose_course(options):
    """Asks the user which course they are part of"""
    if len(options) == 0:
        err = "There is a problem with the MWC site. Please ask a teacher for help."
        error(err)
        raise ValueError(err)
    elif len(options) == 1:
        confirm(f"You are part of the course '{options[0]}'.")
        return options[0]
    else:
        return click.choice(
            question("Choose your course:"), 
            type=click.Choice(options),
        )  

def choose_editor(default=None):
    """Asks the user which editor they want to use."""
    while True:
        ed = click.prompt(
            question("Which code editor do you want to use?"),
            default=default
        )
        if editor_installed(ed) or ed in ['atom', 'subl', 'charm', 'mate', 'code']:
            return ed
        click.echo(error(f"Couldn't find {ed}. Double-check that it's installed."))

def editor_installed(ed):
    return bool(run(f"which {ed}", shell=True, capture_output=True).stdout)

def get_shell_name():
    shellpath = run("echo $SHELL", shell=True, capture_output=True, text=True)
    return shellpath.stdout.split('/')[-1].strip()

def get_mwc_rc_path():
    return (Path.home() / ".mwc_rc").resolve()

class SetupTask:
    "An idempotent task"
    platform = Platform.SUPPORTED
    description = "A task"

    def __init__(self, settings):
        self.settings = settings

    def run_task_if_needed(self):
        if not Platform.detect() & Platform.SUPPORTED:
            return 
        elif self.is_complete():
            self.report_not_needed()
        else:
            self.run_task()
            self.report_complete()
        
    def is_complete(self):
        return True    

    def run_task(self):
        pass

    def report_not_needed(self):
        click.echo(info(f"{self.description} is already complete."))
        
    def report_complete(self):
        click.echo(success(f"{self.description} is complete!"))

    def executable_on_path(self, name):
        return bool(run(f"which {name}", shell=True, capture_output=True).stdout)

class MWCShellConfig(SetupTask):
    """Writes a line in the rc shell config file sourcing ~/.mwc_rc.
    """
    description = "Link main shell config file to ~/.mwc_rc"

    def is_complete(self):
        return f"source {get_mwc_rc_path()}" in self.platform_rc_file().read_text()

    def run_task(self):
        with self.platform_rc_file().open('a') as fh:
            result = run("which mwc", shell=True, check=True, text=True, capture_output=True)
            mwcpath = Path(result.stdout).parent
            fh.write(f"\n# MAKING WITH CODE\n")
            fh.write(f'export PATH="{mwcpath}:$PATH"\n')
            fh.write(f"source {get_mwc_rc_path()}\n")
        
    def platform_rc_file(self):
        shell = get_shell_name()
        candidates = [
            ("bash", Path.home() / ".bash_profile"),
            ("bash", Path.home() / ".bash_rc"),
            ("zsh", Path.home() / ".zprofile"),
            ("zsh", Path.home() / ".zshrc"),
        ]
        for sh, rc in candidates:
            if shell == sh and rc.exists():
                return rc
        raise IOError("Can't find an rc file.")

class InstallHomebrew(SetupTask):
    description = "Install homebrew"

    def is_complete(self):
        return self.executable_on_path("brew")

    def run_task(self):
        click.echo(address("Installing homebrew... (this may take a while)"))
        cmd = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
        run(cmd, shell=True, check=True)

class InstallXCode(SetupTask):
    description = "Install XCode"
    platform = Platform.MAC

    def is_complete(self):
        return bool(run("xcode-select -p", shell=True, capture_output=True, check=True).stdout)

    def run_task(self):
        msg = (
            "Installing Xcode... (this may take a while)"
            "Please click \"Install\" and accept the license agreement. "
        )
        click.echo(address(msg))
        run("xcode-select --install", shell=True, check=True)

class InstallPoetry(SetupTask):
    description = "Install poetry"

    def is_complete(self):
        return self.executable_on_path("poetry")

    def run_task(self):
        shell = get_shell_name()
        click.echo(address("Installing poetry..."))
        run("curl -sSL https://install.python-poetry.org | python3 -", shell=True, check=True)
        click.echo(address("Installing poetry tab completions..."))
        if shell == "bash":
            Path("/etc/bash_completion.d").mkdir(exist_ok=True)
            run("poetry completions bash > /etc/bash_completion.d/poetry", shell=True, check=True)
        if shell == "zsh":
            Path("~/.zfunc").mkdir(exist_ok=True)
            run("poetry completions zsh > ~/.zfunc/_poetry", shell=True, check=True)

class WriteShellConfig(SetupTask):
    description = "Write the MWC shell configuration file ~/.mwc_rc"

    def is_complete(self):
        return False

    def run_task(self):
        click.echo(address("Writing the MWC shell configuration file..."))
        with get_mwc_rc_path().open('w') as fh:
            shell = get_shell_name()
            fh.write("# Making With Code RC File\n\n")
            fh.write("## Add Poetry to $PATH\n")
            fh.write('export PATH="$HOME/.local/bin:$PATH"\n\n')
            if Platform.detect() == Platform.MAC:
                if self.settings['editor'] == "subl":
                    fh.write("## Add subl to $PATH\n")
                    fh.write('export PATH="/Applications/Sublime Text.app/Contents/SharedSupport/bin:$PATH"\n\n')
            if Platform.detect() == Platform.WSL:
                if self.settings['editor'] == "subl":
                    fh.write("## Create subl alias for Sublime Text\n")
                    fh.write('alias subl=\'"/mnt/c/Program Files/Sublime Text 3/subl.exe"\'')
                if self.settings['editor'] == "atom":
                    fh.write("## Create atom alias\n")
                    fh.write('alias atom=”/mnt/c/Windows/System32/cmd.exe /c \'atom\'"\n\n')
        run(f"source {get_mwc_rc_path()}", shell=True, check=True)

class InstallPackage(SetupTask):
    package_name = "package"
    brew_name = "package"
    apt_name = "package"

    def __init__(self, *args, **kwargs):
        self.description = f"Install {self.package_name}"
        super().__init__(*args, **kwargs)

    def is_complete(self):
        return self.executable_on_path(self.package_name)
    
    def run_task(self):
        platform = Platform.detect()
        click.echo(address(f"Installing {self.package_name}..."))
        pkg = self.brew_name if (platform == Platform.MAC) else self.apt_name
        run(f"{self.package_installer()} install {pkg}", shell=True, check=True)

    def package_installer(self):
        platform = Platform.detect()
        if platform == Platform.LINUX:
            return "apt"
        if platform == Platform.MAC:
            return "brew"
        raise IOError(f"Platform {platform} not supported...")

class InstallPython3(InstallPackage):
    package_name = brew_name = apt_name = "python3"

class InstallGit(InstallPackage):
    package_name = brew_name = apt_name = "git"

class InstallTree(InstallPackage):
    package_name = brew_name = apt_name = "tree"

class InstallAtom(InstallPackage):
    platform = Platform.MAC
    package_name = brew_name = apt_name = "atom"

class InstallGh(InstallPackage):
    package_name = brew_name = "gh"

    def package_installer(self):
        return "brew"

class InstallImageMagick(InstallPackage):
    package_name = brew_name = apt_name = "imagemagick"

    def is_complete(self):
        return self.executable_on_path("magick")

class InstallHttpie(InstallPackage):
    package_name = brew_name = apt_name = "httpie"

class GHAuthentication(SetupTask):
    description = "Sign in to github"
    gh_auth_file = Path.home() / ".config/gh/hosts.yml"

    def is_complete(self):
        return "github.com" in self.gh_auth_data()

    def run_task(self):
        click.echo(address("You will now be prompted to log in to github.com (or to create an account)."))
        click.echo(address(" - Choose 'GitHub.com' when asked which account you want to log into."))
        click.echo(address(" - Choose 'HTTPS' when asked which protocol to use"))
        run("gh auth login", shell=True, check=True)

    def gh_auth_data(self):
        if self.gh_auth_file.exists():
            return yaml.safe_load(self.gh_auth_file.read_text())
        else:
            return {}

class GitConfiguration(SetupTask):
    """Configure global git settings.
    Can be skipped by setting `skip_git_config: true` in settings.
    """
    description = "Configure git"

    editorcmds = {
        "atom": "atom --wait",
        "code": "code --wait",
        "subl": "subl -n -w",
        "mate": "mate -w",
        "vim": "vim",
        "emacs": "emacs",
    }

    def is_complete(self):
        return self.settings.get("skip_git_config")

    def run_task(self):
        (Path.home() / ".gitconfig").touch()
        git_settings = {
            "init.defaultBranch": "main",
        }
        if self.settings.get('editor') in self.editorcmds:
            editorcmd = self.editorcmds[self.settings.get('editor')]
            git_settings["core.editor"] = f'"{editorcmd}"'
        if self.settings.get('git_name'):
            git_settings["user.name"] = self.settings['git_name']
        if self.settings.get('github_email'):
            git_settings["user.email"] = self.settings['github_email']
        for key, val in git_settings.items():
            run(f'git config --global --replace-all {key} "{val}"', shell=True, check=True)




