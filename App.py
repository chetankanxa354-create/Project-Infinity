import streamlit as st

# तिम्रो एपको टाइटल
st.title("Project-Infinity: Cosmic Simulation Engine")

# एउटा सानो स्लाइडर
entropy = st.slider("इन्ट्रोपी (Entropy) स्तर छान्नुहोस्:", 0, 100)

# बटम लजिक
if st.button("सिमुलेट गर्नुहोस्"):
    st.write(f"सिमुलेशन चलिरहेको छ... हालको इन्ट्रोपी: {entropy}")
    if entropy > 70:
        st.error("सावधानी: उच्च इन्ट्रोपी! सिस्टम रिसेट गर्नुपर्छ।")
    else:
        st.success("सिस्टम स्थिर छ। सबै ठिक छ!")
