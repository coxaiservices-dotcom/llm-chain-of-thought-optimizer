import streamlit as st

# Configure page
st.set_page_config(page_title="CoT Generator", page_icon="🧠")

# Title
st.title("🧠 Chain-of-Thought Prompt Generator")
st.write("Transform simple prompts into structured, reasoning-enhanced versions")

# Input section
st.subheader("Input Your Prompt")

# Sample prompts
samples = {
    "Math": "Calculate 15% tip on a $45 bill",
    "Coding": "Write a function to reverse a string", 
    "Analysis": "Compare iPhone vs Android",
    "Decision": "Should I buy or rent a house?"
}

# Sample selector
sample_choice = st.selectbox("Try a sample:", ["None"] + list(samples.keys()))

# Get the prompt
if sample_choice != "None":
    prompt = st.text_area("Your prompt:", value=samples[sample_choice], height=100)
else:
    prompt = st.text_area("Your prompt:", height=100, placeholder="Enter your prompt here...")

# Process button
if st.button("Generate Enhanced Prompt", type="primary"):
    if prompt.strip():
        # Simple enhancement
        enhanced = f"""Original task: {prompt}

Let's think through this step by step:

1. First, I'll understand what we're trying to accomplish
2. Then, I'll consider the key factors and requirements  
3. Next, I'll think through different approaches
4. Finally, I'll provide a clear, well-reasoned response

Please work through each step methodically before giving your final answer."""

        st.subheader("Enhanced Prompt")
        st.text_area("Copy this:", value=enhanced, height=200)
        
        st.subheader("What Changed")
        st.success("✅ Added structured thinking steps")
        st.success("✅ Encouraged methodical reasoning")
        st.success("✅ Improved response quality guidance")
        
        # Quick stats
        original_words = len(prompt.split())
        enhanced_words = len(enhanced.split())
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Original", f"{original_words} words")
        col2.metric("Enhanced", f"{enhanced_words} words") 
        col3.metric("Added", f"+{enhanced_words - original_words} words")
        
    else:
        st.warning("Please enter a prompt first!")

# Footer
st.markdown("---")
st.write("🎯 **How it works:** Adds chain-of-thought reasoning structure to improve AI response quality")