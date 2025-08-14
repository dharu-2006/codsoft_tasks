import re
import random

class RuleBasedChatbot:
    def __init__(self):
        # Define response patterns with multiple variations for better accuracy
        self.patterns = {
            # Greetings
            r'\b(hello|hi|hey|greetings|good morning|good afternoon|good evening)\b': [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! Nice to meet you. How may I assist you?"
            ],
            
            # How are you
            r'\b(how are you|how\'s it going|how do you do|what\'s up)\b': [
                "I'm doing great, thank you for asking! How are you?",
                "I'm functioning perfectly! How about you?",
                "All systems running smoothly! How can I help you today?"
            ],
            
            # Name questions
            r'\b(what is your name|what\'s your name|who are you|your name)\b': [
                "I'm a rule-based chatbot created to help you!",
                "You can call me ChatBot. I'm here to assist you!",
                "I'm your friendly AI assistant. What would you like to know?"
            ],
            
            # Help requests
            r'\b(help|assist|support|can you help)\b': [
                "I'm here to help! I can answer questions, have conversations, and provide information.",
                "Of course! I can assist with various topics. What do you need help with?",
                "I'd be happy to help! What can I do for you?"
            ],
            
            # Thank you
            r'\b(thank you|thanks|appreciate|grateful)\b': [
                "You're very welcome!",
                "Happy to help!",
                "My pleasure! Anything else I can do for you?"
            ],
            
            # Weather (basic)
            r'\b(weather|temperature|rain|sunny|cloudy)\b': [
                "I don't have access to real-time weather data, but you can check a weather app or website!",
                "For current weather information, I'd recommend checking your local weather service.",
                "I wish I could tell you the weather, but I don't have that capability yet!"
            ],
            
            # Time
            r'\b(time|what time|current time|clock)\b': [
                "I don't have access to real-time clock data. Please check your device's clock!",
                "You can check the time on your computer or phone.",
                "I can't tell time, but your device surely can!"
            ],
            
            # Goodbye
            r'\b(bye|goodbye|see you|farewell|take care|exit|quit)\b': [
                "Goodbye! Have a wonderful day!",
                "See you later! Take care!",
                "Farewell! It was nice talking with you!"
            ],
            
            # Yes/No responses
            r'\b(yes|yeah|yep|sure|okay|ok)\b': [
                "Great! How can I help you further?",
                "Excellent! What would you like to do next?",
                "Perfect! Let me know if you need anything else."
            ],
            
            r'\b(no|nope|not really|nah)\b': [
                "That's okay! Is there something else I can help you with?",
                "No problem! What else would you like to talk about?",
                "Alright! Feel free to ask me anything else."
            ],
            
            # Capabilities
            r'\b(what can you do|your capabilities|features)\b': [
                "I can have conversations, answer basic questions, and respond to various topics!",
                "I'm designed to chat with you and provide helpful responses based on what you say.",
                "I can engage in conversations and try to help with information and support!"
            ]
        }
        
        # Default responses for unmatched inputs
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "That's interesting! Tell me more about it.",
            "I don't have a specific response for that, but I'm here to chat!",
            "Could you please elaborate on that?",
            "I'm still learning! Can you ask me something else?"
        ]
    
    def preprocess_input(self, user_input):
        """Clean and normalize user input for better pattern matching"""
        # Convert to lowercase
        processed = user_input.lower().strip()
        # Remove extra whitespace
        processed = re.sub(r'\s+', ' ', processed)
        # Remove punctuation at the end
        processed = re.sub(r'[.!?]+$', '', processed)
        return processed
    
    def get_response(self, user_input):
        """Generate response based on pattern matching"""
        processed_input = self.preprocess_input(user_input)
        
        # Check each pattern
        for pattern, responses in self.patterns.items():
            if re.search(pattern, processed_input, re.IGNORECASE):
                return random.choice(responses)
        
        # Return default response if no pattern matches
        return random.choice(self.default_responses)
    
    def chat(self):
        """Main chat loop"""
        print(" ChatBot: Hello! I'm a rule-based chatbot. Type 'quit' or 'bye' to exit.")
        print("=" * 60)
        
        while True:
            try:
                user_input = input("\n You: ").strip()
                
                if not user_input:
                    print(" ChatBot: Please say something!")
                    continue
                
                # Check for exit commands
                if re.search(r'\b(quit|exit|bye|goodbye)\b', user_input.lower()):
                    print(" ChatBot: Goodbye! Have a great day!")
                    break
                
                response = self.get_response(user_input)
                print(f" ChatBot: {response}")
                
            except KeyboardInterrupt:
                print("\n ChatBot: Goodbye! Have a great day!")
                break
            except Exception as e:
                print(f" ChatBot: Sorry, I encountered an error: {e}")

def main():
    """Main function to run the chatbot"""
    chatbot = RuleBasedChatbot()
    chatbot.chat()

if __name__ == "__main__":
    main()
