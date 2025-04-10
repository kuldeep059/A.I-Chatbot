import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK data (run this once)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Download punkt_tab resource
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

responses = {
    "what services do you offer": "We offer a range of tech services including Website Designing, Printer Service and Renting, Computer Service and Renting, Customized PC Builds, Laptop Service and Sales, and Social Media Handling.",
    "what are your services": "We offer a range of tech services including Website Designing, Printer Service and Renting, Computer Service and Renting, Customized PC Builds, Laptop Service and Sales, and Social Media Handling.",
    "tell me about your services": "We offer a range of tech services including Website Designing, Printer Service and Renting, Computer Service and Renting, Customized PC Builds, Laptop Service and Sales, and Social Media Handling.",
    "do you offer website designing": "Yes, we offer professional website designing services. Tell us more about your needs!",
    "i need a website designed": "Yes, we offer professional website designing services. Tell us more about your needs!",
    "do you provide printer service": "Yes, we provide both printer service and printer renting options. What are you looking for?",
    "can i rent a printer from you": "Yes, we provide both printer service and printer renting options. What are you looking for?",
    "do you offer computer service": "Yes, we offer comprehensive computer services and also have computers available for rent. What can we help you with?",
    "can i rent a computer": "Yes, we offer comprehensive computer services and also have computers available for rent. What can we help you with?",
    "do you build custom pcs": "Absolutely! We specialize in building customized PCs tailored to your specific requirements and budget. Tell us what you need.",
    "i want a customized pc": "Absolutely! We specialize in building customized PCs tailored to your specific requirements and budget. Tell us what you need.",
    "do you service laptops": "Yes, we offer both laptop repair services and have a selection of laptops for sale. What can we assist you with today?",
    "do you sell laptops": "Yes, we offer both laptop repair services and have a selection of laptops for sale. What can we assist you with today?",
    "do you handle social media": "Yes, we provide social media handling services to help you manage and grow your online presence.",
    "i need help with social media": "Yes, we provide social media handling services to help you manage and grow your online presence.",
    "how can i contact you": "You can contact us via email at [email address removed] or by phone at +91-XXXXXXXXXX.",
    "what's your contact information": "You can contact us via email at [email address removed] or by phone at +91-XXXXXXXXXX.",
    "hello": "Hello! How can I assist you with our services today?",
    "hi": "Hello! How can I assist you with our services today?",
    "hey": "Hello! How can I assist you with our services today?",
    "bye": "Goodbye! Feel free to reach out if you have more questions.",
    "goodbye": "Goodbye! Feel free to reach out if you have more questions.",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
    "i want a customized pc with": "Tell us more about the components you'd like for your custom PC.",
    "build a custom pc with": "Tell us more about the components you'd like for your custom PC.",
    "custom pc for": "Tell us more about what you need your custom PC for.",
    "what's the cost": "Could you please specify which service you are interested in?", # Generic response for cost
}

synonyms = {
    "guys": "you",
    "provide": "offer",
    "do": "",
    "know if": "",
    "help with": "handle",
    "about": "",
    "your company": "you",
    "designing": "design",
    "pcs": "pc",
    "service": "services",
    "rent": "renting",
    "sell": "sales",
    "want": "need",
    "with": "",
    "cost": "price",
    "'s": " is"
}

previous_intent = None # Variable to store the last identified intent

def preprocess_input(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    processed_tokens = [synonyms.get(token, token) for token in tokens]
    return " ".join(processed_tokens)

def simple_chatbot(user_input):
    global previous_intent
    processed_input = preprocess_input(user_input)
    user_tokens = set(word_tokenize(processed_input))
    identified_intent = None

    for pattern, response in responses.items():
        processed_pattern = preprocess_input(pattern)
        pattern_tokens = set(word_tokenize(processed_pattern))
        common_tokens = user_tokens.intersection(pattern_tokens)

        if "custom" in pattern_tokens and "pc" in pattern_tokens:
            remaining_tokens = [token for token in word_tokenize(user_input.lower()) if token not in pattern_tokens and token not in synonyms and len(token) > 2]
            if remaining_tokens and len(common_tokens) >= len(pattern_tokens) * 0.5:
                identified_intent = "custom_pc_inquiry"
                pc_components = ", ".join(remaining_tokens).strip()
                if pc_components:
                    return response.replace("the components you'd like", pc_components).replace("what you need your custom PC for", f"your requirements like {pc_components}")
                else:
                    return response
        elif len(common_tokens) >= len(pattern_tokens) * 0.6:
            identified_intent = pattern.replace("do you ", "").replace("i want to ", "").replace("can i ", "").replace("what is the ", "").replace("tell me about ", "").replace("how can i ", "").replace("what's your ", "").replace("build a ", "").replace("custom pc for ", "").strip()
            return response

    if "cost" in user_tokens or "price" in user_tokens:
        if previous_intent == "website designing":
            return "The cost for website designing varies greatly depending on the complexity and features. Could you provide more details about your requirements?"
        elif previous_intent == "printer renting":
            return "Printer rental costs depend on the type of printer and the rental duration. What kind of printer are you looking for and for how long?"
        elif previous_intent == "custom_pc_inquiry":
            return "The cost of a custom PC depends entirely on the components you choose. Once you specify your requirements, we can provide an estimate."
        else:
            return responses.get("what's the cost", "Could you please specify which service you are interested in?")

    previous_intent = identified_intent
    return responses.get(processed_input, "I'm sorry, I don't understand your question. Could you please rephrase it?")

# The interactive loop is removed here