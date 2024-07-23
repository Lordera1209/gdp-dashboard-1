import streamlit as st

# 设置页面标题
st.title('Simple Calculator')

# 添加文本输入框用于输入数字
num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')

# 添加下拉框选择运算符
operator = st.selectbox('Select an operator:', ['+', '-', '*', '/'])

# 定义计算逻辑
if st.button('Calculate'):
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
            result = 'Division by zero is undefined'
    st.write('Result:', result)
