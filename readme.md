# Streamlit Cheat Sheet

Streamlit is an open-source Python library for creating web applications. This cheat sheet provides quick reference code snippets.

## 1. Installation
```python
pip install streamlit
```

## 2. Running a Streamlit Application
```bash
streamlit run your_script.py
```

## 3. Import Streamlit
```python
import streamlit as st
```

## 4. Text Elements

### Display text
```python
st.text("Hello Streamlit!")
```

### Display markdown
```python
st.markdown("# This is a markdown header")
```

### Display header
```python
st.header("This is a header")
```

### Display subheader
```python
st.subheader("This is a subheader")
```

## 5. Data Display

### Display a dataframe
```python
st.dataframe(dataframe)
```

### Display a table
```python
st.table(dataframe)
```

## 6. Widgets

### Button
```python
if st.button("Press me"):
    st.write("Button pressed!")
```

### Checkbox
```python
if st.checkbox("Check me out"):
    st.write("Checkbox is checked")
```

### Radio buttons
```python
option = st.radio("Choose an option", ('Option 1', 'Option 2'))
st.write(f"You selected {option}")
```

### Selectbox
```python
option = st.selectbox("Choose an option", ['Option 1', 'Option 2'])
st.write(f"You selected {option}")
```

### Multiselect
```python
options = st.multiselect("Select options", ['Option 1', 'Option 2', 'Option 3'])
st.write("You selected:", options)
```

### Slider
```python
value = st.slider("Select a value", 0, 100)
st.write(f"You selected {value}")
```

### Text input
```python
text = st.text_input("Enter some text")
st.write(f"You entered {text}")
```

## 7. Layouts

### Columns
```python
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
with col2:
    st.header("Column 2")
```

### Expander
```python
with st.expander("See explanation"):
    st.write("Here is some explanation")
```

## 8. Display Charts

### Line Chart
```python
st.line_chart(data)
```

### Bar Chart
```python
st.bar_chart(data)
```

### Area Chart
```python
st.area_chart(data)
```

## 9. Display Media

### Image
```python
st.image(image, caption="Image caption")
```

### Video
```python
st.video(data)
```

### Audio
```python
st.audio(data)
```

## 10. Caching

### Cache function
```python
@st.cache
def load_data():
    # Load and return data
    pass
```

Remember, this is just a basic cheat sheet and Streamlit offers much more functionality!
