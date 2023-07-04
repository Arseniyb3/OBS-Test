from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .models import *
from .ui import UserAddWindow, PermissionAddWindow

class User(ObjectPack):

    model = User
    add_window = edit_window = UserAddWindow
    add_to_menu = True

class Permission(ObjectPack):
    model = Permission
    add_window = edit_window = PermissionAddWindow
    add_to_menu = True

class Group(ObjectPack):
    model = Group
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)
    add_to_menu = True

class ContentType(ObjectPack):
    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)
    add_to_menu = True