from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext

class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%')
        
        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last login',
            allow_blank=True,
            anchor='100%',
            format = 'd.m.Y')
        
        self.field__superuser = ext.ExtCheckBox(
            label=u'superuser status',
            name='superuser status',
            allow_blank=True,
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')
        
        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first name',
            allow_blank=True,
            anchor='100%')
        
        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last name',
            allow_blank=True,
            anchor='100%')
        
        self.field__email = ext.ExtStringField(
            label=u'email address',
            name='email',
            allow_blank=True,
            anchor='100%')
        
        self.field__staff = ext.ExtCheckBox(
            label=u'staff status',
            name='staff',
            allow_blank=True,
            anchor='100%')
        
        self.field__active = ext.ExtCheckBox(
            label=u'active',
            name='active',
            allow_blank=True,
            anchor='100%')

        self.date_joined = ext.ExtDateField(
            label=u'date joined',
            name='date joined',
            allow_blank=True,
            anchor='100%',
            format = 'd.m.Y')
    
    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__staff,
            self.field__active,
            self.date_joined,
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'
        
class PermissionAddWindow(BaseEditWindow):

    def _init_components(self):
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=True,
            anchor='100%')
        
        self.field__content_type = ext.ExtDictSelectField(
            label=u'content type',
            name='content_type',
            allow_blank=True,
            anchor='100%',
            value={'log entry', 'user', 'permission', 'group'})
        
        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=True,
            anchor='100%')
    
    def _do_layout(self):
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'