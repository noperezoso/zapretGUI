# zapretGUI

Данный проект представляет собой графический пользовательский интерфейс (GUI) для программы [zapret](https://github.com/bol-van/zapret), являющимся автономным средством противодействия DPI, не требующим подключения каких-либо сторонних серверов.

## Описание

Графический интерфейс позволяет настраивать и управлять функциями zapret без необходимости использования командной строки, делая программу более доступной для пользователей без технических навыков.

Основные возможности:

- Изменение параметров запуска zapret через графический интерфейс
- Быстрое включение/отключение противодействия DPI
- Автозапуск zapret при старте системы

## Быстрый старт

0. Установите zapretGUI в соответствии с [инструкцией](https://github.com/noperezoso/zapretGUI?tab=readme-ov-file#установка)
1. Запустить zapretGUI
2. Открыть окно для изменения фильтров, нажав [Фильтры]
3. В выпадающем списке выбрать нужный файл со стратегиями (например, preset_russia.cmd)
4. Нажать кнопку [Применить] и после этого закрыть окно
5. В блоке "Управление" выбрать тип автозапуска (Служба)
6. Там же нажать [Создать], а после - [Запустить]

## Использование

Главное окно - zapretGUI:

![zapretGUI](media/main_window.png)

- Запустить/Обновить - скачивание последней версии zapret и полная замена текущей версии, если таковая имеется
- Фильтры - изменение параметров запуска zapret
- Управление - изменение состояния работы программы

Фильтры - Изменение фильтров:

![Изменение фильтров](media/filters_window.png)

- Выпадающий список - файлы со встроенными стратегиями
- Текстовое поле - полученные из файла строки аргументов для zapret, которые можно доработать перед применением
- Применить - сохраняет строки из текстового поля для дальнейших действий
- Очистить - очищает текстовое поле

## Требования

- Windows 10/11 64-разрядная

## Установка

1. Скачать последнюю версию GUI со [страницы релиза](https://github.com/noperezoso/zapretGUI/releases/latest)
2. Распаковать архив в удобное место (желательно, чтобы в пути не было кириллицы)
3. Запустить исполняемый файл zapretGUI.exe
4. Нажать кнопку [Установить] и дождаться изменения текста кнопки на "Обновить"

## TDs
- Экран первого запуска программы
- Проверка наличия обновлений zapretGUI и zapret
- Поддержка разных кодировок для открытия файла в окне "Фильтры"
- Открытие внешнего файла со стратегиями в окне "Фильтры"
- Проверка блокировки ресурсов и получение доступных стратегий в отдельном окне
- Поддержка Windows 7, 8, 8.1 в виде отдельных сборок
- Продвинутый режим интерфейса

## Благодарности

Выражаем благодарность [bol-van](https://github.com/bol-van) за создание оригинальной программы [zapret](https://github.com/bol-van/zapret)

## Лицензия

Данный проект распространяется под лицензией GNU AGPLv3. [LICENSE](https://github.com/noperezoso/zapretGUI/blob/main/LICENSE)
