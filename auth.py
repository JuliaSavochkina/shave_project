import yaml
from flask import redirect
from werkzeug.datastructures import ImmutableMultiDict


def is_allowed(login: str, password: str) -> bool:
    """
    проверяет допуск пользователя по логину и паролю переданному в теле запроса в виде json
    :param login: переданный в боди при переходе логин
    :param password: переданный в боди при переходе пароль
    :return: идентификатор того, авторизован ли пользователь
    """
    auth_given = {'login': login, 'pass': password}
    auth_known = []
    with open('auth.yml') as config:
        auth_data = yaml.load(config, Loader=yaml.FullLoader)
    for each in auth_data.values():
        auth_known.append(each)
    return auth_given in auth_known


def goto_shave(params: ImmutableMultiDict):
    """
    редиректит пользователя на ендпоинт /shave, со всемми гет параметрами, которые были в ссылке
    и проставляет ему идентификтор в куку
    :return:
    """
    parameters = dict(params)
    parameters_to_string = []
    for key, value in parameters.items():
        parameters_to_string.append(f'{key}={value}')
    result = "&".join(parameters_to_string)
    location = f'http://0.0.0.0:5000/shave?{result}'
    return redirect(location=location, code=200)


if __name__ == '__main__':
    goto_shave(ImmutableMultiDict([('first', '111'), ('second', 'aaa')]))
