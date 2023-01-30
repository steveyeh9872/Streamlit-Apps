import streamlit as st

def main():
    st.title("Cover Letter Generator")

    # Get the user's personal information
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    address = st.text_input("Address")

    # Get the user's job information
    job_title = st.text_input("Job Title")
    company = st.text_input("Company")
    job_description = st.text_area("Job Description")

    # Get the user's preferences for the generated text
    length = st.slider("Length of Cover Letter (in words)", min_value=50, max_value=1000, value=200, step=50)
    tone = st.selectbox("Tone", ["Professional", "Friendly"])

    # Generate the cover letter
    prompt = (f"Write a {tone.lower()} cover letter for the position of {job_title} at {company}. Use the following personal information: {name}, {email}, {phone}, {address}. Use the following job information: {job_description}.")
    #cover_letter = generate_text(prompt, "text-davinci-002", length)

    # Display the cover letter
    st.write("Here is your cover letter:")
    #st.write(cover_letter)

    # Allow the user to download the cover letter
    if st.button("Download Cover Letter"):
        st.text("Your cover letter is downloading...")
        file_name = name + "_cover_letter.txt"
        with open(file_name, "w") as f:
            f.write(prompt)
        st.success("Cover letter saved as " + file_name)

if __name__ == "__main__":
    main()