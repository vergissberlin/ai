import Testing
model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
test_path = 'Data/Test'

model = load_model(model_path)
model.load_weights(model_weights_path)
st.sidebar.title("Predict New Images")
imageselect = st.sidebar.selectbox("Pick an image.", onlyfiles)
if st.sidebar.button('Predict Animal'):
    prediction = Testing.predict((model),"C:/Users/Luke/Desktop/StreamlitDemo/Data/Test/" + imageselect)
