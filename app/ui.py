from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext

from .models import User


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'Имя',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__surname = ext.ExtStringField(
            label=u'Фамилия',
            name='surname',
            allow_blank=False,
            anchor='100%')

        self.field__gender = make_combo_box(
            label=u'Пол',
            name='gender',
            allow_blank=False,
            anchor='100%',
            data=User.GENDERS)

        self.field__birthday = ext.ExtDateField(
            label=u'Дата рождения',
            name='birthday',
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__surname,
            self.field__gender,
            self.field__birthday,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'