import daemon
import lockfile
import signal
import sys

from engine import Engine


def kill(signum, frame):
    sys.exit(0)


engine = Engine(kill_method=kill)


with daemon.DaemonContext(
    signal_map={
        signal.SIGTERM: kill,
        signal.SIGTSP: engine.shutdown,
    },
    pidfile=lockfile.FileLock('/var/run/mtp.pid'),
    chroot_directory=None,
    working_directory='/var/lib/mtp',
):
    engine.run()
