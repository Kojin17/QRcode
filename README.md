# Проект "Генератор QR-кодов с интерфейсом на Python" 
Представляет собой простое графическое приложение, созданное с использованием библиотеки Tkinter для построения пользовательского интерфейса и библиотеки qrcode для генерации QR-кодов. Это приложение позволяет пользователям вводить текстовые данные и генерировать QR-код, представляющий введенную информацию.

### Основные компоненты проекта:

1. **Главное окно приложения:**
   - Отображает заголовок "QR Code Generator".
   - Содержит текстовое поле для ввода данных.
   - Имеет кнопку "Создать QR-код" для генерации QR-кода.

2. **Методы и функции:**
   - **generate_qr_code:** Функция, вызываемая при нажатии кнопки "Создать QR-код". Она извлекает данные из текстового поля, создает QR-код с использованием библиотеки qrcode, и отображает его в графическом интерфейсе.

3. **Отображение QR-кода:**
   - Используется метка (Label) для отображения сгенерированного QR-кода.
   - Изображение QR-кода обновляется в интерфейсе при каждой новой генерации.

### Инструкции по использованию:

1. Введите текстовые данные в соответствующее текстовое поле.
2. Нажмите кнопку "Создать QR-код".
3. Приложение отобразит сгенерированный QR-код в интерфейсе.
4. Возможность сохранения QR-кода в файл можно добавить по необходимости.

### Требования к запуску:

1. Python
2. Установленные библиотеки: tkinter, qrcode, Pillow

Этот проект предоставляет основу для создания полноценного генератора QR-кодов с использованием Python и может быть расширен в соответствии с конкретными потребностями и требованиями.
