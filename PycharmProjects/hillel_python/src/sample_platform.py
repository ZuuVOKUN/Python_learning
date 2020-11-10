import platform
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='platform.log',
                    filemode='w')

print('My system description:')
logging.info('My system description:')


print('Version           : ', platform.python_version())
print('Version tuple     : ', platform.python_version_tuple())
print('Compiler          : ', platform.python_compiler())
print('Build             : ', platform.python_build())

print('System            : ', platform.system())
print('Node              : ', platform.node())
print('Release           : ', platform.release())
print('Version           : ', platform.version())
print('Machine           : ', platform.machine())
print('Processor         : ', platform.processor())
print('Interpreter       : ', platform.architecture())

logging.info(f'Version           : {platform.python_version()}')
logging.info(f'Version tuple     : {platform.python_version_tuple()}')
logging.info(f'Compiler          : {platform.python_compiler()}')
logging.info(f'Build             : {platform.python_build()}')

logging.info(f'System            : {platform.system()}')
logging.info(f'Node              : {platform.node()}')
logging.info(f'Release           : {platform.release()}')
logging.info(f'Version           : {platform.version()}')
logging.info(f'Machine           : {platform.machine()}')
logging.info(f'Processor         : {platform.processor()}')
logging.info(f'Interpreter       : {platform.architecture()}')

# GCC - GNU C Compiler



