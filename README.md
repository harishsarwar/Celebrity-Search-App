-------Celebrity Search App------

This project is a Streamlit application that interacts with a language model from HuggingFace to provide information about celebrities. Users can input a celebrity's name, and the app generates details about the person, their date of birth, and major world events that happened around their birth date.


Features

Language Model Integration: Uses the HuggingFace model for generating text-based outputs.

Conversational Memory: Stores conversations using LangChain's memory modules.

Dynamic Prompting: Utilizes multiple prompts to sequentially fetch information.

Streamlit Interface: Provides a user-friendly interface to interact with the model.



Application Flow

User Input: The user enters a celebrity's name.

LLM Processing:

Fetches basic information about the celebrity.

Determines the date of birth.

Lists five major events that happened around the celebrity's birth date.

Display Results:

Shows the fetched information along with conversational memory logs.


Dependencies

Streamlit: For building the web interface.

LangChain: For memory management and chaining prompts.

HuggingFace Endpoint: To interact with the language model.



Example Output

Input: "Albert Einstein"

Output:

Information about Albert Einstein.

His date of birth.

Major events around his birth year.