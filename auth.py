import datetime
from typing import Optional

import yaml
from flask import redirect, Response
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


def goto_shave(login: str, password: str, params: Optional[ImmutableMultiDict] = None) -> Response:
    """
    редиректит пользователя на ендпоинт /shave, со всемми гет параметрами, которые были в ссылке
    и проставляет ему в куку логин и пароль, а также время простановки кук для определения возможности шейва.
    :param login: значение переданное в body в качестве логина
    :param password: значение переданное в body в качестве пароля
    :param params: get-параметры ссылки, если есть
    :return:
    """
    parameters = dict(params)
    if parameters:
        parameters_to_string = []
        for key, value in parameters.items():
            parameters_to_string.append(f'{key}={value}')
        result = "&".join(parameters_to_string)
        location = f'http://0.0.0.0:5000/shave?{result}'
    else:
        location = 'http://0.0.0.0:5000/shave'
    res = redirect(location=location, code=302)
    res.set_cookie("Login", value=login)
    res.set_cookie("Password", value=password)
    time = str(datetime.datetime.now())
    res.set_cookie('DateSet', value=time)
    return res
