from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate(
    messages = [
        ##(role, message)
        ("system", """
            1. You are a Helpful Chatbot AI Assistant for human.
            2. Please Answer for the following question based on following context.
            3. If you can't find the information for the question from the context,
            4. Please tell me "I don't know".
            5. Please Answer in korean.
         
            # Context
            {context}
          """),
        ("human", "# Question \n {question}")
    ]
)