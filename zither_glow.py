import time
import random
import mido

PORT_NAME = 'ZitherGlow_Port'

def main():
    print("==================================================")
    print("      ZitherGlow: A Pentatonic MIDI Generator     ")
    print("          Created by Zeqi Chen (George)           ")
    print("==================================================")

    # 1. INTERACTION STEP 1: Choose Musical Mode / 选择一个调式
    print("\n[STEP 1] Select traditional Chinese pentatonic mode:")
    print("  1: Gong Mode (宫调式 - Bright, grand, like epic fairy tales)")
    print("  2: Yu Mode   (羽调式 - Melancholy, nostalgic, like martial arts films)")
    
    mode_choice = input("Enter number (1 or 2): ").strip()
    
    # Define arrays based on user choice
    if mode_choice == "1":
        # C Gong Mode (C Major Pentatonic): C4, D4, E4, G4, A4, C5...
        pentatonic_scale = [60, 62, 64, 67, 69, 72, 74, 76, 79, 81]
        print("-> Gong Mode selected.")
    else:
        # A Yu Mode (A Minor Pentatonic): A3, C4, D4, E4, G4, A4...
        # Default to Yu mode if input is invalid
        pentatonic_scale = [57, 60, 62, 64, 67, 69, 72, 74, 76, 79]
        print("-> Yu Mode selected.")

    # 2. INTERACTION STEP 2: Choose Tempo/Emotion / 选择速度与情绪
    print("\n[STEP 2] Select performance tempo and texture:")
    print("  1: Flowing Water (流水 - Slow, spacious, peaceful atmosphere)")
    print("  2: Rapid Strings (急弦 - Fast, dense, virtuoso-style plucking)")
    
    tempo_choice = input("Enter number (1 or 2): ").strip()
    
    if tempo_choice == "2":
        note_duration = 0.2  # Fast tempo 更快的速度
        rest_probability = 0.10  # Less silence, more notes 更多音符
        print("-> Rapid Strings mode selected.")
    else:
        note_duration = 0.5  # Slow, meditative tempo 更慢的速度
        rest_probability = 0.30  # More musical rests 更多留白
        print("-> Flowing Water mode selected.")

    # 3. Setup Virtual MIDI Connection / 建立虚拟MIDI连接
    try:
        midi_output = mido.open_output(PORT_NAME, virtual=True)
        print("\n==================================================")
        print(f"STATUS: MIDI Player is online via '{PORT_NAME}'")
        print("ACTION: Switch to Logic Pro Guzheng track now.")
        print("        Press Logic's RECORD button (R) to capture.")
        print("        Press Ctrl+C in Terminal to STOP anytime.")
        print("==================================================")
        time.sleep(3.0)

        # 4. Core Generative Loop / 循环实现
        while True:
            # Pick a note under scale constraint
            current_note = random.choice(pentatonic_scale)
            # Add subtle humanized volume variations
            current_velocity = random.randint(65, 95)

            # Traditional Chinese 'Rest / 留白' Logic
            if random.random() < rest_probability:
                time.sleep(note_duration)
                continue

            # Play the note
            note_on_msg = mido.Message('note_on', note=current_note, velocity=current_velocity)
            midi_output.send(note_on_msg)

            time.sleep(note_duration)

            # Stop the note
            note_off_msg = mido.Message('note_off', note=current_note, velocity=0)
            midi_output.send(note_off_msg)

    except KeyboardInterrupt:
        print("\n==================================================")
        print("ZitherGlow stopped gracefully. Thanks for using Zeqi's ZitherGlow!")
        print("==================================================")
    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
