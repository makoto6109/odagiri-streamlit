from posixpath import expanduser
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit入門')
#プログレスバーの表示
st.write('プログレスバーの表示')
'Start!!' 

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'    




st.write('DataFrame')


#データフーレーム
df= pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})


st.write('動的なフレーム')

st.dataframe(df.style.highlight_max(axis=0)) #動的なフレーム
st.write('静的なフレーム')

st.table(df.style.highlight_max(axis=0)) #静的なフレーム

#テキスト記入方法↓
"""           
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```


"""


#折れ線グラフ

st.write('折れ線グラフ')
df= pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

#マップ表示
df= pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

#画像を表示
st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('uyuni1.jpg')
    st.image(img, caption='ウユニ湖', use_column_width=True)


#ウィジット（セレクトボックスによる、値の動的変更）
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたの好きな数字は、', option,'です。'

#カラムの作成
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')



#expanderの追加
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ回答1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ回答2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ回答3')

#テキスト入力による動的変更(st.sidebarつけることも可)
st.write('Interactive Widgets')
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味 :', text


#スライダーによる動的変更
condistion = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション:', condistion









