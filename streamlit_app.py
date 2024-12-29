import streamlit as st
from openai import OpenAI

st.title("Русско-Кетский и Кетско-Русский Переводчик")

# Выбор направления перевода
direction = st.selectbox(
    "Выберите направление перевода",
    ("Русский → Кетский", "Кетский → Русский")
)

# Ввод слова для перевода
word = st.text_input("Введите слово для перевода:")
client = OpenAI(
  api_key="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"
)

if st.button("Перевести") and word:
        # Определение целевого языка на основе направления
        if direction == "Русский → Кетский":
            prompt = f"Переведи слово '{word}' с русского на кетский язык. Предоставь только правильные варианты перевода."
        else:
            prompt = f"Переведи слово '{word}' с кетского на русский язык. Предоставь только правильные варианты перевода."

        # Вызов OpenAI API для получения перевода

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": "Ты переводчик между русским и кетским языками. Тебе нужно писать только варианты переводов и ничего больше. Вот примеры {ru: август, ket: августәип}, {ru: август, ket: даанәип}, {ru: август, ket: ульбънна әип}, {ru: автобус, ket: автобус}, {ru: автомобиль, ket: автомобиль}, {ru: адрес, ket: адрес}, {ru: азбука, ket: азбука}, {ru: аккуратный, ket: тъәиен}, {ru: аккуратная, ket: тъәиен}, {ru: аккуратное, ket: тъәиен}, {ru: рыба, ket: ись}"},
                {"role": "user", "content": prompt}
            ]
        )
        print(response.choices[0].message)

        # Извлечение ответа
        translation = response.choices[0].message.content

        # Отображение результатов
        st.subheader("Варианты перевода:")
        st.write(translation)

