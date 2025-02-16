import streamlit as st

# Set page config for a wider layout
st.set_page_config(
    page_title="Slow Mover Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 1rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 20px;
    }
    .title-container {
        background-color: black;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 2rem;
    }
    .main-title {
        text-align: center;
        color: white;
        font-size: 3em;
        font-weight: bold;
        margin: 0;
        padding: 0;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Add main title with container
    st.markdown("<div class='title-container'><h1 class='main-title'>Codeworks ML</h1></div>", unsafe_allow_html=True)
    
    st.title("🚛 Slow Mover Item Prediction")
    st.markdown("---")
    
    # Create two columns for input fields
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Item Details")
        item = st.text_input("Item Code", value="0015804")
        cqty = st.number_input("CQTY (Current Quantity)", 
                              value=4125668.0,
                              format="%.2f")
        uom = st.text_input("UOM (Unit of Measure)", value="CS")
        tqty = st.number_input("TQTY (Total Quantity)", 
                              value=1116.0,
                              format="%.2f")
    
    with col2:
        st.subheader("Additional Information")
        twght = st.number_input("TWGHT (Total Weight)", 
                               value=4017.64,
                               format="%.2f")
        lot1 = st.text_input("LOT1", value="VDHPE01-B047A")
        lot2 = st.text_input("LOT2", value="20250216")
        lot3 = st.text_input("LOT3", value="B047250216")

    # Center the predict button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_button = st.button("🔍 Predict", use_container_width=True)

    if predict_button:
        if item and uom and lot1 and lot2 and lot3:
            # Add a spinner while predicting
            with st.spinner('Analyzing item...'):
                from model_prediction import predict_slow_mover
                prediction = predict_slow_mover(
                    item, cqty, uom, tqty, twght, lot1, lot2, lot3
                )
            
            if prediction is not None:
                st.markdown("---")
                st.subheader("📊 Prediction Result")
                if prediction == 1:
                    st.error("🚨 This item is predicted to be a SLOW MOVER")
                    st.markdown("""
                        **Recommendation:**
                        - Consider reviewing inventory levels
                        - Evaluate pricing strategy
                        - Check for seasonal patterns
                    """)
                else:
                    st.success("✅ This item is predicted to NOT be a slow mover")
                    st.markdown("""
                        **Status:**
                        - Regular movement pattern detected
                        - Current inventory strategy seems effective
                    """)
            else:
                st.error("⚠️ An error occurred during prediction. Please check the inputs.")
        else:
            st.warning("⚠️ Please fill in all required fields.")

    # Add helpful information at the bottom
    with st.expander("ℹ️ Help"):
        st.markdown("""
            **Input Field Descriptions:**
            - **Item Code**: Unique identifier for the item
            - **CQTY**: Current quantity in stock
            - **UOM**: Unit of Measure (e.g., CS for Case)
            - **TQTY**: Total quantity
            - **TWGHT**: Total weight
            - **LOT1-3**: Lot identification numbers
        """)

if __name__ == "__main__":
    main()