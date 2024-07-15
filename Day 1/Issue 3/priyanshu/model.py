import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
import os
import tkinter as tk
from tkinter import scrolledtext
import threading

# Expanded dataset (same as before)
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "greetings"],
    "farewell": ["goodbye", "bye", "see you later", "take care", "have a good day"],
    "thanks": ["thank you", "thanks", "appreciate it", "thank you so much", "thanks a lot"],
    "help": ["help", "can you help me", "I need assistance", "support please", "can you assist", "how can you help me"],
    "about_open": ["tell me about OPEN", "what is OPEN Community", "who are you", "what do you do"],
    "projects": ["what projects do you have", "tell me about your projects", "open source projects", "github repositories"],
    "sponsorship": ["how can I sponsor OPEN", "sponsorship opportunities", "become a sponsor", "support OPEN financially"],
    "events": ["what events do you organize", "upcoming events", "past events", "workshops"],
    "specific_event": ["tell me about RPA 3.0", "what was TECHNOVA", "details of OPEN Summer of Code"],
    "get_involved": ["how can I join OPEN", "volunteer opportunities", "become a member", "contribute to OPEN"],
    "contact": ["how can I contact OPEN", "get in touch", "contact information", "reach out to OPEN"],
    "open_source": ["what is open source", "benefits of open source", "why open source is important"],
    "skills": ["what skills can I learn", "skill development", "improve my skills with OPEN"],
    "community": ["tell me about the OPEN community", "community activities", "community benefits"],
    "specific_project": [
        "tell me about AUTO-INFIRMARY", "what is OPEN-CHAT-BOT", "explain LOST-AND-FOUND-MOBILE-APP",
        "describe BUS-TRACKING-SYSTEM", "what is ANALYSIS-OF-PRODUCTS-USING-NLP",
        "explain DOCUMENT-STORAGE-IPFS", "tell me about GRAPH-GENERATOR",
        "what is MEDIAMORPH", "describe MEETINGMINUTES-MOM-GENERATOR",
        "explain OMUSIGATOR", "what is ONE-STOP-SOLUTION"
    ],
}

responses = {
    "greeting": "Hello! Welcome to the OPEN Community chatbot. How can I assist you today?",
    "farewell": "Thank you for chatting with us. Have a great day and keep supporting open source!",
    "thanks": "You're welcome! We appreciate your interest in OPEN Community. Is there anything else I can help you with?",
    "help": "I'd be happy to help! I can provide information about OPEN Community, our projects, events, sponsorship opportunities, and how to get involved. What specific information are you looking for?",
    "about_open": "OPEN Community aims to spread awareness about the advantages of open software. We provide support and mentorship to students working on open source projects, fostering innovation and skill development. Our community offers a holistic environment to explore, ideate, and create solutions to real-world problems.",
    "projects": "OPEN Community has numerous exciting projects! Some of our top repositories include AUTO-INFIRMARY, BUS-TRACKING-SYSTEM, LOST-AND-FOUND-MOBILE-APP, and OPEN-CHAT-BOT. You can find all our projects on our GitHub page. Would you like more details about a specific project?",
    "sponsorship": "We welcome sponsorships to support our community initiatives! Sponsoring OPEN Community helps us organize events, maintain our projects, and provide resources to our members. Please contact our sponsorship team for more details on how you can support us.",
    "events": "OPEN Community organizes various events throughout the year, including workshops, webinars, and coding competitions. Some of our past events include RPA 3.0, TECHNOVA, and OPEN Summer of Code. Would you like information about upcoming events or details about a specific past event?",
    "specific_event": "Certainly! I can provide information about specific events. Which event would you like to know more about?",
    "get_involved": "There are many ways to get involved with OPEN Community! You can contribute to our open source projects on GitHub, participate in our events, or become a community member. Visit our website for more information on how to join and contribute.",
    "contact": "You can reach out to OPEN Community through our official website or social media channels. For specific inquiries, you can also email us at contact@opencommunity.org (this is a fictional email for demonstration).",
    "open_source": "Open source refers to software whose source code is freely available for anyone to view, modify, and distribute. It promotes collaboration, transparency, and innovation in software development. OPEN Community supports and encourages open source development to benefit society and enhance skills.",
    "skills": "By participating in OPEN Community, you can develop various skills including programming, project management, teamwork, and communication. Our projects and events cover a wide range of technologies, allowing you to enhance your technical and soft skills.",
    "community": "The OPEN Community is a dynamic group of students, developers, and mentors passionate about open source. We organize events, collaborate on projects, and provide a supportive environment for learning and growth. Join us to connect with like-minded individuals and make a positive impact through technology!",
    "unknown": "I apologize, but I'm not sure I understood your request. Could you please rephrase or provide more details? I'm here to help with information about OPEN Community, our projects, events, and how to get involved.",
    "specific_project": "Which project would you like to know about? I can provide information on AUTO-INFIRMARY, OPEN-CHAT-BOT, LOST-AND-FOUND-MOBILE-APP, BUS-TRACKING-SYSTEM, ANALYSIS-OF-PRODUCTS-USING-NLP, DOCUMENT-STORAGE-IPFS, GRAPH-GENERATOR, MEDIAMORPH, MEETINGMINUTES-MOM-GENERATOR, OMUSIGATOR, and ONE-STOP-SOLUTION.",
    "AUTO-INFIRMARY": "AUTO-INFIRMARY is an app that allows you to book appointments for medical emergencies. It provides a list of available doctors, real-time traffic information, and first-aid guidance for emergencies.",
    "OPEN-CHAT-BOT": "OPEN-CHAT-BOT is a project aimed at creating a chatbot for OPEN's website. It helps visitors learn about the community's vision, purpose, and navigate through the website pages.",
    "LOST-AND-FOUND-MOBILE-APP": "The LOST-AND-FOUND-MOBILE-APP is designed for university use, simplifying the process of retrieving lost items. It allows users to browse through a list of recently found items, saving time and effort in locating lost valuables.",
    "BUS-TRACKING-SYSTEM": "The BUS-TRACKING-SYSTEM is an application that uses Google Maps and Flutter to track a driver's location and estimate the time a bus will take to reach the user's stop. It's currently in the development phase for its first version, which is a Minimum Viable Product (MVP).",
    "ANALYSIS-OF-PRODUCTS-USING-NLP": "This project is a platform that uses Natural Language Processing (NLP) to analyze product reviews. It helps businesses understand consumer acceptance, filter positive and negative reviews, and study market competition.",
    "DOCUMENT-STORAGE-IPFS": "DOCUMENT-STORAGE-IPFS is a secure blockchain platform for storing important documents using the InterPlanetary File System (IPFS) technology.",
    "GRAPH-GENERATOR": "GRAPH-GENERATOR is a Java-based project that visualizes mathematical equations or functions as 2D graphs.",
    "MEDIAMORPH": "MEDIAMORPH is a Chrome extension that enhances video player functionalities. It allows users to control video speed, adjust sound up to 200%, use OCR for copying text, interact with clickable video links, enable picture-in-picture mode, and provides video controls for YouTube shorts.",
    "MEETINGMINUTES-MOM-GENERATOR": "The MEETINGMINUTES-MOM-GENERATOR is a Google Chrome extension that automates the conversion of spoken language to written meeting minutes. It uses speech-to-text technology to generate comprehensive meeting summaries in both offline and online formats.",
    "OMUSIGATOR": "OMUSIGATOR is a web app built with HTML, CSS, and JS that allows users to transfer their playlists from Spotify to YouTube using Python and Google API.",
    "ONE-STOP-SOLUTION": "ONE-STOP-SOLUTION is an app that serves as a comprehensive resource for students, providing information about nearby restaurants, pharmacies, hostels, PGs, and doctors near the college campus. It includes details such as menus, phone numbers, and directions for each establishment."
}

# Prepare dataset
texts = []
labels = []
for intent, phrases in intents.items():
    for phrase in phrases:
        texts.append(phrase)
        labels.append(intent)

# Encode labels
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Define a custom Dataset
class CustomDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, item):
        text = self.texts[item]
        label = self.labels[item]

        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_len,
            return_token_type_ids=False,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt',
        )

        return {
            'text': text,
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(label, dtype=torch.long)
        }

# Initialize BERT model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=len(intents))

# Split data
train_texts, val_texts, train_labels, val_labels = train_test_split(
    texts, encoded_labels, test_size=0.2, random_state=42
)

# Create DataLoaders
train_dataset = CustomDataset(train_texts, train_labels, tokenizer, max_len=32)
val_dataset = CustomDataset(val_texts, val_labels, tokenizer, max_len=32)

train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=16, shuffle=False)

# Training parameters
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
optimizer = AdamW(model.parameters(), lr=2e-5, correct_bias=False)

# Training function
def train_epoch(model, data_loader, optimizer, device):
    model.train()
    total_loss = 0
    correct_predictions = 0

    for batch in data_loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)

        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels
        )

        loss = outputs.loss
        total_loss += loss.item()

        logits = outputs.logits
        _, preds = torch.max(logits, dim=1)
        correct_predictions += torch.sum(preds == labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    return correct_predictions.double() / len(data_loader.dataset), total_loss / len(data_loader)

# Validation function
def eval_model(model, data_loader, device):
    model.eval()
    total_loss = 0
    correct_predictions = 0

    with torch.no_grad():
        for batch in data_loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels
            )

            loss = outputs.loss
            total_loss += loss.item()

            logits = outputs.logits
            _, preds = torch.max(logits, dim=1)
            correct_predictions += torch.sum(preds == labels)

    return correct_predictions.double() / len(data_loader.dataset), total_loss / len(data_loader)

# Train the model
num_epochs = 200
for epoch in range(num_epochs):
    train_acc, train_loss = train_epoch(model, train_loader, optimizer, device)
    val_acc, val_loss = eval_model(model, val_loader, device)

    print(f'Epoch {epoch + 1}/{num_epochs}')
    print(f'Train loss: {train_loss}, Train accuracy: {train_acc}')
    print(f'Val loss: {val_loss}, Val accuracy: {val_acc}')

# Save the model
model_path = 'bert_intent_model.pt'
torch.save(model.state_dict(), model_path)

# Load the model (for inference)
model.load_state_dict(torch.load(model_path))

# Chatbot interface using tkinter
class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=60, height=20, font=("Helvetica", 14))
        self.text_area.grid(row=0, column=0, padx=10, pady=10)

        self.entry = tk.Entry(root, width=50, font=("Helvetica", 14))
        self.entry.grid(row=1, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", self.get_response)

        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name, num_labels=len(intents))
        self.model.load_state_dict(torch.load(model_path))
        self.model = self.model.to(device)

        self.label_encoder = label_encoder

    def get_response(self, event):
        user_input = self.entry.get()
        self.entry.delete(0, tk.END)
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.END, f"You: {user_input}\n")
        self.text_area.configure(state='disabled')

        # Process user input in a separate thread
        threading.Thread(target=self.process_user_input, args=(user_input,)).start()

    def process_user_input(self, user_input):
        inputs = self.tokenizer.encode_plus(
            user_input,
            add_special_tokens=True,
            max_length=32,
            return_token_type_ids=False,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt',
        )

        input_ids = inputs['input_ids'].to(device)
        attention_mask = inputs['attention_mask'].to(device)

        with torch.no_grad():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
        
        logits = outputs.logits
        _, prediction = torch.max(logits, dim=1)
        predicted_label = self.label_encoder.inverse_transform(prediction.cpu().numpy())[0]

        response = responses.get(predicted_label, responses["unknown"])

        self.text_area.configure(state='normal')
        self.text_area.insert(tk.END, f"Bot: {response}\n")
        self.text_area.configure(state='disabled')

# Run the chatbot application
root = tk.Tk()
app = ChatbotApp(root)
root.mainloop()
