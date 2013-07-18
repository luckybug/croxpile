croxpile
========

extension scons for cross compile


SConstruct example
if not ARGUMENTS.has_key('CROX_TOOLS_PATH'):
    ARGUMENTS['CROX_TOOLS_PATH'] = '/opt/arm-2007q3/bin/'
if not ARGUMENTS.has_key('CROX_TOOLS_PREFIX'):
    ARGUMENTS['CROX_TOOLS_PREFIX'] = 'arm-none-linux-gnueabi-'

targets = set(COMMAND_LINE_TARGETS)
for _target in targets:
    env = Environment(tools=['default', 'croxpile'], **ARGUMENTS)
    #print env.Dump()
    Export('env')
    objs = env.SConscript(_target + '/SConscript')


