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

