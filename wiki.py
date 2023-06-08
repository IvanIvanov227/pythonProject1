import wikipedia


def get_info_wiki(article):
    # Установил язык
    wikipedia.set_lang('ru')
    try:
        # Запрос на получение статьи
        return f'{wikipedia.summary(article)}'
    # Информация не найдена
    except wikipedia.WikipediaException:
        return 'Информация не найдена'


