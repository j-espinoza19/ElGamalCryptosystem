import tkinter as tk
from elgamal_functions import (
    is_prime, rootprimitivity, generate_prime_and_root,
    generate_exponent, k_inverse, encryption,
    decryption, message_to_blocks, blocks_to_message
)

def on_generate_random():
    global p, g, e, gb
    p, g = generate_prime_and_root(block_size.get())
    e = generate_exponent(p)
    gb = pow(g, e, p)
    entry_p.set(p)
    entry_g.set(g)
    entry_e.set(e)
    result_public_key.set(gb)

def on_manual_entry():
    try:
        global p, g, e, gb
        p = int(entry_p.get())
        g = int(entry_g.get())
        e = int(entry_e.get())
        
        if not is_prime(p):
            result_message.set("Error: p is not a prime number.")
            return

        if not rootprimitivity(p, g):
            result_message.set("Error: g is not a primitive root of p.")
            return

        if not (1 < e < p - 1):
            result_message.set("Error: e must be between 1 and p-1.")
            return

        prime_minlimit = 256 ** 2 if block_size.get() == 2 else 256
        if not (p >= prime_minlimit):
            result_message.set("Error: p must be equal or greater than the block size.")
            return
    
        gb = pow(g, e, p)
        result_public_key.set(gb)
        result_message.set(f"Manual Entry - Prime p: {p}, Root g: {g}, Exponent e: {e}")
    except ValueError:
        result_message.set("Error: Please enter valid numeric values.")

def on_encrypt():
    global int_blocks, x, k, encrypted_blocks
    message = entry_message.get()
    p = int(entry_p.get())
    g = int(entry_g.get())
    e = int(entry_e.get())
    gb = pow(g, e, p)
    x = random.randint(2, p - 2)
    int_blocks = message_to_blocks(message, block_size.get())
    k = pow(gb, x, p)
    encrypted_blocks = encryption(int_blocks, k, p)
    result_encryption.set(", ".join(map(str, encrypted_blocks)))

def on_decrypt():
    encrypted_text = entry_encrypted.get().strip()
    try:
        encrypted_blocks = [int(block) for block in encrypted_text.replace(",", "").split()]
        decrypted_blocks = decryption(encrypted_blocks, k, p)
        result_decryption.set(blocks_to_message(decrypted_blocks))
    except ValueError:
        result_message.set("Error: Invalid input format for encrypted message.")

def on_show_values():
    global k, p
    i = k_inverse(k, p)
    values = f"x: {x}, p: {p}, g: {g}, k: {k}, i: {i}"
    result_values.set(values)

def reset_fields():
    entry_p.set("")
    entry_g.set("")
    entry_e.set("")
    entry_message.set("")
    entry_encrypted.set("")
    result_encryption.set("")
    result_decryption.set("")
    result_message.set("")
    result_values.set("")
    result_public_key.set("")
    block_size.set(1)

# Create the main window
root = tk.Tk()
root.title("CRYPTOSYSTEM EL GAMAL")
root.geometry("800x700")  # Set the window size to be larger

# Variables for the input fields
block_size = tk.IntVar(value=1)  # Default to 1 block size
entry_p = tk.StringVar()
entry_g = tk.StringVar()
entry_e = tk.StringVar()
entry_message = tk.StringVar()
entry_encrypted = tk.StringVar()
result_encryption = tk.StringVar()
result_decryption = tk.StringVar()
result_message = tk.StringVar()
result_values = tk.StringVar()
result_public_key = tk.StringVar()

# Create and organize the widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Block Division Size radio buttons
tk.Label(frame, text="Block Division Size:").grid(row=0, column=0, sticky="e", pady=(0, 20))
tk.Radiobutton(frame, text="Single Block", variable=block_size, value=1).grid(row=0, column=1, sticky="w")
tk.Radiobutton(frame, text="Double Blocks", variable=block_size, value=2).grid(row=0, column=1, sticky="e")

# Manual input fields
tk.Label(frame, text="Prime p:").grid(row=2, column=0, sticky="e")
tk.Entry(frame, textvariable=entry_p, width=50).grid(row=2, column=1)

tk.Label(frame, text="Root g:").grid(row=3, column=0, sticky="e")
tk.Entry(frame, textvariable=entry_g, width=50).grid(row=3, column=1)

tk.Label(frame, text="Exponent e:").grid(row=4, column=0, sticky="e")
tk.Entry(frame, textvariable=entry_e, width=50).grid(row=4, column=1, pady=5)

# Buttons to generate random values and manually enter values
btn_generate = tk.Button(frame, text="Generate Random", command=on_generate_random)
btn_generate.grid(row=5, column=0, pady=(0, 20))

btn_manual = tk.Button(frame, text="Enter Manually", command=on_manual_entry)
btn_manual.grid(row=5, column=1, pady=(0, 20))

# Text field for the message to encrypt
tk.Label(frame, text="Message:").grid(row=6, column=0, sticky="e", pady=(0, 20))
tk.Entry(frame, textvariable=entry_message, width=50).grid(row=6, column=1, pady=(0, 20))

# Button to encrypt and show the result
btn_encrypt = tk.Button(frame, text="Encrypt", command=on_encrypt)
btn_encrypt.grid(row=7, column=1, pady=5)

tk.Label(frame, text="Encrypted Message:").grid(row=8, column=0, sticky="e")
tk.Entry(frame, textvariable=result_encryption, width=50, state="readonly").grid(row=8, column=1)

# Text field for the encrypted message
tk.Label(frame, text="Encrypted Message:").grid(row=9, column=0, sticky="e")
tk.Entry(frame, textvariable=entry_encrypted, width=50).grid(row=9, column=1, pady=(0, 20))

# Button to decrypt and show the result 
btn_decrypt = tk.Button(frame, text="Decrypt",command=on_decrypt) 

btn_decrypt.grid(row=10, column=1) 

tk.Label(frame, text="Decrypted Message:").grid(row=11, column=0, sticky="e") 
tk.Entry(frame, textvariable=result_decryption, width=50, state="readonly").grid(row=11, column=1) 

# Result and validation messages 
tk.Label(frame, textvariable=result_message, fg="red").grid(row=12, column=0, columnspan=2) 

# Button to show values of variables
btn_show_values = tk.Button(frame, text="Show Values", 
command=on_show_values) 
btn_show_values.grid(row=15, column=1, pady=5) 

tk.Label(frame, textvariable=result_values, fg="blue").grid(row=14, column=0, columnspan=2) 

# Label to show the public key 
tk.Label(frame, text="Public Key:").grid(row=16, column=0,
sticky="e") 
tk.Entry(frame,textvariable=result_public_key, width=50,
state="readonly").grid(row=16, column=1) 

# Buttons to exit and reset 
btn_exit = tk.Button(frame, text="Exit", command=root.quit) 
btn_exit.grid(row=19, column=0, pady=50) 

btn_reset = tk.Button(frame, text="Reset", command=reset_fields) 
btn_reset.grid(row=19, column=1, pady=50) 

# Labels to show authors 
tk.Label(root, text="Developed by: Arnau Cano & Josueth Espinoza", fg="gray").pack(side="bottom", pady=5) 

root.mainloop()
