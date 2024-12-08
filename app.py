import streamlit as st

from plot import first_plot
from scatter import second_plot
from pie import third_plot
from heatmap import fourth_plot
from bar import fifth_plot
from plot3d import seventh_plot

st.title("Lab 4")
st.sidebar.title('Graphics')
action = st.sidebar.radio('Select graphic', ['Plot', 'Scatter', 'Pie', 'Heatmap', 'Bar', '3D Plot'])

if action == 'Plot':
    st.header('Plot')
    #First plot
    b = st.slider("Choose a value b", -10, 10)
    st.write(f"The b is {b}")

    y = st.slider("Choose a value y", -10, 10)
    st.write(f"The y is {y}")
    try:
        st.pyplot(first_plot(b,y))
    except:
        st.text("The bad arguments. Try again.")

elif action == 'Scatter':
    st.header('Scatter')
    #Second plot
    try:
        st.pyplot(second_plot())
    except:
        st.text("Something went wrong. Try again")

elif action == 'Pie':
    st.header('Pie')
    # Third plot
    try:
        st.pyplot(third_plot())
    except:
        st.text("Something went wrong. Try again")

elif action == 'Heatmap':
    st.header('Heatmap')
    # Fourth plot
    try:
        st.pyplot(fourth_plot())
    except:
        st.text("Something went wrong. Try again")

elif action == 'Bar':
    st.header('Bar')
    # Fifth plot
    try:
        st.pyplot(fifth_plot())
    except:
        st.text("Something went wrong. Try again")

elif action == '3D Plot':
    st.header('3D Plot')
    # Seventh plot
    try:
        st.pyplot(seventh_plot())
    except:
        st.text("Something went wrong. Try again")