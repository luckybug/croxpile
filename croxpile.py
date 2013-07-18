#!/usr/bin/env python

import os
from SCons.Builder import Builder
from SCons.Defaults import DirScanner, Copy
from SCons.Errors import UserError

def get_variable(env, variable):
    """
    Extract a variable from the environment if it exists.
    Optionally exits the run
    """
    if variable in os.environ:
        return os.environ[variable]
    elif variable in env:
        return env[variable]
    else:
        return None;

def crox_check_settings(env, kw):
    do_exit = False

    _item = 'CROX_TOOLS_PATH'
    if kw.has_key(_item): # override it
        env[_item] = kw[_item]
    elif not get_variable(env, _item):
        print "Please set %s. export %s=path" % (_item, _item)
        print "or run scons with argument '%s=path'" % _item
        do_exit = True

    _item = 'CROX_TOOLS_PREFIX'
    if kw.has_key(_item):
        env[_item] = kw[_item]
    if not get_variable(env, _item):
        print "Please set %s. export %s=prefix" % (_item, _item)
        print "or run scons with argument '%s=prefix'" % _item
        do_exit = True

    if do_exit:
        env.Exit(1)

    return (env['CROX_TOOLS_PATH'], env['CROX_TOOLS_PREFIX'])

def generate(env, **kw):
    """ SCons tool entry point """

    _path, _prefix = crox_check_settings(env, kw)

    gnu_tools = ['gcc', 'g++', 'gnulink', 'ar', 'gas']
    for tool in gnu_tools:
        env.Tool(tool)

    env['CC'] =  _prefix+'gcc'
    env['CXX'] = _prefix+'g++'
    env['AS'] = _prefix+'as'
    env['AR'] = _prefix+'ar'
    env['RANLIB'] = _prefix+'ranlib'
    env['OBJCOPY'] = _prefix+'objcopy'
    env['STRIP'] = _prefix+'strip'

    env.PrependENVPath('PATH', _path) 


def exists(env):
    """ NOOP method required by SCons """
    return 1
