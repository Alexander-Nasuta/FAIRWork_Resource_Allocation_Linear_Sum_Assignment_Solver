import logging
import shutil

from rich.logging import RichHandler

from wzl_banner import wzl_banner
from fairwork_banner import banner_color as fairwork_banner

# print banner when logger is imported
w, h = shutil.get_terminal_size((80, 20))

#print(small_banner if w < 140 else big_banner)
print(wzl_banner)
print(fairwork_banner)

FORMAT = "%(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(show_path=True)]
)

log = logging.getLogger(__name__)

if __name__ == '__main__':
    # check if logger is working
    log.debug("debug msg")
    log.info("info msg")
    log.warning("warning msg")
    log.error("error msg")
    log.critical("critical msg")
