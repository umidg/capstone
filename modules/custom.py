import os
import pickle
import torch
from modules.custom_model import GPTConfig, GPT

# Function to load the GPT model from a checkpoint file
def load_model(checkpoint_path, device='cpu'):
    # Load checkpoint file
    checkpoint = torch.load(checkpoint_path)
    # Extract model arguments and state dictionary from checkpoint
    model_args = checkpoint['model_args']
    state_dict = checkpoint['model']
    
    # Create GPT configuration from model arguments
    gpt_configuration = GPTConfig(**model_args)
    # Initialize GPT model with the configuration
    gpt_model = GPT(gpt_configuration)
    # Load model state dictionary
    gpt_model.load_state_dict(state_dict)
    # Move model to specified device (CPU or GPU)
    gpt_model.to(device)

    return gpt_model

# Function to load meta information (stoi and itos) from a pickle file
def load_meta_info(meta_path):
    with open(meta_path, 'rb') as file:
        meta_info = pickle.load(file)
    return meta_info

# Function to encode text using character-to-index mapping (stoi)
def encode_text(text, stoi):
    return [stoi[char] for char in text]

# Function to decode list of token IDs into text using index-to-character mapping (itos)
def decode_text(list_of_ids, itos):
    return ''.join([itos[i] for i in list_of_ids])

# Function to generate text based on input data using the GPT model
def generate_text(input_data, gpt_model, max_tokens=800, temp=0.5, top_k_tokens=800):
    output_data = gpt_model.generate(input_data, max_tokens, temperature=temp, top_k=top_k_tokens)
    return output_data[0].tolist()

# Function to clean up the generated cover letter text
def clean_cover_letter(output_data, input_prompt):
    dear_index = output_data.find("Dear")
    sincerely_index = output_data.find("Sincerely")
    
    if dear_index != -1:
        cleaned_cover_letter = output_data[dear_index:sincerely_index + 20]
        if cleaned_cover_letter != '':
            return cleaned_cover_letter
        else:
            return output_data[dear_index:].replace(input_prompt, '')
    return output_data.replace(input_prompt, '')

# Main function to generate the cover letter
def generate_cover_letter(input_prompt):
    # Paths to checkpoint file and meta pickle file
    output_dir = 'modules/output_data_store'
    checkpoint_path = os.path.join(output_dir, 'ckpt.pt')
    meta_path = 'modules/data/model_datasets/meta.pkl'

    # Device specification (CPU or GPU)
    device = torch.device('cpu')

    # Load GPT model from checkpoint
    gpt_model = load_model(checkpoint_path, device)
    # Load meta information (stoi and itos) from meta pickle file
    meta_info = load_meta_info(meta_path)
    stoi, itos = meta_info['stoi'], meta_info['itos']

    # Encode input prompt into token IDs
    input_data = torch.tensor(encode_text(input_prompt, stoi), dtype=torch.long, device=device)[None, ...]
    # Generate text based on input prompt using the GPT model
    output_data = generate_text(input_data, gpt_model)
    # Decode generated token IDs into text
    decoded_output = decode_text(output_data, itos)

    # Clean up the generated cover letter text
    return clean_cover_letter(decoded_output, input_prompt)
