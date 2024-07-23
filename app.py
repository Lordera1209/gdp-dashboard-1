import streamlit as st

# 设置页面标题
st.title('简易计算器')

# 添加文本输入框用于输入数字
num1 = st.number_input('请输入第一个数字:')
num2 = st.number_input('请输入第二个数字:')

# 添加下拉框选择运算符
operator = st.selectbox('选择运算符:', ['+', '-', '*', '/'])

# 定义计算逻辑
if st.button('计算'):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = '除数不能为0！'
    st.write('Result:', result)
