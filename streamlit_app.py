import streamlit as st
from openai import OpenAI

st.title("Русско-Кетский и Кетско-Русский Переводчик")

# Запрос API-ключа у пользователя
api_key = st.text_input("Введите ваш ключ:", type="password")

if not api_key:
    st.warning("Пожалуйста, введите ваш ключ для продолжения.")
else:
    # Инициализация клиента OpenAI с введённым ключом
    client = OpenAI(api_key=api_key)

    # Выбор направления перевода
    direction = st.selectbox(
        "Выберите направление перевода",
        ("Русский → Кетский", "Кетский → Русский")
    )

    # Ввод слова для перевода
    word = st.text_input("Введите слово для перевода:")

    if st.button("Перевести") and word:
        try:
            # Определение целевого языка на основе направления
            if direction == "Русский → Кетский":
                prompt = f"Переведи слово '{word}' с русского на кетский язык. Предоставь только правильные варианты перевода."
            else:
                prompt = f"Переведи слово '{word}' с кетского на русский язык. Предоставь только правильные варианты перевода."

            # Вызов OpenAI API для получения перевода
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Ты переводчик между русским и кетским языками. Тебе нужно писать только варианты переводов и ничего больше. Вот примеры {ru: август, ket: августәип}, {ru: август, ket: даанәип}, {ru: август, ket: ульбънна әип}, {ru: автобус, ket: автобус}, {ru: автомобиль, ket: автомобиль}, {ru: адрес, ket: адрес}, {ru: азбука, ket: азбука}, {ru: аккуратный, ket: тъәиен}, {ru: аккуратная, ket: тъәиен}, {ru: аккуратное, ket: тъәиен}, {ru: рыба, ket: ись}"},
                    {"role": "user", "content": prompt}
                ]
            )

            # Извлечение ответа
            translation = response.choices[0].message.content.strip()

            # Отображение результатов
            st.subheader("Варианты перевода:")
            st.write(translation)

        except Exception as e:
            st.error(f"Произошла ошибка при получении перевода: {e}")
