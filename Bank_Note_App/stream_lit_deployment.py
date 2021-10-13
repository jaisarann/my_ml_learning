# Import required packages
import pickle
import streamlit as st

print('Normal code calling...')
# Open model pickle file
pickle_in = open("rf_bank_note_classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


def Predict_Bank_Note(variance, skewness, curtosis, entropy):
    print('Variance : ', variance)
    print('skewness : ', skewness)
    print('curtosis : ', curtosis)
    print('entropy : ', entropy)
    result = classifier.predict([[variance, skewness, curtosis, entropy]])
    # print("Prediction : ", result)
    return result


def main():
    st.title("Bank Note Authentification")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align=center;">
    Streamlit Bank Authenticator App
    </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance", "Type Here")
    skewness = st.text_input("skewness", "Type Here")
    curtosis = st.text_input("curtosis", "Type Here")
    entropy = st.text_input("entropy", "Type Here")

    # predict result
    result = ""
    if st.button("Predict"):
        # result = PredictAuthentication(variance, skewness,curtosis,entropy)
        result = Predict_Bank_Note(variance, skewness, curtosis, entropy)

    st.success("The resuls it : {}".format(result))
    if st.button("About"):
        st.text("This is Bank Note Applicaiton")
        st.text("Built using Streamlit")


if __name__ == "__main__":
    main()
