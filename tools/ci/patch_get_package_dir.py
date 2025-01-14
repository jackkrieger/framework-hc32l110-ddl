# for some reason, the 'platform_packages' directive in platformio.ini
# does not apply to 'DefaultEnvironment().PioPlatform().get_package_dir()', which is used 
# by the hc32l1xx build system...
#
# this script is a workaround, patching the 'get_package_dir' method to return the directory
# defined by 'board_build.ddl_package_dir' (relative to $PROJECT_DIR) for the 'framework-hc32f46x-ddl' package.
from SCons.Script import DefaultEnvironment
from os.path import abspath, join

env = DefaultEnvironment()
platform = env.PioPlatform()
original_get_package_dir = platform.get_package_dir

def get_package_dir_override(name):
    if name == "framework-hc32l1xx-ddl":
        project_dir = env.subst("$PROJECT_DIR")
        ddl_package_dir = env.BoardConfig().get("build.ddl_package_dir", "")
        if ddl_package_dir == "":
            raise ValueError("board_build.ddl_package_dir is not defined")

        package_dir = abspath(join(project_dir, ddl_package_dir))
        print("Using package dir: " + package_dir)
        return package_dir
    else:
        return original_get_package_dir(name)

platform.get_package_dir = get_package_dir_override