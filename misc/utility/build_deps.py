import os


def get_build_deps_folder(engine_root: str) -> str:
    """
	Return the directory used by install scripts and SCons for optional SDKs.
    Resolution order:
    1. ``GODOT_BUILD_DEPS`` if set
    2. ``<engine_root>/godot_build_deps``
    """
    override = os.environ.get("GODOT_BUILD_DEPS")
    if override:
        return os.path.abspath(os.path.expanduser(override))

    return os.path.join(os.path.abspath(engine_root), "godot_build_deps")
