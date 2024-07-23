import streamlit as st
import random

# 英単語のクイズデータ
quiz_data = [
    {'word': 'apple', 'meaning': 'りんご'},
    {'word': 'car', 'meaning': '車'},
    {'word': 'computer', 'meaning': 'コンピュータ'},
    # 他のクイズデータも追加可能
]

# 英単語ガチャのデータ
gacha_words = [
    'apple', 'banana', 'orange', 'grape', 'melon',
    'car', 'bus', 'train', 'bicycle', 'motorcycle',
    'computer', 'phone', 'tablet', 'keyboard', 'mouse'
]

def main():
    st.title('英単語クイズとガチャアプリ')

    # クイズの表示
    quiz_index = st.radio('問題を選んでください', range(len(quiz_data)))
    question = quiz_data[quiz_index]['word']
    answer = quiz_data[quiz_index]['meaning']
    user_answer = st.text_input('次の英単語の意味は何ですか？', '')

    if st.button('回答する'):
        if user_answer.lower() == answer.lower():
            st.success('正解です！')
            st.write('英単語ガチャを引いてみましょう！')
            draw_gacha = st.button('英単語ガチャを引く')
            if draw_gacha:
                random_word = random.choice(gacha_words)
                st.write(f'ガチャで選ばれた英単語: {random_word}')
        else:
            st.error('不正解です。もう一度挑戦してください。')

if __name__ == '__main__':
    main()
