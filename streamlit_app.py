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
                {"role": "user", "content": "Ты переводчик между русским и кетским языками. Тебе нужно писать только варианты переводов и ничего больше."},
                {"role": "user", "content": prompt}
            ]
        )
        print(response.choices[0].message)

        # Извлечение ответа
        translation = response.choices[0].message.content

        # Отображение результатов
        st.subheader("Варианты перевода:")
        st.write(translation)

