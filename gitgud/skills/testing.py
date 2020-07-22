import os
import subprocess


def simulate(gg, level, commands):
    level._setup()

    for command in commands:
        if '^' in command and os.name == 'nt':
            command = command.replace('^', '^^')
        # Only test if there are commands which change state.
        assert not level._test()
        subprocess.call(command, shell=True)

    assert level._test()
