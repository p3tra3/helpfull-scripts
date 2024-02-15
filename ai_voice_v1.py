import requests
import json
import os
import re
import uuid
import time
from pydub import AudioSegment
import io

# Configuration
polling_interval = 10  # Time in seconds to wait between polling attempts

# Voice tokens for characters
voice_m = 'TM:mcvca56k5d5e'
voice_ry = 'TM:ebgxj0j4fvzp'
voice_s = 'TM:ktwj3fa7ec4a'
voice_b = 'TM:kqt84ngj96jx'
voice_y = 'TM:7tdqxvg8kw5h'
voice_j = 'TM:pfwv9crn11gr'
voice_r = 'TM:ebgxj0j4fvzp'
#voice_t
#voice_n
#voice_



# Function to authenticate and get the session cookie
def authenticate(username, password):
    data = {
        'uuid_idempotency_token': str(uuid.uuid4()),
        'username_or_email': username,
        'password': password
    }
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post('https://api.fakeyou.com/v1/login', json=data, headers=headers)

    if response.status_code != 200 or not response.json().get('success'):
        print(f'Error authenticating: {response.text}')
        return None

    session_cookie = response.headers.get('set-cookie')
    return session_cookie

# Function to call the FakeYou API for TTS and poll for completion
def generate_voice(voice_token, text, index, base_filename, script_dir, session_cookie):
    # Define a dictionary to map voice_token to character
    character_mapping = {
        voice_m: 'm',
        voice_r: 'r',
        voice_r: 'ry',
        voice_r: 'rl',    
        voice_r: 'rm',
        voice_r: 'rr',
        voice_b: 'b',
        voice_s: 's',
        voice_y: 'y',
        voice_j: 'j',
        #voice_t: 't',
        #voice_n: 'n',
    }

    # Use the dictionary to determine the character based on voice_token
    character = character_mapping.get(voice_token, 'default_character')
    
    
    output_file = os.path.join(script_dir, f'{base_filename}_{character}_{index}.mp3')
    data = {
        'uuid_idempotency_token': str(uuid.uuid4()),
        'tts_model_token': voice_token,
        'inference_text': text
    }
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': session_cookie  # Include the session cookie for authentication
    }
    print(f'Submitting TTS request for line {index}: "{text}"')
    response = requests.post('https://api.fakeyou.com/tts/inference', json=data, headers=headers)

    if response.status_code != 200 or not response.json().get('success'):
        print(f'Error submitting voice generation request: {response.text}')
        return None

    job_token = response.json()['inference_job_token']
    print(f'Polling for TTS job completion (Job Token: {job_token})...')

    while True:
        job_status_response = requests.get(f'https://api.fakeyou.com/tts/job/{job_token}', headers=headers)
        
        if job_status_response.status_code != 200 or not job_status_response.json().get('success'):
            print(f'Error checking job status: {job_status_response.text}')
            return None

        job_status = job_status_response.json()['state']['status']
        print(f'Job Status: {job_status}')

        if job_status == 'complete_success':
            audio_path = job_status_response.json()['state']['maybe_public_bucket_wav_audio_path']
            audio_url = f'https://storage.googleapis.com/vocodes-public{audio_path}'
            
            try:
                audio_response = requests.get(audio_url)
                audio = AudioSegment.from_file(io.BytesIO(audio_response.content), format="wav")
                audio.export(output_file, format="mp3")
                print(f'Saved audio file: {audio_url}')
                return output_file
            except Exception as e:
                print(f"Error saving audio file: {e}")
                return None

        elif job_status in ['complete_failure', 'dead']:
            print(f'TTS job failed: {job_status}')
            return None

        time.sleep(polling_interval)

def main():
    username = input('Enter your FakeYou username: ')
    password = input('Enter your FakeYou password: ')
    
    # Step 1: Get the session cookie by authenticating with the API
    session_cookie = authenticate(username, password)

    if not session_cookie:
        print("Authentication failed. Exiting.")
        return

    filename = input('Enter the filename of your Ren\'Py script: ')
    script_dir = os.path.dirname(filename)
    base_filename = os.path.splitext(os.path.basename(filename))[0]

    with open(filename, 'r') as file:
        lines = file.readlines()

    dialogue_pattern = re.compile(r'^(\s*)(\w+)( ")(.*?)(")')

    new_lines = []

    for index, line in enumerate(lines):
        match = dialogue_pattern.match(line)
        if match:
            indentation, character, quote1, dialogue, quote2 = match.groups()

            dialogue = dialogue.replace('[mcs.morty.name]', 'Morty')
            dialogue = dialogue.replace('[mcs.rick.name]', 'Rick')
            dialogue = dialogue.replace('[mcs.morty.age]', '')
            dialogue = dialogue.replace('{i}', '')
            dialogue = dialogue.replace('[mcs.jerry.name]', 'jerry')
            dialogue = dialogue.replace('{b}', '')
            dialogue = dialogue.replace('[mcs.sum.age]', '')
            dialogue = dialogue.replace('[mcs.beth.age]', '')
            dialogue = dialogue.replace('[defaults.morty.age_galactic]', '')
            dialogue = dialogue.replace('[mcs.sum.nickname]', '')
            dialogue = dialogue.replace('[mcs.sum.name]', 'summer')
            dialogue = dialogue.replace('[mcs.beth.nickname]', '')
            dialogue = dialogue.replace('[mcs.beth.n.comma]', '')
            dialogue = dialogue.replace('[mcs.beth.n.mom]', '')
            dialogue = dialogue.replace('[[mcs.beth.petname]]', 'sweetie')
            dialogue = dialogue.replace('[mcs.beth.n.mom]', '')
            dialogue = dialogue.replace('[mcs.beth.n.beth]', '')
            dialogue = dialogue.replace('[mcs.jessica.name]', 'jessica')
            dialogue = dialogue.replace('[mcs.tricia.name]', 'tricia')
            dialogue = dialogue.replace('[mcs.sum.n.bro]', 'morty')
            dialogue = dialogue.replace('[mcs.sum.n.morty]', 'morty')

            
            input_lower = character.lower()
            voice_token = None
            if 'm' in input_lower or 'mu' in input_lower or 'mt' in input_lower :
                voice_token = voice_m
            elif input_lower == 'o':
                voice_token = voice_m  
            elif input_lower == 'rr':   
                voice_token = voice_ry
            elif input_lower == 'ry':
                voice_token = voice_ry
            elif input_lower == 'rl':
                voice_token = voice_ry
            elif input_lower == 'r':
                voice_token = voice_ry
            elif input_lower == 'rm':
                voice_token = voice_ry
            elif input_lower == 'b':
                voice_token = voice_b
            elif input_lower == 's':
                voice_token = voice_s
            elif input_lower == 'y':
                voice_token = voice_y    
            elif input_lower == 'j':
                voice_token = voice_j
            #elif input_lower == 't': # fix it with the new voice 
            #    voice_token = voice_m
            #elif input_lower == 'n': # fix it with the new voice 
            #    voice_token = voice_m                
            else:
                voice_token = None
            
            if voice_token and dialogue.strip():
                voice_file = generate_voice(voice_token, dialogue, index, base_filename, script_dir, session_cookie)
                if voice_file:
                    voice_command = f'{indentation}voice "{voice_file}"\n'
                    new_lines.append(voice_command)

            new_lines.append(line)
        else:
            new_lines.append(line)

    new_filename = f"{base_filename}_new{os.path.splitext(filename)[1]}"
    new_file_path = os.path.join(script_dir, new_filename)

    with open(new_file_path, 'w') as file:
        file.writelines(new_lines)

    print("Script processing complete.")

if __name__ == "__main__":
    main()
