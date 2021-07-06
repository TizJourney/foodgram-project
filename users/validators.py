from django.contrib.auth import password_validation

class UserAttributeSimilarityValidator(
    password_validation.UserAttributeSimilarityValidator
    ):
    def get_help_text(info):
        return (
            'Ваш пароль не должен совпадать с вашим именем или другой '
            'персональной информацией или быть слишком похожим на неё.'
        )


class CommonPasswordValidator(
    password_validation.CommonPasswordValidator
    ):
    def get_help_text(info):
        return (
            'Ваш пароль не может быть одним из широко распространённых паролей.'
        )

class NumericPasswordValidator(
    password_validation.NumericPasswordValidator
    ):
    def get_help_text(info):
        return (
            'Ваш пароль не может состоять только из цифр.'
        )
